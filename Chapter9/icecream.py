from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors
    def allFlavors(self):
        print("Our ice cream stand has the following flavors:")
        for flav in self.flavors:
            print(flav)