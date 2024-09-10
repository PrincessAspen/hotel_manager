class Treat:
    def __init__ (self, satiety, deliciousness):
        self.satiety = satiety
        self.deliciousness = deliciousness
        
class ColdPizza(Treat):
    def __init__(self):
        super().__init__(5, 20)
        
class Bacon(Treat):
    def __init__(self):
        super().__init__(10, 10)
        
class VeganSnack(Treat):
    def __init__(self):
        super().__init__(20, 5)