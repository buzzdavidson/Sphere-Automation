DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3', 
    'NAME': '/tmp/sphere-automation.db',
  }
}
INSTALLED_APPS = ['sphere-automation']
ROOT_URLCONF = ['sphere-automation.urls']
