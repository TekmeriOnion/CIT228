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