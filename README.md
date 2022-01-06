# Restaurant Booking App

A booking app built using Django for a fictitious restaurant, built to demonstrate a full stack product with CRUD functionality. 

# Table of Contents <a name='contents'></a>

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

## User Experience (UX) <a name='userexperience'></a>

[Return to Table of Contents](#contents)

## Design <a name='design'></a>

- **Colour Scheme**

- **Typography**

- **Imagery**

- **Layout**

[Return to Table of Contents](#contents)

## Development <a name='development'></a>

[Return to Table of Contents](#contents)

## Existing Features <a name='existingfeatures'></a>

[Return to Table of Contents](#contents)

## Features Left to Implement <a name ='toimplement'></a>

[Return to Table of Contents](#contents)

## Testing <a name ='testing'></a>  

- **Validator Testing**

    - HTML
        - No errors were found when passing through the [W3C Validator tool](https://validator.w3.org/#validate_by_uri)

    - CSS
        - No errors were found when passing through the [W3C Validator tool](https://jigsaw.w3.org/css-validator/)

    - JAVASCRIPT
        - - No errors were found when passing through [JSHint](https://jshint.com/)

    - Python
        - No errors were found when passing through the [PEP8 Validator tool](http://pep8online.com/)

- **Lighthouse**


[Return to Table of Contents](#contents)

## Unfixed Bugs <a name ='bugs'></a>


[Return to Table of Contents](#contents)

## Deployment <a name ='deployment'></a>

- The site is deployed via [Heroku](https://heroku.com/). The steps to deploy are as follows:

    *Ensure the requirements for the project are added to the requirements.txt file prior to deployment*

    1: From the dashboard, select New and then Create new app.
    
    2: Enter an individual app name into the text box, select a region from the dropdown and then press Create app.
    
    3: A Heroku app has now been created and the Deploy tab is opened.
    
    4: Select the Settings tab.
    
    5: If required, click on the Reveal Config Vars button and add.
    
    6: In the Buildpacks section of the settings tab, click on Add Buildpack, select Python and then save changes.
    
    7: Click on Add Buildpack again, select node.js and then save changes.

    *When they are on the dashboard, ensure that python is above node.js on the list*
    
    8: Open the Deploy tab.
    
    9: In the deployment method section, select GitHub and confirm the connection.
    
    10: Enter the repo-name into the text box. When the correct repo appears, click Connect.
    
    11: If desired, in the Automatic deploys section, click Enable Automatic Deploys.

    *This then updates the deployment every time GitHub code is pushed.*
    
    12: To complete the process click on the Deploy Brach button in the Manual deploy section. 
        
    *This will take a few seconds to complete while Heroku builds the app.*
    
    13: A message will appear informing you that the app was successfully deployed and a View button will bring you to the live site.

The live link can be found here - [restaurant-booking-app]()

[Return to Table of Contents](#contents)

## Technologies Used <a name ='tech'></a>

- **Languages Used**

    * HTML
    * CSS
    * JAVASCRIPT
    * PYTHON
    * MARKDOWN

- **Frameworks**

    * **[Django 3.2](https://www.djangoproject.com/download/).**
        * Python based web framework, used to build the application.

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

- **Libraries**

    * **[dj_database_url](https://pypi.org/project/dj-database-url/).**
        * A PostgreSQL supporting library. Allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
    
    * **[pyscopg2](https://www.psycopg.org/docs/).**
        * PostgreSQL database adapter for the Python programming language.
    
    * **[dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/).**
        * a Django package that facilitates integration with Cloudinary.
    
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

- **Media**

[Return to Table of Contents](#contents)
