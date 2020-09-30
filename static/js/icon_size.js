$(document).ready(function() {
    $('#dropdown-form').submit(function(e) {

        var iconElement = $('#icon-element').val();
        var forwardSlashCount = 0;
        var newIconElement = [];
        var sizeChanged = false;

        for (let i = 0; i < iconElement.length; i++) {

            var letter = iconElement[i];

            if (letter == '/') {
                forwardSlashCount++;
            };

            if (forwardSlashCount == 4 && sizeChanged == false) {
                newIconElement.push('/18');
                sizeChanged = true;
            };

            if (forwardSlashCount != 4) {
                newIconElement.push(letter);
            };
            
       }
       $('#icon-element').val(newIconElement.join(''))
       e.submit();
    });
});