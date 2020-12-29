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

1. Flask-CORS is used to enable cross-domain requests and set response headers. 
2. There are error handlers for all expected errors including 400, 404, 405, 422 and 500. 

The frontend can be reviewed to identify the endpoints that the backend is expected to service together with the response data formats required. 

You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. [GET    '/'](#get-) A dummy endpoint that displays 'Hello' to check if the server is running
2. [GET    '/categories'](#get-categories) An endpoint that handles GET requests for all available categories. 
3. [GET    '/questions'](#get-questionsspageintpagerequired) An endpoint that handles GET requests for questions, including pagination (every 10 questions). This endpoint returns a list of questions, number of total questions, current category, categories. 
4. [DELETE '/questions/<question_id>'](#delete-questionsintquestion_id) An endpoint that DELETEs a question using a question ID. 
5. [PUT    '/questions'](#put-questions)] An endpoint that PUTs a new question into the database, which will require the question and answer text, category, and difficulty score. 
6. [POST   '/questions'](#post-questionspageintpagerequired)] A POST endpoint that gets questions based on a search term. It returns any questions for whom the search term is a substring of the question. 
7. [GET    '/categories/<category_id>/questions'](#get-categoriesintcategory_idquestionspageintpagerequired) A GET endpoint that gets questions based on category_id. 
8. [POST   '/quizzes'](#post-quizes) A POST endpoint that gets questions to play the quiz. This endpoint takea category and previous question parameters and returns a random questions within the given category, if provided, and that is not one of the previous questions. 

## Testing the API
The unitest library has been used to create one or more tests for each endpoint to test for expected success and error behaviour.

All the tests are included in the test_flasker.py file within the backend folder.  When updating the project ensure that the tests are run and that they all pass.  When adding new functionality appropriate tests should be added to the test_flasker.py file.

Tests are run using the `trivia_test` database so as to avoid corrupting the live `trivia` database.

### Running the tests
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
To use the API endpoints you must first run the backend server using the following commands:
```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

## Base URL
At present this app can only be run locally and is not hosted as a base URL. 

The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration. 

## Errors
Errors are returned as JSON objects in the following format:
```json
{
    "success": false, 
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


## Endpoints

### Endpoints Index
The following endpoints are accepted by the API

GET    '/'
GET    '/categories'
GET    '/questions'
DELETE '/questions/<question_id>'
PUT    '/questions'
POST   '/questions'
GET    '/categories/<category_id>/questions'
POST   '/quizzes'

---
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

---
### GET '/categories'
Retrieve all categories

#### curl
```bash
curl http://127.0.0.1:5000/categories
```
#### response
```json
{
  "success": true,
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
```json
{
  "error": 404,
  "message": "404 Not Found: There are no categories available.",
  "success": false
}
```

---
### GET '/questionss?page=<int:pagerequired>'
(page is optional - default page=1)

Retrieve all questions (up to 10 per page)
#### URL parameters
```
page=<int:pagerequired> (default page=1)
```
#### returns
```
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
```json
{
  "success": true,
  "total_questions": 33,
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
Page nuber is past the end.
```bash
curl http://127.0.0.1:5000/questions?page=99999
```
#### errors
```json
{
  "error": 404,
  "message": "404 Not Found: There are no questions on that page.",
  "success": false
}
```

---
### DELETE '/questions/<int:question_id>'
Delete a specific question with the ID specified.

#### curl
```bash
curl -X DELETE http://127.0.0.1:5000/questions/15
```
#### response
```json
{
  "success": true,
  "deleted": "15"
}
```
#### curl to generate an error
An invalid ID is specified.
```bash
curl -X DELETE http://127.0.0.1:5000/questions/99999
```
#### errors
```json
{
  "error": 404,
  "message": "404 Not Found: Question ID does not exist.",
  "success": false
}
```

---
### PUT '/questions'
Add a new question to the database
#### json parameters
```
question=<str:text_of_the_question>
answer=<str:text_of_the_answer>
difficulty=<int:1-5>
category=<int:category_id>
```
##### sample json parameters
```json
{
    "question": "What colour is the sky",
    "answer": "Blue",
    "difficulty": "3",
    "category": "4"
}
```
#### curl
```bash
curl -X PUT http://127.0.0.1:5000/questions --header "Content-Type:application/json" -d '{"question": "What colour is the sky", "answer": "Blue", "difficulty": "3", "category": "4"}'
```
#### response
```json
{
  "success": true
}
```

#### curl to generate an error
The question, answer, difficulty and category parameters are not supplied
```bash
curl -X PUT http://127.0.0.1:5000/questions
```
#### errors
```javascript
{
  "error": 422,
  "message": "422 Unprocessable Entity: question, answer, difficulty and category must be supplied.",
  "success": false
}
```
#### other errors
```javascript
  "message": "422 Unprocessable Entity: None of the fields may be blank.",
  "message": "422 Unprocessable Entity: The difficulty must be between 1 and 5 inclusive.",
  "message": "422 Unprocessable Entity: The category specified does not exist.",
  "message": "422 Unprocessable Entity: Unexpected error accessing the database.",
```

---
### POST '/questions?page=<int:pagerequired>'
(page is optional - default page=1)

Search for any questions for whom the search term is a substring of the question (up to 10 per page).

#### parameters
```
searchTerm=<str:search_term>
```
##### sample json parameters
```json
{
    "searchTerm": "beetle"
}
```
#### curl
```bash
curl -X POST http://127.0.0.1:5000/questions?page=1 --header "Content-Type:application/json" -d '{"searchTerm": "beetle"}'
```
#### response
```json
{
  "success": true,
  "total_questions": 33,
  "current_category": null,
  "questions": [
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ],
}
```

#### curl to generate a not found error
The searchTerm does not match any questions
```bash
curl -X POST http://127.0.0.1:5000/questions?page=1 --header "Content-Type:application/json" -d '{"searchTerm": "zzzz"}'
```
#### not found error
```json
{
  "error": 404,
  "message": "404 Not Found: There are no questions matching the searchTerm.",
  "success": false
}
```
#### curl to generate an error
The searchTerm parameter is  not supplied
```bash
curl -X POST http://127.0.0.1:5000/questions
```
#### errors
```json
{
  "error": 422,
  "message": "422 Unprocessable Entity: searchTerm must be supplied.",
  "success": false
}
```
#### other errors
```json
  "message": "422 Unprocessable Entity: Unexpected error accessing the database.",
  "message": "404 Not Found: There are no questions matching the searchTerm.",
  "message": "404 Not Found: There are no more questions matching the searchTerm.",
```

---
### GET '/categories/<int:category_id>/questions?page=<int:pagerequired>'
(page is optional - default page=1)

Search for any questions within a specific category (up to 10 per page).

#### parameters
```
none
```

#### curl
```bash
curl http://127.0.0.1:5000/categories/3/questions?page=1
```
#### response
```json
{
  "success": true,
  "questions": [
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "NewA1",
      "category": 3,
      "difficulty": 3,
      "id": 39,
      "question": "NewQ1"
    },
    {
      "answer": "A13",
      "category": 3,
      "difficulty": 2,
      "id": 42,
      "question": "Q13"
    }
  ],
}
```

#### curl to generate a not found error
An invalid category is specified
```bash
curl http://127.0.0.1:5000/categories/9999/questions?page=1
```
#### not found error
```json
{
  "error": 404,
  "message": "404 Not Found: No questions match that search.",
  "success": false
}
```
#### other errors
```json
  "message": "404 Not Found: There are no more questions that match that search..",
  "message": "422 Unprocessable Entity: Unexpected error accessing the database.",
```

---
### POST '/quizzes'
Using the category and previous question parameters, return a random question within the given category (if provided), that is not one of the previous questions.

#### json parameters
```
previous_questions a list of question_IDs that should not be returned
quiz_category['id'] 0=questions from any category, otherwise only return questions from the category specified
```
##### sample json parameters
```json
{
    "previous_questions": [
        21,
        31,
        34
    ],
    "quiz_category": {
        "type": "Science",
        "id": 1
    }
}
```

#### curl (get a question in the Science Category)
```bash
curl -X POST http://127.0.0.1:5000/quizzes --header "Content-Type:application/json" -d '{ "previous_questions": [21,31,34], "quiz_category": {"type":"Science","id":1} }'
```
#### response
```json
{
  "success": true,
  "question": {
    "answer": "The Liver",
    "category": 1,
    "difficulty": 4,
    "id": 20,
    "question": "What is the heaviest organ in the human body?"
  },
}
```
#### curl (get any question in any Category)
```bash
curl -X POST http://127.0.0.1:5000/quizzes --header "Content-Type:application/json" -d '{ "previous_questions": [], "quiz_category": {"type":"click","id":0} }'
```
#### response
```json
{
  "success": true,
  "question": {
    "answer": "One",
    "category": 2,
    "difficulty": 4,
    "id": 18,
    "question": "How many paintings did Van Gogh sell in his lifetime?"
  },
}
```

#### curl to generate an error (previous questions not a list)
```bash
curl -X POST http://127.0.0.1:5000/quizzes --header "Content-Type:application/json" -d '{ "previous_questions": 0, "quiz_category": {"type":"click","id":0} }'
```
#### error response
```json
{
  "error": 422,
  "message": "422 Unprocessable Entity: The previous_questions parameter must be a list (even if it is empty)",
  "success": false
}
```
#### other errors
```json
  "message": "422 Unprocessable Entity: A list of previous_questions parameter must be provided (even if it is empty).",
  "message": "422 Unprocessable Entity: The previous_questions parameter must be a list (even if it is empty).",
  "message": "422 Unprocessable Entity: A quiz_category parameter must be provided (set 'id':0 to specify any category).",
  "message": "422 Unprocessable Entity: A quiz_category['id'] parameter must be provided (set 'id':0 to specify any category).",
  "message": "422 Unprocessable Entity: Unexpected error accessing the database.",
```
