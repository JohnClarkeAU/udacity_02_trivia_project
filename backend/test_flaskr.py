""" Trivia Testing Suite """
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question': 'What colour is the sky',
            'answer': 'Blue',
            'difficulty': '1',
            'category': '1'
        }

        self.new_search = {
            'searchTerm': 'What'
        }

        self.new_quiz = {
            "previous_questions": [21,31,34],
            "quiz_category": {"type":"Science","id":1}
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        # db.session.close() # is this required??
        pass

    """
    Tests for each successful operation and for expected errors.
    """
    def test_index(self):
        ''' GET the home page just to ensure that the system is up and running OK '''
        res = self.client().get('/')
        data = (res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, b'Hello\r\n')

    def test_retrieve_categories(self):
        ''' GET requests for all available categories '''
        res = self.client().get('/categories')
        data = json.loads(res.data)
        categories = Category.query.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['categories']))
        self.assertEqual(len(data['categories']), len(categories))

        i = 0
        dat = list(data['categories'].items())
        for category in categories:
            self.assertEqual(dat[i][0], str(category.id))
            self.assertEqual(dat[i][1], category.type)
            i = i+1


    def test_retrieve_questions(self):
        ''' GET a page of questions and all the categories '''
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])

        self.assertTrue(len(data['categories']))
        self.assertEqual(data['current_category'], None)

    def test_retrieve_questions_past_the_end(self):
        ''' GET a page of questions and all the categories should return 404 if page number past the end '''
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "404 Not Found: There are no questions on that page.")

    def test_delete_question(self):
        ''' DELETE question using a valid question ID '''
        question = Question.query.first()
        url = '/questions/' + str(question.id)

        res = self.client().delete(url)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], str(question.id))

        updatedquestion = Question.query.filter(Question.id == question.id).one_or_none()
        self.assertEqual(updatedquestion, None)


    def test_delete_question_returns_404_if_question_does_not_exist(self):
        ''' DELETE question using a question ID check it returns 404 if the question does not exist '''
        res = self.client().delete('/questions/99999')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "404 Not Found: Question ID does not exist.")

    def test_put_new_question(self):
        q = self.new_question
        res = self.client().put('/questions', json=q)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_put_new_question_blank_question_422(self):
        q = self.new_question
        q['question'] = ''
        res = self.client().put('/questions', json=q)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "422 Unprocessable Entity: None of the fields may be blank.")

    def test_put_new_question_blank_answer_422(self):
        q = self.new_question
        q['answer'] = ''
        res = self.client().put('/questions', json=q)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "422 Unprocessable Entity: None of the fields may be blank.")

    def test_put_new_question_blank_difficulty_422(self):
        q = self.new_question
        q['difficulty'] = ''
        res = self.client().put('/questions', json=q)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "422 Unprocessable Entity: None of the fields may be blank.")

    def test_put_new_question_blank_category_422(self):
        q = self.new_question
        q['category'] = ''
        res = self.client().put('/questions', json=q)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "422 Unprocessable Entity: None of the fields may be blank.")

    def test_put_new_question_difficulty_out_of_range_0_422(self):
        q = self.new_question
        q['difficulty'] = 0
        res = self.client().put('/questions', json=q)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "422 Unprocessable Entity: The difficulty must be between 1 and 5 inclusive.")

    def test_put_new_question_difficulty_out_of_range_6_422(self):
        q = self.new_question
        q['difficulty'] = 6
        res = self.client().put('/questions', json=q)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "422 Unprocessable Entity: The difficulty must be between 1 and 5 inclusive.")

    def test_put_new_question_category_out_of_range_7_422(self):
        q = self.new_question
        q['category'] = 7
        res = self.client().put('/questions', json=q)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "422 Unprocessable Entity: The category specified does not exist.")

    def test_search_questions(self):
        s = self.new_search
        s['searchTerm'] = "what"
        res = self.client().post('/questions', json=s)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertEqual(data['total_questions'], Question.query.count() )
        self.assertEqual(data['current_category'], None)

    def test_search_questions_not_found(self):
        s = self.new_search
        s['searchTerm'] = "zzz"
        res = self.client().post('/questions', json=s)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_retrieve_questions_by_category_0_error_404(self):
        res = self.client().get('/categories/0/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "404 Not Found: No questions match that search.")

    def test_retrieve_questions_by_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])

    def test_retrieve_quiz_question_by_category(self):
        z = self.new_quiz
        z['previous_qustions'] = [21,31,34]
        z['quiz_category'] = {"type":"Science","id":1}

        res = self.client().post('/quizzes', json=z)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])

    def test_retrieve_quiz_question_for_all_categories(self):
        z = self.new_quiz
        z['previous_qustions'] = []
        z['quiz_category'] = {"type":"click","id":0}
        res = self.client().post('/quizzes', json=z)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
