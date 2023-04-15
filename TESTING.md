# Happy Beans - Testing

Return to [README](https://github.com/ShizukaDonaghue/happy-beans)

## Code Validation

### HTML
[W3C HTML Validator](https://validator.w3.org/) was used to validate HTML codes used in the application. All the pages were check for any issues or syntax errors. The only errors identified were for Summernote fields.
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
  <summary>Post Recipe Page - Errors identified for Summernote fields</summary> 
  
  <img src="docs/images/validation/post-recipe-page-1.png">
  <img src="docs/images/validation/post-recipe-page-2.png">
  <img src="docs/images/validation/post-recipe-page-3.png">
  <img src="docs/images/validation/post-recipe-page-4.png">

</details>

The errors identified were all related to Summernote widget that is used in the recipe form. Since the errors resulted from Summernote codes, these were not addressed. However, these errors do not affect the functionality of the application.

<details>
  <summary>Update Recipe Page - Errors identified for Summernote fields</summary> 
  
  <img src="docs/images/validation/update-recipe-page-1.png">
  <img src="docs/images/validation/update-recipe-page-2.png">
  <img src="docs/images/validation/update-recipe-page-3.png">
  <img src="docs/images/validation/update-recipe-page-4.png">

</details>

The errors identified were all related to Summernote widget that is used in the recipe form. Since the errors resulted from Summernote codes, these were not addressed. However, these errors do not affect the functionality of the application.

<details>
  <summary>Recipe Details Page - Errors identified for Summernote fields</summary> 
  
  <img src="docs/images/validation/recipe-details-page-1.png">
  <img src="docs/images/validation/recipe-details-page-2.png">

</details>

The errors identified were all related to CSS property used in Summernote list items for unordered list. Since the errors resulted from Summernote codes, these were not addressed.

<details>
  <summary>403 Error Page - No issues or errors</summary> 
  
  <img src="docs/images/validation/403-error-page.png">

</details>

<details>
  <summary>404 Error Page - No issues or errors</summary> 
  
  <img src="docs/images/validation/404-error-page.png">

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

</details>

Note: `# noqa` was added to Django generated codes under "AUTH_PASSWORD_VALIDATORS" and also to Cloudinary storage under "STATICFILES_STORAGE" for "line too long" errors to be ignored as these could not be shortened without breaking the codes.

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
[Wave Web Accessibility Evaluation Tools](https://wave.webaim.org/) was used to test accessibility. The only errors identified were for Crispy Form fields. Please see below results for each page.

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
  
  <img src="docs/images/validation/wave-browse-recipes.png">

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
  <summary>Update Comment Page - Missing form label error</summary> 
  
  <img src="docs/images/validation/wave-update-comment-page.png">

</details>

The error identified was a missing form label for the Crispy Form used in the Comment field. Since the error resulted from the Crispy Form codes, this was not addressed.

<details>
  <summary>Post Recipe Page - No errors</summary> 
  
  <img src="docs/images/validation/wave-post-recipe-page.png">

</details>

<details>
  <summary>Update Recipe Page - Empty link error</summary> 
  
  <img src="docs/images/validation/wave-update-recipe-page.png">

</details>

The error identified was for an empty link for the current recipe image loaded. Since the error resulted from the Crispy Form codes, this was not addressed.
<details>
  <summary>Recipe Details Page - Missing form label error</summary> 
  
  <img src="docs/images/validation/wave-recipe-details-page.png">

</details>

The error identified was a missing form label for the Crispy Form used in the Comment field. Since the error resulted from the Crispy Form codes, this was not addressed.

<details>
  <summary>403 Error Page - No errors</summary> 
  
  <img src="docs/images/validation/wave-403-page.png">

</details>

<details>
  <summary>404 Error Page - No errors</summary> 
  
  <img src="docs/images/validation/wave-404-page.png">

</details>

## Lighthouse
XXXXXXXXXXXXXXXX  NEED SCREENSHOTS  XXXXXXXXXXXXXXXXXXXX

## Responsiveness
Responsiveness was testing using [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) and no issues were found.
This included the following devices:
* iPhone 5/SE, 6/7/8, 6/7/8 Plus, SE, XR, 12 Pro, and X
* iPad Air and iPad Mini
* Samsung Galaxy S8+, S9+, S20 Ultra, A51/71
* Microsoft Surface Pro 7 and Duo
* Nest Hub and Hub Max

XXXXXXXXXXXXXXXX  NEED SCREENSHOTS  XXXXXXXXXXXXXXXXXXXX (PP4 walkthrough)

## Browser Compatibility
Browser compatibility was checked for the following browsers and no issues were found:
* Google Chrome
* Microsoft Edge
* Apple Safari
* Mozilla Firefox
* Opera

The application was also tested manually on the follwoing devices and no issues were found:
* iPhone 12
* iPhone 11
* iPhone XR
* iPhone 8
* iPad 8
* HP Elitebook 840
* Dell XPS

XXXXXXXXXXXXXXXX  NEED SCREENSHOTS  XXXXXXXXXXXXXXXXXXXX (PP4 walkthrough)

## Manual Testing
Manual testing was performed using Google Chrome to verify that all the features functioned as expected and no issues were found.

### Browser Tab
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Favicon | Display | Favicon is displayed correctly in the browser tab | PASS
Title | Display | "Home" is displayed as the title of the page for Home page | PASS
Title | Display | "Browse Recipes" is displayed as the title of the page for Browse Recipes page | PASS
Title | Display | The title of the recipe is displayed as the title of the page for each Recipe Details page | PASS
Title | Display | "My Favourites" is displayed as the title of the page for My Favourites page | PASS
Title | Display | "My Recipes" is displayed as the title of the page for My Recipes page | PASS
Title | Display | "Post Recipe" is displayed as the title of the page for Post Recipe page | PASS
Title | Display | "Update Recipe" is displayed as the title of the page for Update Recipe page | PASS
Title | Display | "Update Comment" is displayed as the title of the page for Update Comment page | PASS
Title | Display | "Signup" is displayed as the title of the page for Signup page | PASS
Title | Display | "Login" is displayed as the title of the page for Login page | PASS
Title | Display | "Logout" is displayed as the title of the page for Logout page | PASS

### Navigation Bar
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Menu | Display | Links displayed side by side in the navigation bar for screen sizes with a minimum width of 1200px | PASS
Position | Display | Navigation bar always stays at the top of the screen | PASS
Logo | Click | Navigates to Home page | PASS
Home Link | Click | Navigates to Home page | PASS
Browse Recipes Link | Click |Navigates to Browse Recipes page | PASS
Sign Up Link | Display | Only available if the user is not logged in | PASS
Sign Up Link | Click | Navigates to Sign Up page | PASS
Log In Link | Display | Only available if the user is not logged in | PASS
Log In Link | Click | Navigates to Log In page | PASS
Log Out Link | Display | Only available if the user is logged in | PASS
Log Out Link | Click | Navigates to Log Out page | PASS
My Favourites Link | Display | Only available if the user is logged in | PASS
My Favourites Link | Click| Navigates to My Favourites page | PASS
My Recipes Link | Display | Only available if the user is logged in | PASS
My Recipes Link | Click| Navigates to My Recipes page | PASS
Post a Recipe Link | Display | Only available if the user is logged in | PASS
Post a Recipe Link | Click| Navigates to Post a Recipe page to | PASS
All Links | Hover | Colour changes to green with hover effect | PASS
All Links | Display | Active page is shown in green | PASS

### Hamburger Menu
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Menu | Display | Hamburger menu displayed in the navigation bar for screen sizes less than 1200px in width | PASS
Animation | Click | Animation functions correctly - X is displayed while the menu is open | PASS
Menu Closure | Click | Hamburger menu closes when clicked outside the menu | PASS
Menu Closure | Click | Hamburger menu closes when clicked on X | PASS 
Logo | Click | Navigates to Home page | PASS
Home Link | Click | Navigates to Home page | PASS
Browse Recipes Link | Click | Navigates to Browse Recipes page | PASS
Sign Up Link | Display | Only available if the user is not logged in | PASS
Sign Up Link | Click | Navigates to Sign Up page | PASS
Log In Link | Display | Only available if the user is not logged in | PASS
Log In Link | Click | Navigates to Log In page | PASS
Log Out Link | Display | Only available if the user is logged in | PASS
Log Out Link | Click | Navigates to Log Out page | PASS
My Favourites Link | Display | Only available if the user is logged in | PASS
My Favourites Link | Click| Navigates to My Favourites page | PASS
My Recipes Link | Display | Only available if the user is logged in | PASS
My Recipes Link | Click| Navigates to My Recipes page | PASS
Post a Recipe Link | Display | Only available if the user is logged in | PASS
Post a Recipe Link | Click| Navigates to Post a Recipe page to | PASS
All Links | Hover | Colour changes to green with hover effect | PASS
All Links | Display | Active page is shown in green | PASS

### Footer
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Position | Display | Footer always stays at the bottom of the screen even when the content does not occupy the full view height | PASS
Facebook Link | Click | Opens Facebook in a new tab | PASS
Twitter Link | Click | Opens Twitter in a new tab | PASS
Instagram Link | Click | Opens Instagram in a new tab | PASS
GitHub Link | Click | Opens GitHub in a new tab | PASS
LinkedIn Link | Click | Opens LinkedIn in a new tab | PASS
All Links | Hover | Colour changes to green with hover effect | PASS

### Signup Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Username Field | Leave Empty | Form does not submit | PASS
Username Field | Leave Empty | Error message is displayed | PASS
Username Field | Duplicate Username | Form does not submit | PASS
Username Field | Duplicate Username | Error message is displayed | PASS
Email Field | Leave Empty | Form submits without email address as this is an optional field | PASS
Email Field | Enter Invalid Format | Form does not submit | PASS
Email Field | Enter Invalid Format | Error message is displayed | PASS
Email Field | Duplicate Email Address | Form does not submit | PASS
Email Field | Duplicate Email Address | Error message is displayed | PASS
Password Field | Leave Empty | Form does not submit | PASS
Password Field | Leave Empty | Error message is displayed | PASS
Password Field | Passwords Not Matched | Form does not submit | PASS
Password Field | Passwords Not Matched | Error message is displayed | PASS
Log In Link | Click | Navigates to Log In page | PASS
Sign Up Link | Click | Once all the required fields are correctly filled in, creates an account | PASS
Sign Up Link | Click | Once an account is created, logs in the user | PASS
Sign Up Link | Click | Once the user is logged in, navigates to Home page | PASS
Alert | Submit | Success message is displayed confirming the user has logged in as [username] | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS

### Login Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Username Field | Leave Empty | Form does not submit | PASS
Username Field | Leave Empty | Error message is displayed | PASS
Password Field | Leave Empty | Form does not submit | PASS
Password Field | Leave Empty | Error message is displayed | PASS
Login Fields | Incorrect Details | Form does not submit | PASS
Login Fields | Incorrect Details | Error message is displayed | PASS
Sign Up Link | Click | Navigates to Sign Up page | PASS
Log In Link | Click | Once the required fields are correctly filled in, logs in the user | PASS
Log In Link | Click | Once the user is logged in, navigates to Home page | PASS
Alert | Submit | Success message is displayed confirming the user has logged in as [username] | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS

### Logout Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Logout Link | Click | Logs out the user | PASS
Logout Link | Click | Once the user is logged out, navigates to Home page | PASS
Browse Recipes Link | Click | Navigates to Browse Recipes page | PASS
Alert | Submit | Success message is displayed confirming that the user has logged out | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS

### Home Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Sign Up Message | Display | Correct message is displayed if the user is not logged in | PASS
Sign Up Link | Display | Only available if the user is not logged in | PASS
Sign Up Link | Click | Navigates to Sign Up page | PASS
Post a Recipe Message | Display | Correct message is displayed if the user is logged in | PASS
Post a Recipe Link | Display | Only available if the user is logged in | PASS
Post a Recipe Link | Click| Navigates to Post a Recipe page to | PASS

### Browse Recipes Page
#### Recipe Filters
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Filter Dropdown Menu | Display | Dropdown menu is displayed correctly for each filter | PASS
Filter Functionality | Click | Filters recipes based on the criteria selected | PASS
Filter Functionality | Click | Clears filters when no criteria is selected | PASS
Filter Functionality | Display | When there are no recipes to display, Browse Recipes button and correct message are displayed | PASS
Browse Recipes Link | Click | Navigates back to Browse Recipes page without any filter criteria applied | PASS
Pagination | Display | When there are more than 12 recipes to display, the filtered list of recipes is paginated correctly and maintains the filter criteria when navigating through the pages (previous, next, first and last pages) | PASS
Pagination | Display | When there are less than 12 recipes to display, pagination is not displayed | PASS

#### Recipe Cards
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Recipe Card | Display | Recipes published are displayed in descending order | PASS
Recipe Card | Display | Draft recipes are not displayed | PASS
Recipe Card | Click | Stretched link is applied correctly and clicking anywhere on a card navigtes to the correct Recipe Details page | PASS
Recipe Card | Hover | Box shadow is applied with hover effect | PASS
Recipe Card Height | Display | Recipe cards are displayed in the same height for each row regardless of the height of card body content (when the height of a card is higher, the rest of the cards in the same row are stretched to the same height) | PASS  
Recipe Card Width | Display | Recipe cards are displayed in the same width for each column and column width is the same for all columns displayed | PASS
Recipe Image | Display | When a recipe image is uploaded, the image is displayed correctly from Cloudinary | PASS
Recipe Image | Display | When a recipe image is not uploaded, the placeholder image is displayed correctly from Cloudinary | PASS
Image Size | Display | Images are displayed in the same height and width regardless of the size or aspect ratio of the images uploaded | PASS
Recipe Title | Display | First letter is always capitalised regardless of whether the title entered is capitalised | PASS
Number of Likes | Display | The number of likes is displayed correcty with a grey love heart and the nubmer indicating the number of likes | PASS
Recipe Description | Display | First letter is always capitalised regardless of whether the description entered is capitalised | PASS
Recipe Description | Display | Description is truncated to 70 characters for display the recipe cards | PASS  
Pagination | Display | When there are more than 12 recipes to display, pagination is added and functions correctly | PASS
Pagination | Display | When there are less than 12 recipes to display, pagination is not displayed | PASS

### Recipe Details Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Recipe Image | Display | When a recipe image is uploaded, the image is displayed correctly from Cloudinary | PASS
Recipe Image | Display | When a recipe image is not uploaded, the placeholder image is displayed correctly from Cloudinary | PASS
Image Size | Display | For screen sizes with a minimum width of 992px, the image height is set to occupy the maximum height of recipe summary container next to the image | PASS
Recipe Title | Display | First letter is always capitalised regardless of whether the title entered is capitalised | PASS
Edit/Delete Recipe Button | Display | Edit/Delete button is available if the user is logged in and is the author of the recipe | PASS
Edit Recipe Button | Click | Opens Update Recipe page with the original details populated from the database | PASS
Edit Recipe Cancel Button | Click | Navigates back to Recipe Detail page | PASS
Delete Recipe Button | Click | Displays the modal asking the user to confirm deletion | PASS
Like/Unlike Button | Display | Like/Unlike button is available if the user is logged in and the recipe is published | PASS
Like/Unlike Button | Display | Like/Unlike button is greyed out and not clickable if the user is not logged in or the recipe is not yet published | PASS
Like/Unlike Button | Click | Toggles between Like (a love heart & plus icon) and Unlike (a love heart icon) if the user is logged in and the recipe is published | PASS
Number of Likes | Display | The number of likes is dispalyed and increases or decreases correctly when the reipe is liked or unliked | PASS
Recipe Description | Display | First letter is always capitalised regardless of whether the description entered is capitalised | PASS
Ingredients | Display | Details are displayed correctly from Summernote field in the default font and font size | PASS
Method | Display | Details are displayed correctly from Summernote field in the default font and font size | PASS
Comments | Display | If there are no comments, correct message is displayed | PASS
Comments | Display | Displays comments, authors and dates in ascending order if there are comments | PASS
Post Comment | Display | If the user is not logged in, correct message is displayed | PASS
Post Comment | Display | If the recipe is not published, correct message is displayed | PASS
Post Comment | Display | Comment form is only available if the user is logged in and the recipe is published | PASS
Post Comment | Display | First letter is always capitalised regardless of whether the comment entered is capitalised | PASS
Post Comment | Leave Empty | Form does not submit | PASS
Post Comment | Submit | Form submits and comment is added in ascending order | PASS
Alert | Submit | Success message is displayed confirming the comment has been added successfully | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS
Edit/Delete Comment Dropdown Menu | Display | Edit/Delete button is available if the user is logged in and is the author of the comment | PASS
Edit Comment Button | Click | Opens Update Comment page with the original details populated from the database | PASS
Delete Comment Button | Click | Displays the modal asking the user to confirm deletion | PASS

### My Favourites Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Defensive Measure | Not Logged-in and Try to Acess the Page by Changing URL | Navigates the user to Log In page | PASS
Recipe Card | Display | Recipes liked by the user are displayed in descending order | PASS
Recipe Card | Click | Stretched link is applied correctly and clicking anywhere on a card navigtes to the correct Recipe Details page | PASS
Recipe Card | Hover | Box shadow is applied with hover effect | PASS
Recipe Card Height | Display | Recipe cards are displayed in the same height for each row regardless of the height of card body (when the height of a card is higher, the rest of the cards in the same row are stretched to the same height) | PASS  
Recipe Card Width | Display | Recipe cards are displayed in the same width for each column and column width is the same for all columns displayed | PASS
Recipe Card | Display | When there are no recipes to display, Browse Recipes button and correct message are displayed | PASS
Browse Recipes Link | Click | Navigates to Browse Recipes page | PASS
Recipe Image | Display | When a recipe image is uploaded, the image is displayed correctly from Cloudinary | PASS
Recipe Image | Display | When a recipe image is not uploaded, the placeholder image is displayed correctly from Cloudinary | PASS
Image Size | Display | Images are displayed in the same height and width regardless of the size or aspect ratio of the images uploaded | PASS
Recipe Title | Display | First letter is always capitalised regardless of whether the title entered is capitalised | PASS
Number of Likes | Display | The number of likes is displayed correcty with a grey love heart and the nubmer indicating the number of likes | PASS
Recipe Description | Display | First letter is always capitalised regardless of whether the description entered is capitalised | PASS
Recipe Description | Display | Description is truncated to 70 characters for display on a card | PASS  
Pagination | Display | When there are more than 12 recipes to display, pagination is added and functions correctly | PASS
Pagination | Display | When there are less than 12 recipes to display, pagination is not displayed | PASS

### My Recipes Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Defensive Measure | Not Logged-in and Try to Acess the Page by Changing URL | Navigates the user to Log In page | PASS
Recipe Card | Display | Recipes posted by the user are displayed in descending order | PASS
Recipe Card | Click | Stretched link is applied correctly and clicking anywhere on a card navigtes to the correct Recipe Details page | PASS
Recipe Card | Hover | Box shadow is applied with hover effect | PASS
Recipe Card Height | Display | Recipe cards are displayed in the same height for each row regardless of the height of card body content (when the height of a card is higher, the rest of the cards in the same row are stretched to the same height) | PASS  
Recipe Card Width | Display | Recipe cards are displayed in the same width for each column and column width is the same for all columns displayed | PASS
Recipe Card | Display | [Draft] in red font is added to the recipe title if the recipe is not published | PASS
Recipe Card | Display | When there are no recipes to display, Post a Recipe button, Browse Recipes button and correct messages are displayed | PASS
Post a Recipe Link | Click | Navigates to Post Recipe page | PASS
Browse Recipes Link | Click | Navigates to Browse Recipes page | PASS
Recipe Image | Display | When a recipe image is uploaded, the image is displayed correctly from Cloudinary | PASS
Recipe Image | Display | When a recipe image is not uploaded, the placeholder image is displayed correctly from Cloudinary | PASS
Image Size | Display | Images are displayed in the same height and width regardless of the size or aspect ratio of the images uploaded | PASS
Recipe Title | Display | First letter is always capitalised regardless of whether the title entered is capitalised | PASS
Number of Likes | Display | The number of likes is displayed correcty with a grey love heart and the nubmer indicating the number of likes | PASS
Recipe Description | Display | First letter is always capitalised regardless of whether the description entered is capitalised | PASS
Recipe Description | Display | Description is truncated to 70 characters for display on a card | PASS  
Pagination | Display | When there are more than 12 recipes to display, pagination is added and functions correctly | PASS
Pagination | Display | When there are less than 12 recipes to display, pagination is not displayed | PASS

### Post Recipe Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Defensive Measure | Not Logged-in and Try to Acess the Page by Changing URL | Navigates the user to Log In page | PASS
Title | Leave Empty | Form does not submit | PASS
Title | Leave Empty | Error message is displayed | PASS
Title | Enter an Empty String | Form does not submit | PASS
Title | Enter an Empty String | Error message is displayed | PASS
Description | Leave Empty | Form does not submit | PASS
Description | Leave Empty | Error message is displayed | PASS
Description | Enter an Empty String | Form does not submit | PASS
Description | Enter an Empty String | Error message is displayed | PASS
Meal Type | Leave Empty | Form does not submit | PASS
Meal Type | Leave Empty | Error message is displayed | PASS
Main Ingredient | Leave Empty | Form does not submit | PASS
Main Ingredient | Leave Empty | Error message is displayed | PASS
Diet Type | Not Selected | Form submits as this is not a required field | PASS
Difficulty | Leave Empty | Form does not submit | PASS
Difficulty | Leave Empty | Error message is displayed | PASS
Preparation Time | Leave Empty | Form does not submit | PASS
Preparation Time | Leave Empty | Error message is displayed | PASS
Preparation Time | Enter Anything Other Than a Positive Integer | Form does not submit | PASS
Preparation Time | Enter Anything Other Than a Positive Integer | Error message is displayed | PASS
Cooking Time | Leave Empty | Form does not submit | PASS
Cooking Time | Leave Empty | Error message is displayed | PASS
Cooking Time | Enter Anything Other Than a Positive Integer | Form does not submit | PASS
Cooking Time | Enter Anything Other Than a Positive Integer | Error message is displayed | PASS
Serves | Leave Empty | Form does not submit | PASS
Serves | Leave Empty | Error message is displayed | PASS
Serves | Enter Anything Other Than a Positive Integer | Form does not submit | PASS
Serves | Enter Anything Other Than a Positive Integer | Error message is displayed | PASS
Ingredients | Leave Empty | Form does not submit | PASS
Ingredients | Leave Empty | Error message is displayed | PASS
Ingredients | Enter an Empty String | Form does not submit | PASS
Ingredients | Enter an Empty String | Error message is displayed | PASS
Method | Leave Empty | Form does not submit | PASS
Method | Leave Empty | Error message is displayed | PASS
Method | Enter an Empty String | Form does not submit | PASS
Method | Enter an Empty String | Error message is displayed | PASS
Image | Not Uploaded | Form submits as this is not a required field | PASS
Status | Save as Draft | Once all the required fields are filled in correctly, saves the recipe | PASS
Status | Save as Draft | Once the recipe is saved as Draft, the recipe is displayed in My Recipe page | PASS
Status | Publish Now | Once all the required fields are filled in correctly, saves the recipe | PASS
Status | Publish Now  | Once the recipe is saved as Draft, the recipe is displayed in Browse Recipes page | PASS
Post Recipe | Submit | Displays the Recipe Details page which has been generated | PASS
Alert | Submit | Success message is displayed confirming [recipe title] has been added successfully | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS
Post Recipe Cancel Button | Click | Navigates back to Browse Recipes page | PASS

### Update Recipe Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Defensive Measure | Not Logged-in and Try to Access Another User's Recipe by Changing URL | Navigates the user to Log In page | PASS
Defensive Measure | Logged-in and Try to Access Another User's Recipe by Changing URL | 403 error page is displayed | PASS
Update Recipe | Display | Update Recipe form contains the original details from database | PASS
Title | Leave Empty | Form does not submit | PASS
Title | Leave Empty | Error message is displayed | PASS
Title | Enter an Empty String | Form does not submit | PASS
Title | Enter an Empty String | Error message is displayed | PASS
Description | Leave Empty | Form does not submit | PASS
Description | Leave Empty | Error message is displayed | PASS
Description | Enter an Empty String | Form does not submit | PASS
Description | Enter an Empty String | Error message is displayed | PASS
Meal Type | Leave Empty | Form does not submit | PASS
Meal Type | Leave Empty | Error message is displayed | PASS
Main Ingredient | Leave Empty | Form does not submit | PASS
Main Ingredient | Leave Empty | Error message is displayed | PASS
Diet Type | Not Selected | Form submits as this is not a required field | PASS
Difficulty | Leave Empty | Form does not submit | PASS
Difficulty | Leave Empty | Error message is displayed | PASS
Preparation Time | Leave Empty | Form does not submit | PASS
Preparation Time | Leave Empty | Error message is displayed | PASS
Preparation Time | Enter Anything Other Than a Positive Integer | Form does not submit | PASS
Preparation Time | Enter Anything Other Than a Positive Integer | Error message is displayed | PASS
Cooking Time | Leave Empty | Form does not submit | PASS
Cooking Time | Leave Empty | Error message is displayed | PASS
Cooking Time | Enter Anything Other Than a Positive Integer | Form does not submit | PASS
Cooking Time | Enter Anything Other Than a Positive Integer | Error message is displayed | PASS
Serves | Leave Empty | Form does not submit | PASS
Serves | Leave Empty | Error message is displayed | PASS
Serves | Enter Anything Other Than a Positive Integer | Form does not submit | PASS
Serves | Enter Anything Other Than a Positive Integer | Error message is displayed | PASS
Ingredients | Leave Empty | Form does not submit | PASS
Ingredients | Leave Empty | Error message is displayed | PASS
Ingredients | Enter an Empty String | Form does not submit | PASS
Ingredients | Enter an Empty String | Error message is displayed | PASS
Method | Leave Empty | Form does not submit | PASS
Method | Leave Empty | Error message is displayed | PASS
Method | Enter an Empty String | Form does not submit | PASS
Method | Enter an Empty String | Error message is displayed | PASS
Image | Not Uploaded | Form submits as this is not a required field | PASS
Status | Save as Draft | Once all the required fields are filled in correctly, saves the recipe | PASS
Status | Save as Draft | Once the recipe is saved as Draft, the recipe is displayed in My Recipe page | PASS
Status | Publish Now | Once all the required fields are filled in correctly, saves the recipe | PASS
Status | Publish Now  | Once the recipe is saved as Draft, the recipe is displayed in Browse Recipes page | PASS
Update Recipe | Submit | Displays the Recipe Details page which has been updated | PASS
Alert | Submit | Success message is displayed confirming the [recipe title] has been updated successfully | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS
Update Recipe Cancel Button | Navigates back to Recipe Detail page | PASS

### Delete Recipe Modal
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Delete Recipe | Submit | Once the user confirms deletion in the modal, the recipe is deleted | PASS
Alert | Submit | Success message is displayed confirming that the recipe has been deleted | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS
Delete Recipe Cancel Button | Click | Modal is closed | PASS
Close Modal | Click Outside Menu | Modal is closed | PASS

### Update Comment Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Defensive Measure | Not Logged-in and Try to Access Another User's Comment by Changing URL | Navigates the user to Log In page | PASS
Defensive Measure | Logged-in and Try to Access Another User's Comment by Changing URL | 403 error page is displayed | PASS
Update Comment| Display | Update Comment form contains the original details from database | PASS
Comment Field | Leave Empty | Form does not submit | PASS
Comment Field | Leave Empty | Error message is displayed | PASS
Update Comment | Click | Comment is updated | PASS
Alert | Submit | Success message is displayed confirming the comment has been updated successfully | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS
Update Comment Cancel Button | Click | Navigates back to Recipe Detail page | PASS

### Delete Comment Modal
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Delete Comment| Submit | Once the user confirms deletion in the modal, the comment is deleted | PASS
Alert | Submit | Success message is displayed confirming that the comment has been deleted | PASS
Alert | Submit | Success message is removed after 3 seconds | PASS
Delete Comment Cancel Button | Click | Modal is closed | PASS
Close Modal | Click Outside Menu | Modal is closed | PASS 

### 403 Error Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Custom 403 Error Page  | Change URL to Acess Another User's Recipe | Custom 403 error message is displayed | PASS
Custom 403 Error Page | Change URL to Acess Another User's Comment | Custom 403 error message is displayed | PASS
Home Link | Click | Navigates to Home page | PASS
Browse Recipes Link | Click | Navigates to Home page | PASS

### 404 Error Page
Feature | Action | Expected Result | PASS/FAIL
---|---|---|---
Custom 404 Error Page | Enter URL that does not exist | Custom 404 error message is displayed | PASS
Home Link | Click | Navigates to Home page | PASS
Browse Recipes Link | Click | Navigates to Home page | PASS

## Bugs
### Resolved Bugs
#### Pagination for a Filtered List of Recipes
**Issue:**  
When [Django filters](https://django-filter.readthedocs.io/en/stable/) were added to Browse Recipes page, the standard [Django pagination](https://docs.djangoproject.com/en/3.2/topics/pagination/) no longer worked.
With the standard Django pagination, the filter criteria were no longer applied when navigating to another page and showed recipes that did not fall under the selected criteria.

**Fix:**  
While searching for a solution, I learnt that this is a common issue with Django filters. 
Having reviewed many possible solutions to the issue, I decided to implement the soluction found in [Django Filter and Pagination](https://www.youtube.com/watch?v=dkJ3uqkdCcY) tutorial.
This solution uses [QueryString Template Tags](https://simpleisbetterthancomplex.com/snippet/2016/08/22/dealing-with-querystring-parameters.html) and works with Django filters.
RecipeList view code and pagination code for Browse Recipe page were updated to incorporate this solution for the Django filters. 

#### Positioning of Remember Me Box
**Issue:**  
The "Remember Me" box in Log In page was initially horizontally centralised with the rest of the contents.
During the manual testing on iPhone 11, it was noted that the box was positioned to the left, although this was not the case in Chrome Developer.
It appered the issue resulted from how Apple Safari rendered the codes.   
<img src="docs/images/validation/remember-me-box-before-fix.jpeg" width=250>

**Fix:**  
CSS codes were added to target the "Remember Me" box and moved it to the right of the "Remember Me" text.
The text and the box are now centralised together. 
I felt that this was a more appropriate position for the box.  
<img src="docs/images/validation/remember-me-box-after-fix.jpeg" width=250>

### Unresolved Bugs

#### Integrity Error for Slug Key Value Violation
**Issue:**  
During the manual testing, when a recipe titled "Bob" was submitted in the deployed site, server error 500 occured.
The error in the development environment showed that it was caused by the duplicate key value as there was already a slug value "Bob" existed in the database and the slug key value must be unique.  
<img src="docs/images/validation/server-error-500.png" width=700>

In the admin panel, it was verified that there was indeed a recipe titled "Bob" saved as a draft by a user.
When the draft recipe was deleted from the database, the error no longer occurred.

**Result:**  
Post Recipe form prevents a recipe entry with the same title as an existing recipe and raises an error. 
<img src="docs/images/validation/no-server-error.png" width=500>
Numerous attempts were made to recreate the error to investigate the issue further, however, I was never able to recreate the error.
Since the error could not be recreated, this bug was not addressed.

There are no other known bugs.
