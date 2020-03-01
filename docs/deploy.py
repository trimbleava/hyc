# create the project
django-admin startproject HYC
mv HYC to Hydroclimate  - only for more distinction

"""
HYC name deendencies:
HYC/settings 
	--> ROOT_URLCONF = 'HYC.urls'
	--> WSGI_APPLICATION = 'HYC.wsgi.application'
Hydroclimate/manage.py
	--> os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HYC.settings')
"""

# test the project setup
python manage.py runserver 0:8000
http://127.0.0.1:8000

# create an app - both valid
django-admin startapp hyc
python manage.py startapp hyc

# add a test view
hyc.views.py --> see def testview

# map the view to url
hyc.urls.py --> see urlpatterns

# point the root URLconf at the hyc.urls module
HYC.urls.py --> see urpatterns

# test the app
python manage.py runserver
http://127.0.0.1:8000/hyc

# add postgres/postgis database to project
# install python database bindings psycopg2 package
python manage.py check                      # before migrate to see if there is any problem
python manage.py migrate                    # all model tables
python manage.py migrate polls 0001         # only this app/version

# update models.py
python manage.py makemigrations
python manage.py migrate                    # all model tables

# add templates
mkdir hyc/templates/hyc/index.html
""" 
How Django will load and render bove template structure
By convention DjangoTemplates looks for a “templates” subdirectory in each of the INSTALLED_APPS.
TEMPLATES = [
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
]
"""
