print("=========================Exercise 9-1========================")
class Restaurant:
    """A class representing restaurants and the cuisine they serve"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes describing a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Return info about a restaruant"""
        descrip = f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} cuisine"
        print(descrip)
    
    def open_restaurant(self):
        """Print message announcing that the restaurant is open"""
        opener = f"{self.restaurant_name.title()} is open"
        print(opener)
    
rest1 = Restaurant("Funistrada","Italian")
print("New Restaurant Created:\n")
print(f"Restaurant = {rest1.restaurant_name}")
print(f"Cuisine = {rest1.cuisine_type}")
rest1.describe_restaurant()
rest1.open_restaurant()
print("\n=====================Exercise 9-2========================")

rest2 = Restaurant("Hexenbelle","Vegetarian")
rest3 = Restaurant("Taj Mahal","Indian")
rest1.describe_restaurant()
rest2.describe_restaurant()
rest3.describe_restaurant()

    