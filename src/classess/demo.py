class Demo:
    def __init__(self):
        pass
    
    def is_odd_number(self,number = int) ->str:
        result = f"{number} is Odd"
        if (number % 2) == 0:
            result = f"{number} is Even"
        return result