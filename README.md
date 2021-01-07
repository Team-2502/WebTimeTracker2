# Web Time Tracker 2

A second attempt at an online hour tracker for Talon Robotics using Django and Heroku

https://time-tracker-2502.herokuapp.com

Features basic sign in and out functionality, ability to see the hours for all team members, see the team members currently signed in, and export all hours to a CSV

![img](https://i.imgur.com/o9XwDkM.png)

## Development Setup for school issued MacBooks
* See "Installing Homebrew" [here](https://team-2502.github.io/programming/Homebrew.html)
* `brew install python postgresql`
* `brew tap heroku/brew && brew install heroku`
* `brew services start postgresql`
* Login to Heroku using `heroku login` (DM me on slack for the credentials)
* Add a Heroku Git remote by running `heroku git:remote -a time-tracker-2502` in the project's local directory
* Enter psql using `psql postgres` (you can quit using `\q`)
* Create a password for your default user using `\password [your-username]` and quit postgres using `\q`
* Create a local PostgreSQL database using `CREATE DATABASE [your-database];` or follow instructions [here](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup) to connect to production database
* Ask me for the secret key
* Create local_settings.py in the same directory as settigns.py with your local PostgreSQL database settings and the secret key I gave you (see example below)
* Create a Python virtual environment and run `pip install -r requirements.txt`
* If you are getting errors with psycopg2 you may need to run `pip install psycopg2-binary`

### local_settings.py Example
Your local_settings.py file should like this if using a local instance of PostgreSQL 
```
DEBUG = True
SECRET_KEY = '[secret-key]'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '[your-database]',
        'USER': '[your-username]',
        'PASSWORD': '[your-password]',
        'HOST': 'localhost',
        'PORT': '5432',  # Default port for PostgreSQL
    }
}
```

## Helpful links

* [Getting Started with PostgreSQL](https://www.codementor.io/@engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb#ii-about-postgresql)
* [Getting Started with Django](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
* [Django Docs](https://docs.djangoproject.com/en/3.0/contents/)
