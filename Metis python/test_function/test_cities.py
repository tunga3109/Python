#стр 229 упр 11.1,11.2
import unittest
from city_functions import county_city


class CityNameCase(unittest.TestCase): #!!!!

    def test_city_country(self):
        formatted_city = county_city('vietnam','hanoi')
        self.assertEqual(formatted_city,'Vietnam,Hanoi') #!!!!!
    
    def test_city_country_population(self):
        formatted_population = county_city('vietnam','hanoi','500000')
        self.assertEqual(formatted_population,'Vietnam,Hanoi - Population 500000')


if __name__ == '__main__': #!!!!
    unittest.main()
