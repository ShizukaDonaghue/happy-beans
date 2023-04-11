# Testing

Return to [README](https://github.com/ShizukaDonaghue/happy-beans)

## Code Validation

### HTML
All the pages were run through [W3C HTML Validator](https://validator.w3.org/) to check for any issues and syntax errors.
Initiallly, there were errors identified due to a missing closing tag and image height values.
Once these issues were rectified, all pages passed validation, except for errors related to Summernote and Bootstrap codes.
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
  <summary>Post and Update Recipe Pages - Errors identified for Summernote fields</summary> 
  
  
 

</details>

Errors were identified in these pages, however, they were all related to Summernote widget that is used in the recipe form for these pages.
The same errors were identified for both pages as the same form is used in both pages. 
Since all the errors were related to Summernote codes and not my own, these were not rectified. 
These errors do not affect the functionality of the application.

<details>
  <summary>Recipe Details Page - Errors identified for Bootstrap CSS property</summary> 
  
  <img src="docs/images/validation/post-and-update-recipe-pages.pdf" width=800>

</details>


********************XXXXXXXREPLACE SCREENSHOT OF ERROR - TYPO IN THE SOURCE CODEXXXXXXXXXXXX*************
********************xxxxxxxCHECK FOR ERROR AGAIN!!!XXXXXXXXXXXXXXXXXXXXXXXXXXX*******************


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

#### Happy Beans project
<details>
  <summary>asgi.py - No issues or errors</summary> 
  
  <img src="docs/images/validation/asgi.png">

</details>

<details>
  <summary>settings.py - No issues or errors</summary> 
  
  <img src="docs/images/validation/settings.png">

Note: `# noqa` was added to Django generated codes under "AUTH_PASSWORD_VALIDATORS" and also to Cloudinary storage under "STATICFILES_STORAGE" to ignore "line too long" errors.

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
  
  <img src="docs/images/validation/template-tags.png">

</details>






Feature | Action | Expected Result | PASS/FAIL
---|---|---|---

