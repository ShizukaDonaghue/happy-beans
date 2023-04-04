// Script to close alert messages
$(document).ready(function() {
    setTimeout(function(){
        if ($('#msg').length > 0) {
            $('#msg').remove();
        }
    }, 3000);
});

// Scrip to close Bootstrap hamburger menu when clicked outside the menu
// Code source: https://stackoverflow.com/questions/71915612/how-to-close-hamburger-menu-when-clicked-outside-the-menu-using-javascript
$(document).on('click', function () {
    $('#navbarContents').collapse('hide');
});