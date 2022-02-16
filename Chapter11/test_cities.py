import unittest
from city_functions import prettyCity

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        """Do cities like 'Santiago, Chile' work?"""
        city = prettyCity('santiago','chile')
        self.assertEqual(city,'Santiago, Chile')
    
    def test_city_country_population(self):
        """Does the function work when users add optional population parameter?"""
        city = prettyCity('santiago','chile',population=5000000)
        self.assertEqual(city, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()