# django-api
A simple facial verification web application that allows clients to
store an image of an individual in a database and verify that a submitted image is stored in
the database.

## Usage
```
post request http://192.53.170.233:8000/upload - to upload an image
post request http://192.53.170.233:8000/check - to check if an individual has been recognized

put your image in request body, form-data with key='file'

```

## Deployment
```bash
git clone https://github.com/Jaime-Pinkman/django-api.git
cd django-api
docker-compose up -d --build
```
