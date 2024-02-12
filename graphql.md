# Graphql Queries

### Token Auth:

- Query:
```
    mutation{
        tokenAuth(email:"test@gmail.com", password:"@Abhinav05"){
            token
            refreshToken
            success
            errors
        }
    }
```

- Response:
```
    {
        "data": {
            "tokenAuth": {
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RAZ21haWwuY29tIiwiZXhwIjoxNzA3NzY3MDY2LCJvcmlnSWF0IjoxNzA3NzY2NzY2fQ.9LXITy4DuNNlMRFPbMKSZ8uY7GCpvIJeckEiJDawlfg",
            "refreshToken": "4df9cf77b310cdc57aae13802d76415f1472ca8a",
            "success": true,
            "errors": null
            }
        }
    }
```

### Refresh Token:

- Query:
```
mutation {
  refreshToken(refreshToken:"4df9cf77b310cdc57aae13802d76415f1472ca8a"){
    token
    success
    errors
  }
}
```

- Response:
```
{
  "data": {
    "refreshToken": {
      "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RAZ21haWwuY29tIiwiZXhwIjoxNzA3NzY3NDc3LCJvcmlnSWF0IjoxNzA3NzY3MTc3fQ.ijFNhvmw0f8zU7JMcV0b4kNwqwNJ7DnB6zbNzCwsKSk",
      "success": true,
      "errors": null
    }
  }
}
```

### Query (Me):

- Headers:
```
{
  "Authorization":"JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InRlc3RAZ21haWwuY29tIiwiZXhwIjoxNzA3NzY3MDY2LCJvcmlnSWF0IjoxNzA3NzY2NzY2fQ.9LXITy4DuNNlMRFPbMKSZ8uY7GCpvIJeckEiJDawlfg"
}
```

- Query:
```
query{
  me{
    id
    email
    userType
  }
}
```

- Response:
```
{
  "data": {
    "me": {
      "id": "VXNlck5vZGU6Mg==",
      "email": "test@gmail.com",
      "userType": "STARTUP"
    }
  }
}
```