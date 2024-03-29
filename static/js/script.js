// Closes alert messages after 3 seconds
$(document).ready(function() {
    setTimeout(function() {
        if ($('#msg').length > 0) {
            $('#msg').remove();
        }
    }, 3000);
});

// Closes Bootstrap hamburger menu when clicked outside the menu
$(document).ready(function() {
    $(document).click(function() {
        $('#navbarContents').collapse('hide');
    });
});

// Validates Post Recipe and Update Recipe forms and raises error messages where required
$(document).ready(function() {
    $('.recipe-form').validate({
        rules: {
            title: 'required',
            description: 'required',
            meal_type: 'required',
            main_ingredient: 'required',
            difficulty: 'required',
            prep_time: 'required',
            cook_time: 'required',
            serves: 'required',
        },

        messages: {
            title: 'Please enter the title of the recipe.',
            description: 'Please enter the description.',
            meal_type: 'Please select a meal type from the list.',
            main_ingredient: 'Please select a main ingredient from the list.',
            difficulty: 'Please select a difficulty level from the list.',
            prep_time: 'Please enter the preparation time in minutes (numbers only).',
            cook_time: 'Please enter the cooking time in minutes (numbers only).',
            serves: 'Please enter the number of servings (numbers only).',
        },

        submitHandler: function(form) {
            form.submit();
        }
    });
});

