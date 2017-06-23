# Basic Django Web App

* Introduction to setting up Django - https://pythonprogramming.net/django-web-development-with-python-intro/
* Create a basic Django Project - https://docs.djangoproject.com/en/1.11/intro/tutorial01/

## Instructions
* Run App on localhost using the following on the command line from the project directory `python manage.py runserver`
* However if you have multiple versions of Python installed on your machine you can specify which version of python (python3 in this case) you'd like to run your `manage.py` by stating the path before it - 
```python
C:/Users/Christiaan/AppData/Local/Programs/Python/Python36-32/python manage.py runserver
```

* Localhost Served at http://127.0.0.1:8000/

* Run Python 3 from terminal `C:/Users/Christiaan/AppData/Local/Programs/Python/Python36-32/python`

## Python 3.6 .exe Location
* `C:\Users\Christiaan\AppData\Local\Programs\Python\Python36-32`

### Create App from Site 
* Run the following to create an app 
```python
C:/Users/Christiaan/AppData/Local/Programs/Python/Python36-32/python manage.py startapp someName
```
* Add `someName` to `settings.py` in `myapp` directory.
* Edit `urls.py` to include our webapp url.
* Add to our `views.py` for `webapp`( add an http response with a simple hello world response).
* Create `urls.py` relative to our `webapp`
* Run our local server to and test the url with `http://localhost:8000/webapp/`

### Templating with Jinja2
* Create an app (instructions above) and it to `settings.py`
* Add `urls.py` and edit `views.py`to render our `html` pages with the jinja templates  (include,extends). 

## Python References
* Python for Windows 3.6.1 (https://www.python.org/downloads/windows/)
