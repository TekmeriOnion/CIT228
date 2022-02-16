import unittest
from restaurant import Restaurant

class TestRestaurant(unittest.TestCase):
    """Unit Tests for Restaurant class"""
    
    def setUp(self):
        restaurant_name="Sal's Diner"
        cuisine_type="American casual"
        number_served=50
        self.restaurant = Restaurant(restaurant_name,cuisine_type,number_served)

    def test_set_number_served(self):
        self.restaurant.set_number_served()
        self.assertEqual(self.restaurant.number_served, 100)
    
    def test_increment_number_served(self):
        self.restaurant.increment_number_served()
        self.assertEqual(self.restaurant.number_served,65)

if __name__ == '__main__':
    unittest.main()