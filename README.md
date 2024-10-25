# TaskPilot
TaskPilot is a web application designed for simple project management. It combines the power of **Streamlit** 
for front-end display and **Django** for backend data management.

## How to run on localhost
### Install requirements
```
pip install -r requirements.txt
```

### Configure database information in [settings.py](task_pilot/settings.py)
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db',
        'USER': 'db_user',
        'PASSWORD': 'db_user_password',
        'HOST': 'db_host',
        'PORT': 'db_port',
    }
}
```
### Start Django server
```
python manage.py runserver 0.0.0.0:8000
```

### Launch Streamlit Interface
```
streamlit run taskpilot_streamlit/taskpilot_app.py
```
If your browser does not open automatically, navigate to http://localhost:8501 to access the app.