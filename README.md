# django-devworld-deploy

## Functionality
- Django Web Application
- Django REST API
- CRUD
- User Authorization
- Email upon Registering
- Message with other Users
- Keep data safe using Amazon RDS(PostgreSQL) and S3 bucket
- Serverless Application

## What is it?
- Website Community for developers to connect
- Make posts on topics such as Jobs, Projects, Questions, etc


## Built With
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Amazon AWS](https://img.shields.io/static/v1?style=for-the-badge&message=Amazon+AWS&color=232F3E&logo=Amazon+AWS&logoColor=FFFFFF&label=)
![HTML5](https://img.shields.io/static/v1?style=for-the-badge&message=HTML5&color=E34F26&logo=HTML5&logoColor=FFFFFF&label=)
![Bootstrap](https://img.shields.io/static/v1?style=for-the-badge&message=Bootstrap&color=7952B3&logo=Bootstrap&logoColor=FFFFFF&label=)
---
# Home Page
<img src="./staticfiles/images/Screenshot 2022-12-06 at 3.40.11 PM.png">  

# Profile Page
<img src="./staticfiles/images/Screenshot 2022-12-06 at 3.40.38 PM.png">

#Create Post Page
<img src="./staticfiles/images/Screenshot 2022-12-06 at 3.40.51 PM.png">

#Register Page
<img src="./staticfiles/images/Screenshot 2022-12-06 at 3.41.13 PM.png">

#Login Page
<img src="./staticfiles/images/Screenshot 2022-12-06 at 3.41.19 PM.png">

Install python

```
# Make a virtual environment
python -m venv venv

# Activate virtual environment
source ./venv/Scripts/activate

# Pip install required packages
pip install -r requirements.txt

# Make DB
python manage.py makemigrations
python manage.py migrate

# Run Server
python manage.py runserver

# Browser
http://127.0.0.1:8000/main/
```
