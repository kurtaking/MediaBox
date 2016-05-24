## MediaBox
###### A media management system written on the Django Framework

####Purpose:
Allow users to create an account and keep track of all their favorite media.<br>
(More information to come)

Let our application be a central media storage location for all of your content (movies, vinyls, books, video games, and more).

####Intentions:

The idea behind the application is to allow the contributors to get comfortable with a new environment and multiple programming tools, such as:<br>
1. Django Web Framework<br>
2. Python<br>
3. HTML/CSS/Javascript (custom and open souce)<br>
4. Databases (creating, adding, updating, saving, deleting, etc)<br>
5. Building a fully responsive mobile web application<br>
6. pyCharm IDE<br>
7. Git (with multiple contributors)<br>
8. Open source APIs<br>
9. Session tracking (multiple users)<br>
10. Deploying an application on a AWS server and making it live<br>
11. Creating an admin interface with statistics about traffic across the site<br>

We want to capture as many attributes as possible about your media to run queries and present your content back to you in the cleanest way possible.
By collecting user data, we will be able to create custom statistics and display it back to the user.

This is our first crack at it. Hope you enjoy.

####Incomplete Features:
1. Session Tracking<br>
2. Application Templates (html views for each page)<br>
3. Responsive design<br>
4. User Dashboard<br>
5. Database tables for user's content<br>
6. Login/Registration page<br>
7. Models for the database<br>
8. Forms for adding entries to database<br>
9. Home Page<br>
10. Navigation Bar<br>
11. (more coming soon)<br>

####Completed Features:
1. Project set-up<br>
2. Git Repository<br>

####Instructions to set up environment
1. Make sure you have virtualenv, pip, and python installed
2. Create a new virtual environment via <code>virtualenv venv</code>
3. Activate virtual environment with <code>source venv/bin/activate</code>
4. Once the virtual environment is activated, you may need to install some python packages. Run:<br>
  <code>pip install django djangorestframework mysqlclient</code>
5. Run <code>python3 manage.py migrate</code> and ensure no errors come up.
6. To run locally, type <code>python3 manage.py runserver</code> and navigate to the index page
