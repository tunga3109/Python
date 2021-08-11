import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        """Имена вида 'Janis Joplin' работают правильно?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_middle_name(self):
        formatted_name = get_formatted_name('Chan', 'Tung', 'Dinh')
        self.assertEqual(formatted_name, 'Chan Dinh Tung')

if __name__ == '__main__':
    unittest.main()