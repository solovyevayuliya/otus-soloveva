document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        var textarea = document.querySelector('textarea');
        var text = textarea.value;

        fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: 'text=' + encodeURIComponent(text)
        })
        .then(function(response) {
            return response.text();
        })
        .then(function(processedText) {
            // Обновление страницы с обработанным текстом
            textarea.value = processedText;
        });
    });
});