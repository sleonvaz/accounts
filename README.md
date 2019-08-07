___
## **Index**
- [App](#app)
    - [Documentation](#documentation)
    - [Task requirements](#task_requirements)
    - [Prerequirements](#prerequirements)
    - [Starting the project](#starting-the-project)
- [Servicios](#servicios)
- [Urls](#urls)

___
## **Documentation**<a name="documentation"></a>
### Documentation<a name="documentation"></a>
To access to the project documentation is an html to access just link on this link:
[Proyect documentation](/docs/build/)


### Task requirements<a name="prerrequisitos"></a>
Necesitaremos tener instalado **docker**, para ello descargamos la aplicación para windows desde:
https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe

Una vez instalado reiniciamos el ordenador y comprobamos que funciona correctamente ejecutando:
````
docker --version
````


___
___

### Prerequirements<a name="rerequirements"></a>
You need to install **docker**, you can download windows docker here:
https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe

When docker is installed, you need to reboot your computer. To check if docker is installed type this on your cmd:
````
docker --version
````


___
___
### Creating Django superadmin<a name="creating-django-superadmin"></a>
Para acceder al panel de configruación de **Django** necesitamos primero crear un superusuario, para ello 
abrimos una consola **mientras se ejecuta el proyecto** y **en la carpeta src del proyecto** y ejecutamos el siguiente comando:
````
docker-compose exec seth python manage.py createsuperuser
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
| seth          |  http://localhost:8000    |   no       |   no       |     
 

## **Urls**<a name="urls"></a>


| APLICACION       |    ENDPOINT               |   DESCRIPCION     |
| -----------------|:-------------------------:|:-----------------:|
| Admin            |  /admin                  |   Acceso al panel de administracion        |