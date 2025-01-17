class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
    
    def eat_treat(self, treat):
        self.happiness += treat.deliciousness
        self.fullness += treat.satiety

    def eat_food(self):
        self.fullness += 30
        print("%s eagerly scarfs up all the food you gave them. They seem less hungry!" % (self.name))

    def get_love(self):
        self.happiness += 30
        print("You gently patted %s on their head. They seem happier!" % (self.name))

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
        
    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        """ % (self.name, self.fullness, self.happiness)


class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level

    def be_alive(self):
        super().be_alive()
        self.happiness -= self.mopiness/2

    def cuddle(self, other_pet):
        # Super cuddle powers, activate!
        for i in range(self.cuddle_level):
            other_pet.get_love()
            
    def __str__(self):
        return "Extra Cuddly"
    

