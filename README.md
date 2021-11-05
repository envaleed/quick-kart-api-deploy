# Quick Kart API

This Quick Kart API interfaces with the front end of the Android application made by another contributor. To test the API, you may use curl or Postman to send requests to the end points

# Endpoints

### Register

#### Request

```
curl -d '{"username":"<YOUR NAME>","password":"<YOUR PASSWORD>","email":"<YOUR EMAIL>"}' -H "Content-Type: application/json" -X POST https://quickkart-api.herokuapp.com/api/registration/
```

#### Response

Successful Registration

```{"You have successfully registered":"Marcus"}```

Failed Registration

```"The username or email is already in use"```

### Login with JWT Authentication

#### Request

```
curl -d '{"username":"<YOUR NAME>","password":"<YOUR PASSWORD>"}' -H "Content-Type: application/json" -X POST https://quickkart-api.herokuapp.com/auth
```

Successful Login

```{"access_token":"<YOUR TOKEN HERE"}```

Failed Login

```{"description":"Invalid credentials","error":"Bad Request","status_code":401}```

