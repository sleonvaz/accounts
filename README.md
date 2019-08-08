___
## **Index**
- [Task requirements](#task_requirements)
- [App](#app)
    - [Documentation](#documentation)
    - [Prerequirements](#prerequirements)
    - [Starting the project](#starting-the-project)
- [Servicios](#servicios)
- [Urls](#urls)

___


## Task requirements<a name="prerrequisitos"></a>


- Please implement a small Django application to manage (CRUD) users and their bank account data (IBAN). 
    Required fields are first name, last name and IBAN. Data should be validated.
    
       - All fields are integrated and validated.
    
- Administrators of the app should authenticate using a Google account.

        - Administrators create by superuser can authenticate on regular login. 
        
        - Loging as Admin Button  will authenticate or create Admin users.

- Administrators should be able to create, read, update and delete users
    
       - Admisitrators are able to do a CRUD.
        
- Restrict manipulation operations on an user to the administrator who created them
    
        - Admisitrators are able to do a CRUD on the users that they created only
          
- Use PostgreSQL as the database backend

        Use Postgres 11
        
- Use Python 3.x
        
        python:3.7
        
Voluntary to get more points for the task:

- Write documentation on how to setup, run and use your implementation.

        Documentation created.
        

- Test environment

    Set up a virtual machine environment using vagrant (provisioned by Puppet/Salt/Ansible/Bash - whatever suits you best) or docker-compose to run the test task including some short documentation

        - Docker-compose to create a container for django and Postgres. The container will run:
            
            - python manage.py makemigrations
            - python manage.py migrate
            - python manage.py test 
            - python manage.py runserver
        
 - Extra tasks: 
  
            - Admisitrators can see the others administrators users.
            - Superuser can create administrators, and do a CRUD to clients.
            - Users can change their password.          
            - Autodoc library to auto generate project documentation as an html rindus-task/docs/build/html/index.html
              (open in browser).
            - Helper Logger to log the app.
            - Cerberus library to validate an normalize data structures.        
---
## **Documentation**<a name="documentation"></a>
The project documentation is an html to access click on this link:
[Project documentation](/docs/build/html/index.html)

---
       
##Prerequirements<a name="rerequirements"></a>
You need to install **docker**, you can download windows docker here:
https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe

When docker is installed, you need to reboot your computer. To check if docker is installed, type this on your cmd:
````
docker --version
````


___

##**Creating Django superadmin**<a name="creating-django-superadmin"></a>
To create a superuser open a terminal, **while project is running** and **in the project folder 'src'** 
exec the next command:
````
docker exec -ti rindus-task_app_1 python manage.py createsuperuse
````
Then follow the instructions:
1. username
2. admin email
3. password  
___

## **Service**<a name="service"></a>

| SERVICE       |    ENDPOINT               |   USER     |   PASSWORD |
| --------------|:-------------------------:|:----------:|:----------:|
| postgres-11   |  http://localhost:3333    |   root     |   root     |          
| app           |  http://localhost:8000    |   no       |   no       |     
 

## **Urls**<a name="urls"></a>

| APLICACION       |    ENDPOINT               |   DESCRIPCION     |   AUTHENTICATION  |
| -----------------|:-------------------------:|:-----------------:|:-----------------:|
| Access           |  /manager/signup/         |  Admin singup     |        YES        |
| Access           |  /signup/                 |  Client singup    |         NO        |
| Access           |  /user/signup/            |  Admin singup     |        YES        |
| Access           |  /accounts/               | login and log out |        YES        |
| Clients          |  /clients                 |  Clients list     |        YES        |
| Clients          |  /client/<int:pk>         |  Client detail    |        YES        |
| Clients          |  /create                  |  Create client    |        YES        |
| Clients          |  /delete/<int:pk>         |  Delete client    |        YES        |
| Clients          |  /update/<int:pk>         |  Update client    |        YES        |