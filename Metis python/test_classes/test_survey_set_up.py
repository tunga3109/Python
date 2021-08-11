import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    """Тесты для класса AnonymousSurvey."""
    def setUp(self):
        """
        Создание опроса и набора ответов для всех тестовых методов.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.response = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Проверяет, что один ответ сохранен правильно."""
        self.my_survey.add_response(self.response[0])
        self.assertIn(self.response[0], self.my_survey.response)

    def test_store_three_responses(self):
        """Проверяет, что три ответа были сохранены правильно."""
        for response in self.response:
            self.my_survey.add_response(response)
        for response in self.response:
            self.assertIn(response, self.my_survey.response)


if __name__ == '__main__':
    unittest.main()