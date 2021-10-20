class Car:

    # create class attributes
    car_count = 0

    # create class methods
    def start(self, name, make, model):
        print("Engine started")
        self.name = name
        self.make = make
        self.model = model
        # Call class attribute
        Car.car_count += 1
    @staticmethod
    def get_class_details():
        print ("This is a car class")


Car.get_class_details()

# Class vs Instance Attributes
