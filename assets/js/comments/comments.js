$(document).ready(function() {
    $(document).on('submit', '.commentCreateForm', function(e) {
        e.preventDefault();
        e.stopPropagation();
        var form = $(this);
        var token = $('input[name=csrfmiddlewaretoken]').val();
        var content = form.find('#id_content').text();
        var url = form.attr('action');

        $.ajax({
            method: 'POST',
            url: url,
            data: {
                content: content
            },
            beforeSend: function(request) {
                request.setRequestHeader('X-CSRFToken', token);
            },
            success: function(data) {
                console.log(data);
            },
            error: function(xhr, exception) {
                console.error(xhr);
                console.error(exception);
            }
        });
    });
});