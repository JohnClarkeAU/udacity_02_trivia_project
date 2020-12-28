# Full Stack API Trivia Project

## Description of the project

The trivia app has been developed to enable users to manage questions and also play the trivia game.

The application allows for the following:

1) Display questions - both all questions and by category. Questions show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

This trivia app demonstrates the ability to structure plan, implement, and test an API - skills essential for a full stack web developer.

## Code Style
The code adheres to the [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/) and follows common best practices.  When updating the code please ensure that the PEP 8 style guide is followed including the following best practices:

[Variable and function names are clear](https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions).

Endpoints are logically named.

Code is [commented appropriately(https://www.python.org/dev/peps/pep-0008/#comments)].

## Project Structure

The project consists of the Frontend which displays the information to the user and communicates with the Backend to access information from the database of questions.
There are three README.md files in the following folders, so you should start by reading each of the READMEs in:

1. [`./`](./README.md) This README.md
2. [`./frontend/`](./frontend/README.md)
3. [`./backend/`](./backend/README.md)

We recommend following the instructions in those files in order to set up your project.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository for review. 

### Update .gitignore
You should exclude any local files, the python virtual environment and node modules directories from your version control system using `.gitignore` or similar, before submitting to github or for review by including the following lines in the [`.gitignore`](./.gitignore) file.

```
.vscode
__pycache__
venv
env
node_modules
```

## About the Stack

The full stack application has been designed with the following key functional areas:

### Backend

The `./backend` directory contains a Flask and SQLAlchemy server. The `__init__.py` source file defines the API endpoints and `models.py` defines the DB and SQLAlchemy setup. 

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. The endpoints in the `.js` files within the `./frontend/src/components` folder must match and integrate with the equivalent endpoints in the backend.

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. 

[View the README.md within ./frontend for more details.](./frontend/README.md)
