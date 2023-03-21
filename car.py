from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, registration, weight):
        super().__init__(registration, weight)

    def Calculcate_Fee(self):
        pass


car1 = Car("ABCD", 300)
print(car1.registration)