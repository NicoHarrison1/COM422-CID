from vehicle import Vehicle

class Lorry(Vehicle):
    def __init__(self, registration, weight):
        super().__init__(registration, weight)

    def Calculcate_Fee(self):
        pass
