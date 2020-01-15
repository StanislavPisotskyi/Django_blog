$(document).ready(function() {
    $(document)
        .on('submit', '.likeForm', function(e) {
            e.preventDefault();
            e.stopPropagation();
            var form = $(this);
            var url = form.attr('action');
            var token = form.find('input[name=csrfmiddlewaretoken]').val();
            var button = form.find('input[type=submit]')

            $.ajax({
                method: 'POST',
                url: url,
                data: {},
                beforeSend: function(request) {
                    request.setRequestHeader('X-CSRFToken', token);
                },
                success: function(data) {
                    if(data.success) {
                        if(data.action === 'like') {
                            button.removeClass('btn-success').addClass('btn-danger').val('Dislike');
                        } else {
                            button.removeClass('btn-danger').addClass('btn-success').val('Like');
                        }
                    }
                    console.log(data);
                },
                error: function(xhr, exception) {
                    console.error(xhr);
                    console.error(exception);
                }
            });
        });
});