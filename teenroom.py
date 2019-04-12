
def explore_teen_room():
    print("Where will you start? Bed, dresser, closet.")

    explore_choice = input("> ")

    if 'bed' in explore_choice:
        print("You observe the a filthy mattress covered in various liquid spots. You hurl so much that it actually kills you. \n Game Over.")
    elif 'dresser' in explore_choice:
        print('The drawers are completely empty. You realize all of the clothes are actually on the floor. You wonder what will become of humanity. \n Game Over.')
    elif 'closet' in explore_choice:
        print('Big mistake. \n Game Over.')



def teenroom():
    print("""You open the door and the smell of corn chips, old pizza, and b.o. assaults your nose.
    Video game cases, empty fast food containers, and a moldy cup of what appears to be milk adorn the room.
    Explore, clean, or exit?""")

    teen_room_choice = input("> ")

    if 'explore' in teen_room_choice:
        print("You are a brave soul indeed. You decide to snoop around.")
        explore_teen_room()

    elif 'clean' in teen_room_choice:
        print("Your benevolence and self-sacrifice is greatly rewarded. You fight through the turmoil and obtain Nirvana. \n Congratulations, You Win!")
        print("""--CREDITS--
        Story Edmund Alyn Jones
        Concept Edmund Alyn Jones
        Music Edmund Alyn Jones
        Script Supervisor Edmund Alyn Jones
        Q&A Edmund Alyn Jones
        Programmer Edmund Alyn Jones
        Special Thanks:
        Me
        Myself 
        I
        
        Thanks for Playing""")

    elif 'exit' in teen_room_choice:
        print('You try to leave, but you can never unsee what you have witness. Madness takes you over. \n Game Over.')


#teenroom()
