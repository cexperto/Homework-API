
# Homework

A project to make crud with movies table with user registered and authenticated


## Deployment

Project in AWS : http://100.25.109.41/

To deploy this project in local, ther are 2 options: cli, Manually

Manually:


venv in linux (make sure have root permissions):

    sudo apt install python3-virtualenv python3-venv
    virtualenv -p `which python3` venv
    source venv/bin/activate
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    python3 manage.py makemigrations customusers movies randomnumber
    python3 manage.py migrate
    python3 manage.py loaddata homework/fixtures/data.json
    python3 manage.py runserver


venv in windows:

    python -m venv venv
    source venv/scripts/activate
    pip install -r requirements.txt
    python manage.py makemigrations customusers movies randomnumber
    python manage.py migrate
    python manage.py loaddata homework/fixtures/data.json
    python manage.py runserver


With cli:

run:

linux:

    chmod u+x clili
    ./clili

windows:

    chmod u+x cliwin
    ./cliwin


When the project already runing go to 


http://127.0.0.1:8000/


## API Reference

http://127.0.0.1:8000/

#### index
```http
  GET /
```
Response:
  
    homework API

    status 200

#### Signup

```http
  POST /auth/signup/
```
Json example:

    {
        "email": "newuser@mail.com",
        "password": "Thepass54678!"
    }

Response:

    {
        "message": "User created successfully",
        "data": {
            "email": "newuser@mail.com"
        }
    }
    status 201



#### Login

```http
  POST /auth/login/
```

Json example:

    {
        "email": "newuser@mail.com",
        "password": "Thepass54678!"
    }

Response:

    {
        "message": "Login Successfull",
        "tokens": {
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0NDg0NDI1LCJpYXQiOjE2NzQ0ODMyMjUsImp0aSI6ImQ5OTA2ZTUxYjBmNjRmMjJhOWIxZGRmOWI3OTc2ODA1IiwidXNlcl9pZCI6NH0.XK_JGRGV3GbUQa3sCUmijkgr6_fqcJ1VuADgPCGGl6A",
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NDU2OTYyNSwiaWF0IjoxNjc0NDgzMjI1LCJqdGkiOiIyZmJlM2I1NDVmM2E0MzkyODA5MDEzMDFiMDNkZTc4NiIsInVzZXJfaWQiOjR9.QJGRu6dklvcHLWCR1vyCvU8GrKIDMuOO5GEkYxEcvzo"
        }
    }
    status 200


#### Get all public movies

```http
  GET /movies/
```
Headers
| key |      Value                       |
| :--------  | :-------------------------------- |
| `Authorization` | Bearer <access token> |

#### Create movie

```http
  POST /movies/
```
Headers
| key |      Value                       |
| :--------  | :-------------------------------- |
| `Authorization` | Bearer <access token> |

Json example:

    {
        "name":"names public",
        "description":"description",
        "year": "2020",
        "category":"category",
        "private": 0
    }
    private values:
    0 for public content
    1 for private content

Response

    {
        "id": 9,
        "name": "names public",
        "description": "description",
        "year": "2020",
        "category": "category",
        "private": 0
    }
    status 201


#### Get all movies from user

```http
  GET /movies/my_movies/
```
Headers
| key |      Value                       |
| :--------  | :-------------------------------- |
| `Authorization` | Bearer <access token> |

#### get, update, delete one movie

#### Get
```http
  GET /movies/<id>/
```
Headers
| key |      Value                       |
| :--------  | :-------------------------------- |
| `Authorization` | Bearer <access token> |


Response:

    status 200
    for item what belong to user

    status 404
    for item does not belong to user

#### Update

Headers
| key |      Value                       |
| :--------  | :-------------------------------- |
| `Authorization` | Bearer <access token> |

```http
  PUT /movies/<id>/
```
Json example:

    {
        "id": 7,
        "name": "names private",
        "description": "description",
        "year": "2020",
        "category": "category2020",
        "private": 1
    }

Response

status 200

#### Partial update
```http
  PATCH /movies/<id>/
```
Headers
| key |      Value                       |
| :--------  | :-------------------------------- |
| `Authorization` | Bearer <access token> |

Json example:

    {    
        "description": "description modified"    
    }

Response 

status 200 ok

#### Delete

```http
  Delete /movies/<id>/
```
Headers
| key |      Value                       |
| :--------  | :-------------------------------- |
| `Authorization` | Bearer <access token> |

Response

status 204


#### Random number

```http
  POST /random/
```

Headers
| key |      Value                       |
| :--------  | :-------------------------------- |
| `Authorization` | Bearer <access token> |

Json example:

    {
        "numberone": 1,
        "numbertwo": 10
    }

Response

    {
        "number": [
            "[6]"
        ]
    }

```http
  GET /random/
```
If the request is not Post the api take 1 and 10 numbers

Response example

    {
        "number": [
            "[6]"
        ]
    }


#### Refresh Token

Refresh token after 20 min

```http
  POST /auth/token/refresh/
```
Json example:

    {
        "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NDU2NjcyNCwiaWF0IjoxNjc0NDgwMzI0LCJqdGkiOiIxOWE4ZTZhNjY1NGY0OGFmYTJhMTgzZGIzYThiNjg2MyIsInVzZXJfaWQiOjN9.1QZ7fDx2Q3G_yRR2-N_kqu2XZRLLtXR9V2JOZBk2kD8"
    }

Response

    {
        "access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0NDg0OTI3LCJpYXQiOjE2NzQ0ODAzMjQsImp0aSI6IjVkZjFlMWU5ZWY2ZDRlMTFhMGY1ZGYyMzE3OWEwOTAxIiwidXNlcl9pZCI6M30.QbyZk-0T4DjAYCWhrit_dxvCouRD_-7Gt-Ycq1SqSRw"
    }


Run tests:

run:

Windows:

    python manage.py test

Linux:

    python3 manage.py test


## Authors

- [@cexperto](https://www.github.com/cexperto)

