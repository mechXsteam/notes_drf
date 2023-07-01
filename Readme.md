# Everything needs to be documented

## What it does ?

This project is a part of my *dj Notes* app. This is just the backend part of it, implemented using django rest
framework.

#### Installation guide

1. Clone the repository `https://github.com/mechXsteam/notes_drf.git`.
2. Move into the directory in which we have manage.py file using `cd`.
3. Hit `python manage.py runserver` in the terminal to fire up the server.

## Project timeline

1. #### Basic Project Setup

- Started the project with the django's default template.
- Ran command `python manage.py migrate` to create the default table in the database.
- Created an app named `api` to handle the API logic and added the app in the `INSTALLED_APP` list in
  notes_backend/settings.py file.
- Created Note model and registered it in the api/admin.py file.
- Ran command `python manage.py makemigrations` and `python manage.py migrate` to create a table with the name Note in
  the database.
- Ran command `python manage.py createsuperuser` to create a superuser having access to the admin pannel.

2. #### Configuring DRF
   [find the initial steps here...](https://www.django-rest-framework.org/#installation)

- Installed DRF using command `pip install djangorestframework`. 
- Added `rest_framework` in the INSTALLED_APPS list and default rest framework permission in the api/settings.py file.
- Created a NoteSerializer in api/serializers.py file.
- Added CRUD views in the api/views.py file.
- Created urls.py file in the api folder and added routes to access views in api/urls.py. Included the views.urls in the
  api/urls.py file.

3. #### Fixing CORS (Cross Origin Resource Sharing)

- Installed `django-cors-headers` package using command `pip install django-cors-headers`.
- Added `"corsheaders.middleware.CorsMiddleware",` in the MIDDLEWARE list in the notes_backend/settings.py file.
- Configured `CORS_ALLOW_ALL_ORIGINS: True` allowing websites will all different domains to access my API.

4. #### Adding documentation to our API

- Installed dependencies using command `pip install pyyaml uritemplate`. [ref...](https://www.django-rest-framework.org/api-guide/schemas/#install-dependencies)
- Added ```REST_FRAMEWORK = {'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'}``` in the
  notes_backend/settings.py file.
- Configured urls to access the docs
   ```python
   from rest_framework.documentation import include_docs_urls
   from rest_framework.schemas import get_schema_view
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('api/', include('api.urls')),
       path('', include_docs_urls(title="DJ Notes")),
       path('schema', get_schema_view(
           title="DJ Notes",
           description="API for CRUD operations utilised by DJ Notes",
           version="1.0.0"
       ), name='openapi-schema'),
   ]
   
   ```

## FAQ's

1. #### What is a serializer ?
   In short, it is used to convert django queryset instances into JSON and data
   validation. [more...](https://www.django-rest-framework.org/tutorial/1-serialization/#tutorial-1-serialization)
2. #### What is CORS and how can I fix that ?
   It is a security mechanism implemented in web browsers that controls how web pages from one domain are allowed to
   interact with resources from a different domain.
   By default, web browsers follow the Same-Origin Policy, which restricts JavaScript code running in a web page from
   making requests to a different domain. However, CORS provides a way to relax these restrictions and enable controlled
   cross-origin requests.
    - Origin - the source of the web page, combination of domain,protocol and port.
    - CORS Request - when a web page makes a cross-origin request the browser sends the origin of the request in the
      HTTP request header.
    - Now, it is upto the server to allow the request or not.
      To solve the CORS error, we use django-cors-headers package in python. Configuring this package will allow the
      access of
      our api to other websites. <br>
      [find the initial steps here...](https://pypi.org/project/django-cors-headers/)