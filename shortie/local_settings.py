DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shortie2021',
        'USERNAME': 'nicoledominguez',
        'OPTIONS': {
            'read_default_file': '/my.cnf',
        },
    }
}