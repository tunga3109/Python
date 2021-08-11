import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase):

    def test_test_store_single_response(self):
        question = 'What is your favorite sport?'
        my_survey = AnonymousSurvey(question)
        my_survey.add_response('Tennis')
        self.assertIn('Tennis',my_survey.response)
    
    def test_store_three_response(self):
        question = 'What is your favorite sport?'
        my_survey = AnonymousSurvey(question)
        responses = ['tennis','footbal','rugby']
        for response in responses:
            my_survey.add_response(response)
        for response in responses:
            self.assertIn(response,my_survey.response)


if __name__ == '__main__':
    unittest.main()