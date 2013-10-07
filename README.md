#Blog-taller

Blog para un taller de la comunidad mejorando.la

##Requerimientos:

* Python 2.7
* Sqlite (incluido en python)
* Django 1.5.2
* PIL (Python Image Library

###Entorno virtual

Se recomienda el uso de un entorno virtual o "virtualenv" para no afectar la configuración de django que tienes en el equipo.

    virtualenv blogcomunidad

Luego, para activar el entorno virtual, ejecutamos:

    source blogcomunidad/bin/activate

###Instalar requerimientos

Ahora, podemos instalar los requerimientos de manera muy sencilla:

    pip install -r requirements.txt
    
###Base de datos

Sincronizamos la base de datos sqlite

    python manage.py syncdb
    
###Iniciar proyecto

Finalmente iniciamos el proyecto

    python manage.py runserver
