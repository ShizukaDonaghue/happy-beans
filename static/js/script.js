// Script to close alert messages

$(document).ready(function() {
    setTimeout(function(){
        if ($('#msg').length > 0) {
            $('#msg').remove();
        }
    }, 3000);
});