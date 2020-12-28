""" Trivia App Backend """
import os
import random
import urllib
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
MIN_DIFFICULTY = 1
MAX_DIFFICULTY = 5

def list_routes(app):
    ''' Helper routine for debugging routes '''
    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        # line = ("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        line = ("{:20s} {}".format(methods, rule))
        output.append(line)

    ret = ''
    for line in sorted(output):
        print(line)
        ret = ret + str(line) + '<br />'
    return ret

def paginate_questions(request, questions):
    """ format questions into a single page """
    page = request.args.get('page', 1, type=int)
    start = (page -1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    formatted_questions = [question.format() for question in questions]
    formatted_questions = formatted_questions[start:end]
    return formatted_questions

def create_app(test_config=None):
    """ create the app """
    app = Flask(__name__)
    setup_db(app)

    @app.route('/')
    def index():
        """ Home page of the API """
        ret = "Hello\r\n"

        # ### Uncomment for debugging ###
        # list_of_routes = list_routes(app)
        # ret = "Hello<br />" + list_of_routes

        # ### Uncomment for debugging ###
        # ret = ['%s' % rule for rule in app.url_map.iter_rules()]

        return ret

    # @TODO: DONE Set up CORS. Allow '*' for origins.
    #  Delete the sample route after completing the TODOs
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    # @TODO: DONE Use the after_request decorator to set Access-Control-Allow
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
        return response

    # @TODO: DONE Create an endpoint to handle GET requests for all available categories.
    @app.route('/categories')
    def retrieve_categories():
        '''
        Retrieve all categories
        '''
        categories = Category.query.all()
        if len(categories) == 0:
            abort(404, description="There are no categories available.")
        formatted_categories = {category.id: category.type for category in categories}
        return jsonify({
            'success': True,
            'categories': formatted_categories
        })

    # @TODO: DONE Create an endpoint to handle GET requests for questions,
    #  including pagination (every 10 questions).
    #  This endpoint should return a list of
    #  questions, number of total questions, current category, categories.
    @app.route('/questions')
    def retrieve_questions():
        '''
        Retrieve a page of questions and the categories
        '''
        # Get a page of questions
        questions = Question.query.order_by(Question.id).all()
        formatted_questions = paginate_questions(request, questions)

        # abort with 404 if there are not any questions to return
        if len(formatted_questions) == 0:
            abort(404, description="There are no questions on that page.")

        # get the categories
        categories = Category.query.all()
        formatted_categories = {category.id: category.type for category in categories}

        return jsonify({
            'success': True,
            'questions': formatted_questions,
            'total_questions': len(questions),
            'categories': formatted_categories,
            'current_category': None
        })

    # TEST: At this point, when you start the application
    #  you should see questions and categories generated,
    #  ten questions per page and pagination at the bottom of the screen for three pages.
    #  Clicking on the page numbers should update the questions.

    # @TODO: DONE Create an endpoint to DELETE question using a question ID.
    @app.route('/questions/<question_id>', methods=['DELETE'])
    def delete_question(question_id):
        question = Question.query.get(question_id)

        if question is None:
            abort(404, description="Question ID does not exist.")

        try:
            question.delete()
            return jsonify({
                "success": True,
                "deleted": question_id
            })
        except:
            abort(422)

    # TEST: When you click the trash icon next to a question, the question will be removed.
    #  This removal will persist in the database and when you refresh the page.

    # @TODO: DONE Create an endpoint to POST a new question,
    #  which will require the question and answer text, category, and difficulty score.

    @app.route('/questions', methods=['PUT'])
    def put_questions():
        try:
            question = request.json.get('question')
            answer = request.json.get('answer')
            difficulty = request.json.get('difficulty')
            category = request.json.get('category')
        except:
            abort(422, "question, answer, difficulty and category must be supplied.")

        # check that all fields have been submitted
        if question is None or answer is None or difficulty is None or category is None:
            abort(422, "question, answer, difficulty and category must be supplied.")
        # check that none of the fields are blank
        if question == '' or answer == '' or difficulty == '' or category == '':
            abort(422, description="None of the fields may be blank.")
        # check that the difficulty is within valid range
        if int(difficulty) < MIN_DIFFICULTY or int(difficulty) > MAX_DIFFICULTY:
            abort(422, description="The difficulty must be between 1 and 5 inclusive.")
        # check that the category exists
        if Category.query.get(category) is None:
            abort(422, "The category specified does not exist.")

        try:
            question = Question(
                question = question,
                answer = answer,
                difficulty = difficulty,
                category = category
            )
            question.insert()
            return jsonify({
                "success": True
            })
        except:
            abort(422, "Unexpected error accessing the database.")

    # TEST: When you submit a question on the "Add" tab,
    #  the form will clear and the question will appear at the end of the last page
    #  of the questions list in the "List" tab.

    # @TODO: DONE Create a POST endpoint to get questions based on a search term.
    #  It should return any questions for whom the search term is a substring of the question.
    @app.route('/questions', methods=['POST'])
    def search_questions():
        # get the searchTerm
        try:
            search_term = '%' + request.json.get('searchTerm', None) + '%'
        except:
            abort(422, description="searchTerm must be supplied.")

        # Get a page of questions
        try:
            questions = Question.query.filter(Question.question.ilike(search_term)).all()
            formatted_questions = paginate_questions(request, questions)
            total_questions = Question.query.count()
        except:
            abort(422, description="Unexpected error accessing the database.")

        # abort with 404 if there are not any questions to return
        if len(questions) == 0:
            abort(404, description="There are no questions matching the searchTerm.")

        if len(formatted_questions) == 0:
            abort(404, description="There are no more questions matching the searchTerm.")

        return jsonify({
            'success': True,
            'questions': formatted_questions,
            'total_questions': total_questions,
            'current_category': None
        })

    # TEST: Search by any phrase. The questions list will update to include
    #  only question that include that string within their question.
    #  Try using the word "title" to start.

    # @TODO: DONE Create a GET endpoint to get questions based on category.
    @app.route('/categories/<category_id>/questions')
    def retrieve_questions_by_category(category_id):
        # Get a page of questions
        try:
            questions = Question.query.filter_by(category=category_id).order_by(Question.id).all()
            formatted_questions = paginate_questions(request, questions)
        except:
            abort(422, description="Unexpected error accessing the database.")

        # abort with 404 if there are not any questions to return
        if len(formatted_questions) == 0:
            abort(404, description="No questions match that search.")

        return jsonify({
            'success': True,
            'questions': formatted_questions
        })

    # TEST: In the "List" tab / main screen, clicking on one of the categories in the left column
    #  will cause only questions of that category to be shown.

    # @TODO: DONE Create a POST endpoint to get questions to play the quiz.
    # This endpoint should take category and previous question parameters and
    #  return a random questions within the given category,
    #  if provided, and that is not one of the previous questions.
    @app.route('/quizzes', methods=['POST'])
    def get_a_question():
        """ return a random questions within the given category """
        # get the category and any previous questions

        req_data = request.get_json()
        previous_questions = None
        if 'previous_questions' in req_data:
            previous_questions = req_data['previous_questions']

        quiz_category = None
        if 'quiz_category' in req_data:
            quiz_category = req_data['quiz_category']

        # previous_questions = request.json.get('previous_questions', None)
        # quiz_category = request.json.get('quiz_category', None)

        # if a category specified restrict questions to that category
        if quiz_category['id'] == 0:
            questions = Question.query.filter(Question.id.notin_(previous_questions)).all()
        else:
            questions = Question.query.filter_by(category=quiz_category['id']).filter(Question.id.notin_(previous_questions)).all()

        # return the random question if found
        questions_found = len(questions)
        if questions_found:
            question = Question.format(questions[random.randrange(0,questions_found)])
        else:
            question = None
        return jsonify({
            'success': True,
            'question': question
        })

    # TEST: In the "Play" tab, after a user selects "All" or a category,
    #  one question at a time is displayed, the user is allowed to answer
    #  and shown whether they were correct or not.

    # @TODO: DONE Create error handlers for all expected errors including 404 and 422.
    @app.errorhandler(400)
    def not_found_error_json(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(404)
    def not_found_error_json(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": str(error)
        }), 404

    @app.errorhandler(405)
    def method_not_allowed_error_json(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method Not Allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable_error_json(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": str(error)
        }), 422

    @app.errorhandler(500)
    def internal_error_json(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Error"
        }), 500

    return app
