// Script to close alert messages
$(document).ready(function() {
    setTimeout(function() {
        if ($('#msg').length > 0) {
            $('#msg').remove();
        }
    }, 3000);
});

// Script to close Bootstrap hamburger menu when clicked outside the menu
$(document).ready(function() {
    $(document).click(function() {
        $('#navbarContents').collapse('hide');
    });
});