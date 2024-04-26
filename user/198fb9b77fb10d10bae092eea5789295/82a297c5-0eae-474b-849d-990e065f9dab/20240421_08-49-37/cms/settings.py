# filename: cms/settings.py

# settings.py - Configuration file for the CMS project

DATABASE = {
    'default': {
        'NAME': 'cms.db',
        'ENGINE': 'sqlite3',
    }
}

SECRET_KEY = "secret_key_here"  # Replace with a secret key

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]