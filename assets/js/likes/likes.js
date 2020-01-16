$(document).ready(function() {
    $(document)
        .on('click', '.likeBtn', function(e) {
            e.preventDefault();
            e.stopPropagation();
            var button = $(this);
            var url = button.attr('data-url');
            var token = $('input[name=csrfmiddlewaretoken]').val();
            var counter = button.find('.likeCount');
            var likeAction = button.find('.likeAction');
            var currentLikesCount = parseInt(counter.html());

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
                            button.removeClass('btn-success').addClass('btn-danger');
                            likeAction.text('Dislike');
                            counter.html(currentLikesCount + 1);
                        } else {
                            button.removeClass('btn-danger').addClass('btn-success');
                            likeAction.text('Like');
                            counter.html(currentLikesCount - 1);
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