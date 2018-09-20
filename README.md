# EC463 MiniProject

This project was written in python3 using the Django web framework 

Link for final project (hosted on AWS): http://13.59.50.148:8000/accounts/login/?next=/catalog/

Links to development log (Agile sprint planning) :  
* Sprint 1 (1 week):http://bit.ly/2OxIO2N 
* Sprint 2 (1 Week): http://bit.ly/2pmJsFJ 

## Authors:
Mohammad Ali Al-Rajjal (mohdali@bu.edu) , &nbsp; Biyao Liang (liangb@bu.edu)   

## Individual contributions:
 * Mohammad: Worked on configuring app settings, creating database mapping, implementing the charting API and creating login system 
 
 * Biyao: Worked on data manipulation, URL configurations, front-end template design, and AWS configurations. 
 
## Install project on local machine (developer mode): 
* Clone the repository. 

* Install, create and launch a virtual environment using virtualenv with python3.

* Install mysql and create a database called “ec463_miniproject” as a root user. 

* Install Django.
```
pip install django==2.1.1
```

* Install mysqlclient (python package). 

* Edit line 74 of the settings.py file by replacing the asterisks with your mysql root user password. 

* Run Database Migrations  (under this directory: EC463MiniProject/EC463_mini_project/).  

```
Python3 manage.py makemigrations
Python3 manage.py migrate 
```
* Create a superuser: 
```
python manage.py create superuser
```
* Run the local development server: 
```
python manage.py runserver
```
* Browse to  127.0.0.1:8000
