print("=========================Exercise 9-4========================")
class Restaurant:
    """A class representing restaurants and the cuisine they serve"""
    def __init__(self, restaurant_name, cuisine_type,number_served=0):
        """Initialize attributes describing a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        """Return info about a restaruant"""
        descrip = f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} cuisine"
        print(descrip)
    
    def set_number_served(self):
        """Update total number of customers served"""
        served = int(input("How many customers have been served today?"))
        self.number_served = served

    def increment_number_served(self):
        """Increment number of customers served"""
        served = int(input("How many additional customers have been served?"))
        self.number_served += served

    def open_restaurant(self):
        """Print message announcing that the restaurant is open"""
        opener = f"{self.restaurant_name.title()} is open"
        print(opener)
    
rest1 = Restaurant("Funistrada","Italian",47)
# retrieving initial number of customers served
print(f"The starting number of customers served is {rest1.number_served}")
# updating number of customers served
rest1.number_served = 103
print(f"The updated count of customers served is {rest1.number_served}")
# updating number of customers served using set_number_served
rest1.set_number_served()
print(f"The updated count of customers served is now {rest1.number_served}")
# incrementing total customers served w/ user input
rest1.increment_number_served()
print(f"The incremented total of customers served is {rest1.number_served}")