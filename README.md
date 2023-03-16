# Python API development

## About
This is a full-fledged API in Python using FastAPI. It includes fundamentals of API design like routes, serialization/deserialization, schema validation, and models and also 
SQL, testing with pytest, and how to build out a CI/CD pipeline using GitHub actions.

## Features
 + Database Connection Using SQLAlchemy
 + FastAPI Server
 + Unit Testing with PyTest
 + Basic CRUD for Posts

## Dependencies
+ Python 3.9+
+ Pip
+ Alembic
+ Other listed in requirements.txt

## Development Environment Setup
+ Install Python(Version 3)
+ Install and Configure VS code
+ Setup Virtual Environment

## Installation
  ```
  $ pip install fastapi 
  ```
     You will also need an ASGI server, for production such as Uvicorn 
  ``` 
  $ pip install "uvicorn[standard]"
  ```
 
 ### Example
 #### Create It
 + Create a file main.py with:
 
 ```python
 
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```
#### Run It:
Run the server with:
```
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

<details>
<summary>About the command uvicorn main:app --reload...</summary>
<br>
The command uvicorn main:app refers to:

+ main: the file main.py (the Python "module").
+ app: the object created inside of main.py with the line app = FastAPI().
+ --reload: make the server restart after code changes. Only do this for development.
</details>

## API Testing Tool
+ Download Postman
  
  - Postman lets users create collections for their Postman API calls. Each collection can create subfolders and multiple requests. This helps in organizing your test suites.
  - There are different types of requests that can be made:

     * GET — Retrieve data
     * POST — Send data.
     * PUT — Update ( Updates the entire resource. Like POST but with a defined URI)
     * PATCH — Update ( Updates partially will not create a resource if resource does not exist)
     * DELETE — Deletes data.

## Setting up FastAPI and PostgreSQL

The easiest way to run the Postgres server is by using Docker and Docker-compose

+ Install PostgreSQL and create your user and database

    * Start the PostgreSQL Docker container:
        ```
        $ docker-compose up -d 
        ```
    * Stop the container:
        ``` 
        $ docker-compose down 
        ```
+ Connecting to the PostgreSQL Server
   * By default, SQLAlchemy uses psycopg2 to interact with the PostgreSQL server.
     ```
     pip install sqlalchemy psycopg2 
     ```

+ execute PostgreSQL commands to communicate with the Postgres server
  ``` 
  docker exec -it <container name> bash 
  ```


## Interactive API docs

Now go to http://127.0.0.1:8000/docs.
You will see the automatic interactive API documentation (provided by Swagger UI):
![image](https://user-images.githubusercontent.com/70798723/225622226-8363cae5-1670-4a77-a1c2-91aecf3a753a.png)


## Deployment
+ Heroku
+ Docker

## Demo Link















 
