# Happy Beans - Testing

Return to [README](https://github.com/ShizukaDonaghue/happy-beans)

## Code Validation

### HTML
[W3C HTML Validator](https://validator.w3.org/) was used to validate HTML codes used in the application.
Each page was checked for any issues and syntax errors.
Initiallly, there were errors resulting from a missing closing tag and image height values.
Once these issues were rectified, all pages passed validation, except for the errors related to Summernote codes and Bootstrap property.
Please see below results for each page.

<details>
  <summary>Home Page - No isses or errors</summary>
  
  <img src="docs/images/validation/home-page.png">

</details>

<details>
  <summary>Sigup Page - No issues or errors</summary>
  
  <img src="docs/images/validation/signup-page.png">

</details>

<details>
  <summary>Login Page - No issues or errors</summary>
  
  <img src="docs/images/validation/login-page.png">

</details>


<details>
  <summary>Logout Page - No issues or errors</summary>
  
  <img src="docs/images/validation/logout-page.png">

</details>


<details>
  <summary>Browse Recipes Page - No issues or errors</summary>
  
  <img src="docs/images/validation/browse-recipes-page.png">

</details>

<details>
  <summary>My Favourites Page - No issues or errors</summary> 
  
  <img src="docs/images/validation/my-favourites-page.png">

</details>

<details>
  <summary>My Recipes Page - No issues or errors</summary> 
  
  <img src="docs/images/validation/my-recipes-page.png">

</details>

<details>
  <summary>Update Comment Page - No issues or errors</summary> 
  
  <img src="docs/images/validation/update-comment-page.png">

</details>

<details>
  <summary>403 Error Page - No issues or errors</summary> 
  
  <img src="docs/images/validation/403-error-page.png">

</details>

<details>
  <summary>404 Error Page - No issues or errors</summary> 
  
  <img src="docs/images/validation/404-error-page.png">

</details>


<details>
  <summary>Post Recipe Page - Errors identified for Summernote fields</summary> 
  
  <img src="docs/images/validation/post-recipe-page-1.png">
  <img src="docs/images/validation/post-recipe-page-2.png">
  <img src="docs/images/validation/post-recipe-page-3.png">
  <img src="docs/images/validation/post-recipe-page-4.png">

The errors identified were all related to Summernote widget that is used in the recipe form. Since the errors resulted from Summernote codes, these were left untouched.
However, these errors do not affect the functionality of the application.

</details>

<details>
  <summary>Update Recipe Page - Errors identified for Summernote fields</summary> 
  
  <img src="docs/images/validation/update-recipe-page-1.png">
  <img src="docs/images/validation/update-recipe-page-2.png">
  <img src="docs/images/validation/update-recipe-page-3.png">
  <img src="docs/images/validation/update-recipe-page-4.png">

The errors identified were all related to Summernote widget that is used in the recipe form. Since the errors resulted from Summernote codes, these were left untouched.
However, these errors do not affect the functionality of the application.

</details>

<details>
  <summary>Recipe Details Page - Errors identified for Bootstrap CSS Property</summary> 
  
  <img src="docs/images/validation/recipe-details-page-1.png">
  <img src="docs/images/validation/recipe-details-page-2.png">

The errors identified were all related to Bootstrap CSS property. Since the errors resulted from Bootstrap codes, these were left untouched.

</details>

### CSS
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate CSS codes used in the application and no issues or errors were found.

<details>
  <summary>CSS Codes - No issues or errors</summary> 
  
  <img src="docs/images/validation/css.png">

</details>

### JavaScript
[JSHint](https://jshint.com/) was used to validate JavaScript codes used in the application and no issues or errors were found.

<details>
  <summary>JavaScript Codes - No issues or errors</summary> 
  
  <img src="docs/images/validation/javascript.png">

</details>

### Python
[CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate Python codes used throughout the application and no issues or errors were found.
Please see the results for each page.

#### Happy Beans Project
<details>
  <summary>asgi.py - No issues or errors</summary> 
  
  <img src="docs/images/validation/asgi.png">

</details>

<details>
  <summary>settings.py - No issues or errors</summary> 
  
  <img src="docs/images/validation/settings.png">

Note: `# noqa` was added to Django generated codes under "AUTH_PASSWORD_VALIDATORS" and also to Cloudinary storage under "STATICFILES_STORAGE" to ignore "line too long" errors as these could not be shortened without breaking the codes.

</details>

<details>
  <summary>urls.py - No issues or errors</summary> 
  
  <img src="docs/images/validation/urls-project.png">

</details>

<details>
  <summary>wsgi.py - No issues or errors</summary> 
  
  <img src="docs/images/validation/wsgi.png">

</details>

#### Recipe App
<details>
  <summary>admin.py - No issues or errors</summary> 
  
  <img src="docs/images/validation/admin.png">

</details>

<details>
  <summary>apps.py - No issues or errors</summary> 
  
  <img src="docs/images/validation/apps.png">

</details>

<details>
  <summary>filters.py - No issues or errors</summary> 
  
  <img src="docs/images/validation/filters.png">

</details>

<details>
  <summary>forms.py - No issues or errors</summary> 
  
  <img src="docs/images/validation/forms.png">

</details>

<details>
  <summary>models.py - No issues or errors</summary> 
  
  <img src="docs/images/validation/models.png">

</details>

<details>
  <summary>urls.py - No issues or errors</summary> 
  
  <img src="docs/images/validation/urls.png">

</details>

<details>
  <summary>validators.py - No issues or errors</summary> 
  
  <img src="docs/images/validation/validators.png">

</details>

<details>
  <summary>views.py - No issues or errors</summary> 
  
  <img src="docs/images/validation/views.png">

</details>

<details>
  <summary>recipeapp_tags.py - No issues or errors</summary> 
  
  <img src="docs/images/validation/recipeapp-tags.png">

</details>

## Accessibility
[Wave Web Accessibility Evaluation Tools](https://wave.webaim.org/) was used to test accessibility and no errors or contrast errors were found.

<details>
  <summary>Home Page - No errors</summary>
  
  <img src="docs/images/validation/wave-home-page.png">

</details>

<details>
  <summary>Sigup Page - No errors</summary>
  
  <img src="docs/images/validation/wave-signup-page.png">

</details>

<details>
  <summary>Login Page - No errors</summary>
  
  <img src="docs/images/validation/wave-login-page.png">

</details>


<details>
  <summary>Logout Page - No errors</summary>
  
  <img src="docs/images/validation/wave-logout-page.png">

</details>


<details>
  <summary>Browse Recipes Page - No errors</summary>
  
  <img src="docs/images/validation/wave-browse-recipes-page.png">

</details>

<details>
  <summary>My Favourites Page - No errors</summary> 
  
  <img src="docs/images/validation/wave-my-favourites-page.png">

</details>

<details>
  <summary>My Recipes Page - No errors</summary> 
  
  <img src="docs/images/validation/wave-my-recipes-page.png">

</details>

<details>
  <summary>Update Comment Page - Missing Form Label Error</summary> 
  
  <img src="docs/images/validation/wave-update-comment-page.png">

The error identified was a missing form label for the Crispy Form used in the Comment field. Since the error resulted from the Crispy Form codes, this was left untouched.

</details>

<details>
  <summary>403 Error Page - No errors</summary> 
  
  <img src="docs/images/validation/wave-403-page.png">

</details>

<details>
  <summary>404 Error Page - No errors</summary> 
  
  <img src="docs/images/validation/wave-404-page.png">

</details>


<details>
  <summary>Post Recipe Page - No errors</summary> 
  
  <img src="docs/images/validation/wave-post-recipe-page-1.png">

</details>

<details>
  <summary>Update Recipe Page - Empty Link Error</summary> 
  
  <img src="docs/images/validation/wave-update-recipe-page.png">

The error identified was for an empty link for the current recipe image loaded. Since the error resulted from the Crispy Form codes, this was left untouched.

</details>

<details>
  <summary>Recipe Details Page - Missing Form Label Error</summary> 
  
  <img src="docs/images/validation/wave-recipe-details-page.png">

The error identified was a missing form label for the Crispy Form used in the Comment field. Since the error resulted from the Crispy Form codes, this was left untouched.

</details>
