from cuddly_pet import Pet, CuddlyPet
from treat import Treat, Bacon, ColdPizza, VeganSnack

pets = []

def pet_timer():
    for animal in pets:
        animal.be_alive()
        

def pet_adopter():
    
    active = True
    while active == True:
        cuddly_or_no = input("""
Choose a type:
1. Regular
2. Cuddly
""") 
        if cuddly_or_no == "Regular" or cuddly_or_no == "1":
            namer = input("Let's give it a name: ")
            pets.append(Pet(namer))
            print("""
Congratulations on adopting %s
""" % (namer))
            active = False
        elif cuddly_or_no == "Cuddly" or cuddly_or_no == "2":
            namer = input("Let's give it a name: ")
            pets.append(CuddlyPet(namer))
            print("""
Congratulations on adopting %s
""" % (namer))
            active = False
        else:
            print("""
I'm sorry, that's not a valid answer.
Try again.
""")

def give_treat(thepet):
    treat_give = input("""Which treat do you want?
1. ColdPizza
2. Bacon
3. VeganSnack
""")
    if treat_give == "ColdPizza":
        thepet.eat_treat(ColdPizza)
    elif treat_give == "Bacon":
        thepet.eat_treat(Bacon)
    elif treat_give == "VeganSnack":
        thepet.eat_treat(VeganSnack)
    else:
        "That is not a valid response"
        

    
def pet_simulator():
    pets_on = True
    while pets_on == True:
        pet_sim = input("""
Please choose an option:
1. Adopt a pet (Adopt)
2. Play with a pet (Play)
3. Feed a pet (Feed)
4. Give a treat (Treat)
5. Check status of pets (Status)
6. Do nothing (Wait)
7. Exit
""")
        if pet_sim == "Adopt" or pet_sim == "1":
            pet_adopter()
        elif pet_sim == "Play" or pet_sim == "2":
            print(pets)
            play_mate = input("Which pet do you want to play with?")
            if not play_mate in pets:
                print("There's no pet by that name")
            else:
                play_mate.get_love()
                pet_timer()
        elif pet_sim == "Feed" or pet_sim == "3":
            print(pets)
            hungry_boi = input("Which pet are you feeding?")
            if not hungry_boi in pets:
                print("There is no pet by that name")
            else:
                hungry_boi.eat_food()
                pet_timer()
        elif pet_sim == "Treat" or pet_sim == "4":
            print(pets)
            good_boi = input("Who gets the treat?")
            give_treat(good_boi)
        elif pet_sim == "Status" or pet_sim == "5":
            for animal in pets:
                print(""" 
""", animal.name, animal.fullness, animal.happiness)
        elif pet_sim == "Wait" or pet_sim == "6":
            pet_timer()
        elif pet_sim == "Exit" or pet_sim == "7":
            break
        else:
            print("""
I'm sorry, that's not a valid answer. Try again.
""")
                
                    
pet_simulator()
            
            
            
    