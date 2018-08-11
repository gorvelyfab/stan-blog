## Stanley Blog

Simple Demo Blog and Portfolio Application build with [Django 2.1](https://docs.djangoproject.com/en/2.1/)

### Install

first, with a terminal change your current directory
to root project directory.

memcached is the main cache system for this app
please install memcached before to continue

Debian like system:
```
apt-get install libevent-dev memcached
```

Install application dependencies with the following command

```
pip install -r requirements.txt
```

### Database setup

The default DB settings use SQLite

But if you wish you can use PostgreSQL, for this please ensure you that PostgreSQL is installed on your system

you should also edit `app/settings.py` for your personal requirements

Example configuration for PostgreSQL:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database_name',
        'USER': 'database_user',
        'PASSWORD': 'database_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

```
if your PostgreSQL use an other port, don't forget indicate them

if you are not accustom with PostgreSQL, you can read a quick tutorial
at https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04


then you can run this command for create all database tables

```
python manage.py migrate
```

### Create a super user for site administration

```
python manage.py createsuperuser
```

you can also load fixtures data

```
python manage.py loaddata data
```

### Running application

For run the Python development server

always on your root project directory run the following command

```
python manage.py runserver
```

by default, a Server will execute at http://127.0.0.1:8000

the admin interface is locate at http://127.0.0.1:8000/admin



If you are encountered problems or detect any bugs
contact me

[Author]
Gorvely Tasida <gorvelyfab@gmail.com>
Website: [braindy.io](https://braindy.io)
