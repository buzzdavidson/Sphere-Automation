DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3', 
    'NAME': '/tmp/sphere.db',
  }
}
INSTALLED_APPS = ['sphere']
ROOT_URLCONF = ['sphere.urls']
