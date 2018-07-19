function deleteCalendarEntry(entry){
    var $entry = $(entry)
    // console.log(this.entry)
    $entry.parent().parent().remove()
    var id = $entry.data('id')
    console.log(id)
    $.ajax({
        url : 'entry/delete/'+id,
        method:'DELETE',
        beforeSend: function(xhr){
            xhr.setRequestHeader('X-CSRFToken',csrf_token)
        }
        // data:{
        //     "csrfmiddlewaretoken":csrf_token    
        // }
    })
}