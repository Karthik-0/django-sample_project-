from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Entry
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import EntryForm
from django.contrib.auth.forms import UserCreationForm

def index(request):
    entries = Entry.objects.all()
    return render(request,'myapp/index.html',{'entries':entries})

@login_required
def details(request,pk):
    entry = Entry.objects.get(id=pk)
    return render(request,'myapp/details.html',{'entry':entry})

@login_required
def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            
            Entry.objects.create(
                name = name,
                date = date,
                author = request.user,
                description = description
            ).save()
            return HttpResponseRedirect('/dashboard')
    else:
        form = EntryForm()
    
    return render(request,'myapp/form.html',{'form':form})


@login_required
def delete(request,pk):
    if request.method == 'DELETE':
        entry = get_object_or_404(Entry,pk=pk)
        print(entry)
        entry.delete()
    return HttpResponseRedirect('/dashboard')

@login_required
def dashboard(request):
    entries = Entry.objects.filter(author=request.user)
    return render(request,'myapp/dashboard.html',{'entries':entries})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request,user)
            return redirect('/dashboard')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})