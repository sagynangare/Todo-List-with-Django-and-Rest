# Django-and React-todo-app
This application allows users to add Add/Update/Delete Todo Tasks

# TechStack Used :
>Backend : Python==3.12 , Django==5.0.2  , Django REST Framework ,Postgresql
Frontend : HTML5 , Bootstrap , Javascript

# Note: This project makes use of Django's Class Based Views

The Following Problem Statement is being Covered :
Create a TO-DO list app
Tech Stack to be used: Python, Django (Use latest versions)
Requirements:
1. The app should have the following fields:
   Title
   Description
   Date & time of the To-do task
   Status (In progress, completed, pending)
   Task Created & Modified at
   is deleted

2. Login & Authentication are not required to view the todo list but are handled authentication also using DjangoRest Framework

3. The app should handle all the CRUD operations. No fancy things are required in the front end. The basic form/list view is enough.

4. Create a Django admin interface for this so that an admin user can log in and add the entries.
5. Admin view should display a list with all the fields from point 1 above. Provide search and filtering with required fields in the admin interface.
6. Create an API to list all the to-do items as well as individual items without using any API Framework also able to view all items in REST API as well

# Steps to Run this Project
Step 1: Clone the project git@github.com:abhishekbudruk007/django-todo-app.git

Step 2: cd ~/django-todo-app

Step 3: Create Virtualenv (Python 3)
         virtualenv -p python3 venv

Step 4: Activate Virtualenv
         source venv/bin/activate

Step 5: Install Dependencies
         pip install -r requirements.txt

Step 6: Migrate To Database
         python manage.py migrate

Step 7: Create Admin
         python manage.py createsuperuser
         # Give Username and Password of Your Choice

Step 8: Run the Project
         python manage.py runserver
         # This will run the project on 127.0.0.1:8000

         You can mention the port and IP of your choice
         python manage.py runserver 0.0.0.0:3000

Step 9: Open URL http://0.0.0.0:3000/ or http://127.0.0.1:8000 in the browser

Step 10: http://0.0.0.0:3000/admin to access admin panel. ( Provide Username and Password you used while creating admin) and entries using the admin panel
![image](https://github.com/sagynangare/Todo-List-with-Django-and-Rest/assets/22528841/2db3991d-4b60-4e10-b8f0-6139575fb874)


Some Project screenshots as below:
# This view uses the Django framework
### Home view:
![image](https://github.com/sagynangare/Todo-List-with-Django-and-Rest/assets/22528841/d59072c1-1e96-4596-81cd-8172e0a024df)

### Add New Item:
![image](https://github.com/sagynangare/Todo-List-with-Django-and-Rest/assets/22528841/c61e8b0e-600b-4349-97cc-0f15d741f3b5)

### Update Existing Item
![image](https://github.com/sagynangare/Todo-List-with-Django-and-Rest/assets/22528841/ec3c3890-bf32-4c09-8e1f-9297068b8f31)

### Delete Item
![image](https://github.com/sagynangare/Todo-List-with-Django-and-Rest/assets/22528841/57d7a4e6-250e-4c1e-a211-24d8f5ae12ca)

# This view uses the Django Rest framework
![image](https://github.com/sagynangare/Todo-List-with-Django-and-Rest/assets/22528841/eec7a13f-e74b-440b-95ff-0444a7e5e68a)
Once you click on Rest, you will get a page like this
![image](https://github.com/sagynangare/Todo-List-with-Django-and-Rest/assets/22528841/2f7e3955-f86e-4dbe-9a92-eb22afd436ba)

Click on ***ToDoRestAPI***

![image](https://github.com/sagynangare/Todo-List-with-Django-and-Rest/assets/22528841/c73a10aa-a0c2-4123-9b5f-d7422557f424)

To check particular list details pass a link like <u>***http://127.0.0.1:8000/api/list/<todo_id>***</u>
for eg: http://127.0.0.1:8000/api/list/4

## To use Django Rest Authentication
use a link to ***register*** a new user: 
<u>http://127.0.0.1:8000/api/register/</u>
and you will get a page like
![image](https://github.com/sagynangare/Todo-List-with-Django-and-Rest/assets/22528841/3908937a-d27b-4fce-84e9-637b0cb9d0fb)

use a link to ***login*** existing user: 
<u>http://127.0.0.1:8000/api/login/</u>
and you will get a page like
![image](https://github.com/sagynangare/Todo-List-with-Django-and-Rest/assets/22528841/e421fd20-16b3-4446-b03a-b264a1cdea2e)

After login, you will get a message like
![image](https://github.com/sagynangare/Todo-List-with-Django-and-Rest/assets/22528841/90009bee-5b64-45e7-ac0c-6bc0b06357f6)

#### If you have any questions or queries please reach out to me
***email id:*** sagy9975340919@gmail.com
***LinkedIn:***https://www.linkedin.com/in/sagar-nangare-0629a09a/
