# booking_api

#### Running Tests in Development 

### How do I get set up? ###

* Clone the repo: ```git clone https://github.com/Sajzad/booking_api.git```.

* Install virtualenv on your system. For linux: ```pip install virtualenv```.

* Go to booking_api dir. And create virtual environment with virtualenv: ```virtualenv -p /usr/bin/python3 .env```.

* Activate the virtual environment: source ```.env/bin/activate```.

* Install required dependencies: ```pip install -r requirements.txt```.

* Set these environment variables which is forwarded via email with corresponding values.

* Go to website dir where the manage.py file.

* Create migrations files: ```./manage.py makemigrations```.

* Update the database with migrations: ```./manage.py migrate```.

* Start the local server: ```./manage.py runserver```.

**.Environent Variable **
```
    SECRET_KEY=foo
```


### Dependencies Used

```
asgiref==3.4.1
Django==3.2.9
django-cors-headers==3.10.0
djangorestframework==3.12.4
importlib-metadata==4.8.2
Markdown==3.3.6
pytz==2021.3
sqlparse==0.4.2
typing_extensions==4.0.0
zipp==3.6.0
```

## API Endpoints


```
| EndPoint                                        |           Functionality             |
| ------------------------------------------------|-----------------------------------: |
| POST /api/rooms//                               |      Get list of rooms available    |
| POST /api/create-room/                          |           Create a new room         |
| POST /api/book-room/                            |               Book a room           |
| GET /api/reservations/                          |       Get list of reservations      |
```
## Responses

The API responds with JSON data by default.

