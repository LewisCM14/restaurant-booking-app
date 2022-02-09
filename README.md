# Restaurant Booking App

A booking app built using Django for a fictitious restaurant, built to demonstrate a full stack product with CRUD functionality. 

## Table of Contents <a name='contents'></a>

* [User Experience (UX)](#userexperience)
* [Design](#design)
* [Development](#development)
* [Existing Features](#existingfeatures)
* [Features Left to Implement](#toimplement)
* [Testing](#testing)
* [Unfixed Bugs](#bugs)
* [Deployment](#deployment)
* [Technologies Used](#tech)
* [Credits](#credits)

### User Experience (UX) <a name='userexperience'></a>

[Return to Table of Contents](#contents)

### Design <a name='design'></a>

- **Colour Scheme**

- **Typography**

- **Imagery**

- **Layout**

[Return to Table of Contents](#contents)

### Development <a name='development'></a>

[Return to Table of Contents](#contents)

### Existing Features <a name='existingfeatures'></a>

[Return to Table of Contents](#contents)

### Future Features <a name ='toimplement'></a>

[Return to Table of Contents](#contents)

### Testing <a name ='testing'></a>  

- **Validator Testing**

    - HTML
        - No errors were found when passing through the [W3C Validator tool](https://validator.w3.org/#validate_by_uri)

    - CSS
        - No errors were found when passing through the [W3C Validator tool](https://jigsaw.w3.org/css-validator/)

    - JAVASCRIPT
        - No errors were found when passing through [JSHint](https://jshint.com/)

    - Python
        - No errors were found when passing through the [PEP8 Validator tool](http://pep8online.com/)

- **Lighthouse**


[Return to Table of Contents](#contents)

### Unfixed Bugs <a name ='bugs'></a>


[Return to Table of Contents](#contents)

### Deployment <a name ='deployment'></a>

- The site is deployed via [Heroku](https://heroku.com/). The steps to deploy are as follows:

    *Ensure all requirements for the project are added to the requirements.txt file prior to deployment*

    * STAGE ONE - Create a New App in Heroku

        1: From the dashboard on Heroku, select New and then Create new app.
        
        2: Enter an individual app name into the text box, select a relevant region from the dropdown and then press Create app.
        
        3: A Heroku app has now been created.
    
    ---
    
    * STAGE TWO - Add a Database

        1: Navigate to the resources tab for the app that has just been created.

        2: In the Add-Ons section, search for the Heroku Postgres add on and submit an order form.
        
        3: Select the Settings tab for the app.

        4: Reveal Config Vars and copy the DATABASE_URL string provided.

        5: Create a env.py file within the project and use the copied string to create a DATABASE_URL environment variable.

    ---
    
    * STAGE THREE - Create a SECRET_KEY

        1: Within the env.py file, create a SECRET_KEY environment variable.

        2: On the settings tab of the Heroku app, reveal config vars and add the created SECRET_KEY.

    ---
    
    * STAGE FOUR - Update the settings.py file

        1: Import dj_database_url and env.py into the settings.py file within the project.

        2: Update the default SECRET_KEY variable provided by Django to the SECRET_KEY environment variable.

        3: Update the DATABASES dictionary to use the DATABASE_URL environment variable, the dj_database_url library is utilised here.

        4: Preform a migration.

        *The Heroku database is now being used as the backend, within the resources tab of the app, the Heroku Postgres link will bring up a window demonstrating this.*

    ---

    * STAGE FIVE - Connect app to Cloudinary

        1: On the Cloudinary website, copy the API environment variable string.

        2: Within the projects env.py file create a CLOUDINARY_URL environment variable using this copied string.

        3: Within the Heroku app, on the settings tab, update the config vars to contain this variable.

        *For initial deployment, a variable called DISABLE_COLLECTSTATIC is also created within the config vars at this point with a value of 1, this is simply to get the skeleton project deployed for testing purposes and removed when deploying the full project*

        4: Within the settings.py file on the project, under INSTALLED_APPS, 'cloudinary_storage' and 'cloudinary' must be added.

        5: Django must then be told to use Cloudinary to store media and static files, this is done by adding the below variables to the relevant section of the settings.py file:
            
            STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
            STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
            STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
            MEDIA_URL = '/media/'
            DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
        
        *The app is now linked to Cloudinary*
    
    ---
     
    * STAGE SIX - Tell Django where the templates are stored

        1: Under the BASE_DIR on settings.py, add in the below templates directory. 
        
            TEMPLATES_DIR =  os.path.join(BASE_DIR, 'templates')
        
        2: Then within the TEMPLATES setting, update the DIRS key to point towards this variable.
    
    ---
    
    * STAGE SEVEN - Update ALLOWED_HOSTS

        1: Within settings.py on the project update the ALLOWED_HOSTS variable to be the name of your Heroku app with ".herokuapp.com" appended to the end.

        *Add localhost too, so that the project can also be ran locally. This is also a good point to add the Media, Static and Template directories, these folders should be added at the top level.*
    
    ---
    
    * STAGE EIGHT - Create a Procfile

        1: Create a Procfile at the top level of the directory.

        2: Within this file, declare the below command.

            * web: gunicorn restobook.wsgi
        
        *Add, commit and push to the repository at this point*
    
    ---
    
    * STAGE NINE - Connect the GitHub repository to the Heroku App

        1: Within the Deploy tab on the Heroku app, choose GitHub as the deployment method.

        2: Search for the correct repository and connect.

        3: At the bottom of the deployment section there is an option to chose which branch to deploy. Chose the main branch and allow the build log to complete.

        4: Once complete, chose to allow automatic deployment from here onwards.

        *The app has now been deployed successfully.*

    ---

The live link can be found here - [restaurant-booking-app](https://restaurant-booking-app-lewiscm.herokuapp.com/)

[Return to Table of Contents](#contents)

## Technologies Used <a name ='tech'></a>

- **Languages Used**

    * HTML
    * CSS
    * JAVASCRIPT
    * PYTHON
    * MARKDOWN

- **Frameworks & Toolkits**

    * **[Django 3.2](https://www.djangoproject.com/download/).**
        * Python based web framework, used to build the application.
    
    * **[Bootstrap](https://getbootstrap.com/).**
        * A front-end open source toolkit, used across the application.
    
    * **[Font Awesome](https://fontawesome.com/).**
        * Icon set and toolkit used across the application.

- **DBMS**
    
    * **[PostgreSQL](https://www.postgresql.org/).**
        * The relational database management system used.

- **Cloud Services**

    * **[Heroku](https://id.heroku.com/login).**
        * Used to deploy my project.

    * **[Cloudinary](https://cloudinary.com/).**
        * A cloud-based image and video management service. Used due to Heroku using an ephemeral file system. 

- **Server**

    * **[Gunicorn](https://gunicorn.org/).**
        * The server used to run Django on Heroku.

- **Version Control**
    
    * **Git.**
        * Git was used for version control by utilizing the GitPod terminal to commit to Git and Push to GitHub.

    * **[GitHub](https://github.com/).**
        * GitHub is used to store the projects code after being pushed from Git.
    
    * **[Gitpod](https://www.gitpod.io/docs/).**
        * The IDE used to build the project.

- **Libraries, Packages and Applications**

    * **[dj_database_url](https://pypi.org/project/dj-database-url/).**
        * A PostgreSQL supporting library. Allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
    
    * **[pyscopg2](https://www.psycopg.org/docs/).**
        * PostgreSQL database adapter for the Python programming language.
    
    * **[dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/).**
        * a Django package that facilitates integration with Cloudinary.
    
    * **[allauth](https://django-allauth.readthedocs.io/en/latest/installation.html).**
        * Used for creation and maintenance of user accounts.
    
    * **[crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html).**
        * Used for rendering the booking form in the browser.
    
    * **[autoslug](https://pypi.org/project/django-autoslug/).**
        * Used on the Booking model to generate the slug field.
    
    * **[coverage](https://coverage.readthedocs.io/en/6.3/).**
        * Used to access the coverage of my automated tests for the python code i've wrote.
    
- **Programs**

    * **Slack.**
        * Specifically the peer-code_review channel on Code Institutes Slack workspace. Used to increase the scope of my testing.
    
    * **Balsamiq.** 
        * Used to create the wire frames during the development process.
       
[Return to Table of Contents](#contents)

## Credits <a name = 'credits'></a> 

* A special thank you to my mentor Rohit Sharma. 

* Thanks to the Code Institute tutor support team, who helped me develop my understanding throughout this project.

* Finally thanks to my peers on Slack who responded to my questions.  

- **Content**

    * I used this YouTube [tutorial](https://www.youtube.com/watch?v=AuNjaMLwuug/) to help me wire up my views.

    * The footer is developed from a template on [MDBootstrap](https://mdbootstrap.com/docs/standard/navigation/footer/).

    * To adjust the base allauth sign up form i used this [post](https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/) to write my custom class and this [post](https://stackoverflow.com/questions/55786710/using-multiple-login-fields-email-or-phone-number-in-django-all-auth) to further develop it. I then used this [post](https://stackoverflow.com/questions/23956288/django-all-auth-email-required) on stack overflow to adjust my allauth configuration.

    * I used this [tutorial](https://www.youtube.com/watch?v=4sosXZsdy-s) to further my understanding of Bootstrap5, particularly when developing my Special Requirements modal. 

    * I used this [post](https://stackoverflow.com/questions/4101258/how-do-i-add-a-placeholder-on-a-charfield-in-django) on StackOverflow to help me add placeholder text to my BookingForm.

    * I used this [post](https://philipwalton.github.io/solved-by-flexbox/demos/sticky-footer/) by [Philip Walton](https://philipwalton.com/) to make my footer stick to to bottom of the browser view.

    * I used this [post](https://www.culturefoundry.com/cultivate/technology/bottom-align-an-element-with-flexbox/) by Josh Coast to refresh my knowledge on flex-box, for then styling my hero image on the index page.

    * I used this [post](https://www.section.io/engineering-education/uploading-images-to-cloudinary-from-django-application/) by [Shuaib Oseni](https://www.section.io/engineering-education/authors/shuaib-oseni/) in order to setup the methods of storing the images used for my project on cloudinary.

- **Media**

    * The hero image used on the index page is a free to use stock photo found [here](https://unsplash.com/photos/-YHSwy6uqvk) on [unsplash](https://unsplash.com/). The photo was taken by [Lily Banse](https://unsplash.com/@lvnatikk).

[Return to Table of Contents](#contents)
