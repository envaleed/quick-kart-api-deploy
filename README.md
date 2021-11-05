# Quick Kart API

This Quick Kart API interfaces with the front end of the Android application made by another contributor. To test the API, you may use curl or Postman to send requests to the end points.

# Libaries and Technologies

This API was developed using the Python microframework, Flask and tested using Postman and the curl command line tool. The libraries I used are as follows:

1. Flask-SQLAlchemy to connect to the cloud Postgresql database 
2. Flask-Bcrypt to hash and salt the passwords 
3. Flask-JWT for authorization using JWT tokens
4. Flask-Marshmallow for JSON serialization

# Endpoints

### Register

```
curl -d '{"username":"<YOUR NAME>","password":"<YOUR PASSWORD>","email":"<YOUR EMAIL>"}' -H "Content-Type: application/json" -X POST https://quickkart-api.herokuapp.com/api/registration/
```

### Login with JWT Authentication

```
curl -d '{"username":"<YOUR NAME>","password":"<YOUR PASSWORD>"}' -H "Content-Type: application/json" -X POST https://quickkart-api.herokuapp.com/auth
```

### Search for Groceries

```
curl -XPOST -H 'Authorization: jwt <TOKEN FROM /auth>' -H "Content-type: application/json" -d '{"keyword":"fruit"}' 'https://quickkart-api.herokuapp.com/api/search/'
```

### Add Orders to Cart

```
curl -XPOST -H 'Authorization: jwt <TOKEN FROM /auth>' -H "Content-type: application/json" -d '[{"title":"Bananas","quantity":12},{"title":"Apples","quantity":10},{"title":"Oranges","quantity":20 },{"title":"Blueberries","quantity":18}]' 'https://quickkart-api.herokuapp.com/api/postorder/'
```

### Find An Orders

```curl -XGET -H "Content-type: application/json" 'https://quickkart-api.herokuapp.com/api/findorder/<id>/<title>'```

### Find All Orders

```curl -XGET -H "Content-type: application/json" 'https://quickkart-api.herokuapp.com/api/findorders/<id>/'```
