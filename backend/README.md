# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

NOTE: 
This project was originally developed using Python 3.7.
If you are using Python 3.8 you may need to amend a Date/Time function in one of the libraries.

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

You can  set up your virtual environment on Windows using Python 3, by naviging to the `/backend` directory and running:

```bash
py -m venv env
```

On macOS and Linux use:
```bash
python3 -m venv env
```

venv will create a virtual Python installation in the `/backend/env` folder.

NOTE:
You should exclude your virtual environment directory from your version control system using `.gitignore` or similar.

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

NOTE: 
If you encounter error messages indicating that you require Visual C++ 14 compiler files you will need to follow the instructions to download them and install them, or you can manually install each of the packages in the requirements.txt file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, create a database called trivia and restore the contents of the database tables using the trivia.psql file provided. 

From the backend folder in terminal run:

```bash
dropdb trivia (not require on the first initial setup)
createdb trivia
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.  

```bash
source env/Scripts/activate
```
You should now see (env) displayed as part of your terminal prompt.

To leave the virtual environment when you have finished running the server:

```bash
deactivate
```

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

The application is run on http://127.0.0.1:5000/ by default and is a proxy in the frontend configuration. 

## Features

Within the backend API each endpoint defines the endpoint and response data. 

The frontend can be reviewed to identify the endpoints that the backend is expected to service together with the response data formats required. 

You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Flask-CORS is used to enable cross-domain requests and set response headers. 
2. An endpoint handles GET requests for questions, including pagination (every 10 questions). This endpoint returns a list of questions, number of total questions, current category, categories. 
3. An endpoint handles GET requests for all available categories. 
4. An endpoint DELETEs a question using a question ID. 
5. An endpoint POSTs a new question, which will require the question and answer text, category, and difficulty score. 
6. A POST endpoint gets questions based on category. 
7. A POST endpoint gets questions based on a search term. It returns any questions for whom the search term is a substring of the question. 
8. A POST endpoint gets questions to play the quiz. This endpoint takea category and previous question parameters and returns a random questions within the given category, if provided, and that is not one of the previous questions. 
9. There are error handlers for all expected errors including 400, 404, 422 and 500. 

## Testing the API
The unitest library has been used to create one or more tests for each endpoint to test for expected success and error behaviour.

All the tests are included in the test_flasker.py file within the backend folder.  When updating the project ensure that the tests are run and that they all pass.  When adding new functionality appropriate tests should be added to the test_flasker.py file.

Tests are run using the `trivia_test` database so as to avoid corrupting the live `trivia` database.

### running the tests
With Postgres running, create a database called trivia_test and restore the contents of the database tables using the trivia.psql file provided. 

To run the tests, open a terminal window, change to the backend folder and run:

```bash
dropdb trivia_test (not require on the first initial run)
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

NOTE:
`dropdb trivia_test` is used to remove any database that has been used in a previous test.

# API Reference
To use the API endpoints you must first run the server using the following commands:
```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

## Base URL
At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration. 

## Endpoints

### Endpoints Index
The following endpoints are accepted by the API
```
GET    '/'
GET    '/categories'
GET    '/questions'
DELETE '/questions/<question_id>'
PUT    '/questions'
POST   '/questions'
GET    '/categories/<category_id>/questions'
POST   '/quizzes'
```

### GET '/'
Accesses the home page of the backend which just displays "Hello"

#### curl
```bash
curl http://127.0.0.1:5000/
```
#### response
```
Hello
```
#### errors
```
none
```

### GET '/categories'
Retrieve all categories

#### curl
```bash
curl http://127.0.0.1:5000/categories
```
#### response
```javascript
{
  "success": true
  "categories": {     
    "1": "Science",   
    "2": "Art",       
    "3": "Geography", 
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
}
```
#### errors
```javascript
{
  "error": 404,
  "message": "404 Not Found: There are no categories available.",
  "success": false
}
```

### GET '/questions'
Retrieve all questions
#### parameters
```
page=<int:pagerequired> (default page=1)
```
#### returns
```javascript
success (true/false)
total_questions (total number of questions in the database)
current_category null
categories (list of category ID and category description)
questions (list of upto 10 questions for the page requested - id, question, answer, difficulty, category)
```

#### curl
```bash
curl http://127.0.0.1:5000/questions (defaults to page=1)
curl http://127.0.0.1:5000/questions?page=1
```
#### response
```javascript
{
  "success": true,
  "total_questions": 33
  "current_category": null,
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
}
```


#### curl to generate an error
```bash
curl http://127.0.0.1:5000/questions?page=99999
```
#### errors
```javascript
{
  "error": 404,
  "message": "404 Not Found: There are no questions available.",
  "success": false
}
```



## Errors
Errors are returned as JSON objects in the following format:
```javascript
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```

### Error Index
The following error types can be returned by the API when requests fail:
```
400 Bad Request
404 Not Found
405 Method Not Allowed
422 Unprocessable
500 Internal Error
```

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```


