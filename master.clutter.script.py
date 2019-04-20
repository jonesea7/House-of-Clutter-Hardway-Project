#establish rand int library, include other libraries from the exercise
from random import randint

#BATHROOM
def bathroom():
    print("You slowly open the door to reveal...Unholy Crap!\n ...no, literally it is a poop demon! It devours you and your soul.\n Game Over.")

#BEDROOM
def pile_num_loop():
    print("Stinky filth.")
    print("Continue searching (choose pile: 1-8 or leave the mess alone?")

    pile_num = input("> ")
    
    if "2" in pile_num:
        print("Your efforts have paid off. You found $20 in a pocket.")
        #send player back to the hallway
    else:
        print("The smell is overwhelming. Continue or give up this disgusting search.")
        
        choice = input('> ')
        if "Continue" in choice:
            pile_num_loop()
        else:
            print("After you barf, you decide to call it quits and return to the hallway.")
            hallway()
    

def bedroom():
    print('''Pushing open the damaged door reveals
    eight piles of smelly dirty laundry surrounding the king size bed against the south wall.
    Do you:
    Rummage for treasure...
    or
    Leave immediately, the stench is overwhelming.''')

    decision = input('> ')

    if 'rummage' in decision or 'treasure' in decision:
        print('You choose to brave the mildewy masses for treasure.')
        print('Which pile do you choose: 1-8.')

        pile_num = input('> ')
        if "2" in pile_num:
            print("Hooray, you found twenty dollars in the pocket of some overalls.")
            #return the player to the hallway
        else:
            print("Stinking filth.")
            print("Continue or call it quits.")

            choice = "> "

            if "quit" in choice:
                print("This is to gross to go on, you decide.")

            elif 'continue' in choice:
                print("Apparently you're a sucker for punishment.")
                pile_num_loop()

            else: 
                print('You\'re mind melts into mush and you can seem to make clear decisions. \n Game Over.')

#bedroom()   
#KITCHEN
def kitchen():
    print("""Behind the door is a kitchen. To your immediate left is a large pile of dishes.
    You try to walk cautiously into the space, but the disturbance of your movment causes the dishes to tumble all over you. 
    A coffee mug with the image of a sparrow is lodged into your jugular. You die slowly...slowly. \n Game Over.""")

#TEEN ROOM

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
        print('You try to leave, but you can never unsee what you have witnessed. Madness takes you over. \n Game Over.')


#teenroom()

#KIDS ROOM
def kids_room():
    print("""At the end of the hallway to the your left appears to be a playroom.
    You enter and see stacks of what appear to be toy boxes, books and various gaming consoles.
    To your right in the room is a massive bookshelf.
    To your left  six toy boxes stacked high.
    In front of you is a massive television connected to seven different gaming consoles.
    You decide to explore:
    The bookshelf
    The toy boxes
    The gaming set""")

    #add exit room as an option when adding to the rest of the script

    choice = input("> ")

    def reset_kids_room():
        print("You decide to do something else.")

        choice = input ('> ')
        
        if 'bookshelf' in choice:
            bookshelf()
    
        if 'toy' in choice:
            toy_boxes()

        if 'gaming' or 'setup' in choice:
            gaming_setup()
        else:
            print("You're confused by the chaos of the room and decide to leave it all alone.")
            hallway_thresholds()


    def bookshelf():
        print("The shelf appears to be unstable.")
        print("Explore or leave.")

        choice_bookshelf = input("> ")

        if "explore" in choice_bookshelf:
            print("You grab a book, and the entire shelf falls on you. \n Game Over.")

        elif 'leave' in choice_bookshelf:
            reset_kids_room()

    def toy_boxes():
        print("The toy boxes are bright and colorful. They appear unstable.")
        print("Explore or leave.")

        choice_toys = input("> ")

        if 'explore' in choice_toys:
            print("The boxes topple over and crush you. \n Game Over.")

        elif 'leave' in choice_toys:
            reset_kids_room()

    def gaming_setup():
        print("The gaming setup is too glorious to resist. You begin playing and never stop. \n Game Over.")

    if 'bookshelf' in choice:
        bookshelf()
    
    if 'toy' in choice:
        toy_boxes()

    if 'gaming' in choice:
        gaming_setup()

#kids_room()

    
#HALLWAY (don't forget to run all the other functions of the individual rooms.)
    #teenroom()
    #kids_room()

def hallway_thresholds():
    print("""You stand before the five choices in front of you. All doors are closed. Anything can be behind them.
    There are two doors to your right, and three doors to your left. 
    Clockwise from your perspective the doors are oddly labeled as follows:
    Mommy, Junior, Rebel, Poop, Endless Dishes. Which path you choose?""")

    hallway_thresholds_choice = input('> ')

    if 'mommy' in hallway_thresholds_choice:
        print("Let us see what mother has to hide.")
        bedroom()

    elif 'junior' in hallway_thresholds_choice or 'jr' in hallway_thresholds_choice:
        print("What does the child have to show us?")
        kids_room()

    elif 'rebel' in hallway_thresholds_choice:
        print('You sense a way out is here. You proceed through the creaky door.')
        teenroom()

    elif 'poop' in hallway_thresholds_choice:
        print('You enjoyed typing poop, didn\'t you?')
        bathroom()

    elif 'dishes' in hallway_thresholds_choice or 'endless' in hallway_thresholds_choice:
        print('You walk through the threshold to your immediate right. Will it be the right choice?')
        kitchen()
    
    else:
        print('Clarity is vital in the game of life, the house does not understand your intent. \n Game Over')



def hallway():
    print("""
    The hallway in front of you is made ever more narrow by several boxes and bags along side the eastern wall of the hall.

    You also notice five thresholds. Two doorways are on the west side of the hallway, one on the north, and two on the east.

    Do you explore or ignore the boxes and bags on the hall floor in front of you?""")

    choice_hall = input("> ")

        

    def hallway_reset():
        print("You stand back and reassess the situation. Do you go the thresholds or search the containers once more.")

        choice_reset = input("> ")

        if 'doorway' in choice_reset or 'threshold' in choice_reset:
            print('You decide to see what other mysteries lie before you in this home of hoarding.')
            hallway_thresholds()
            #add options for each threshold here (kidsroom, bedroom, teenroom, bathroom, kitchen)
        elif 'search' in choice_reset or 'containers' in choice_reset:
            print('Boxes. Bags. What will it be?')

            choice_reset_again = input('> ')

            if 'box' in choice_reset_again:
                boxes()
            elif 'bag' in choice_reset_again:
                bags()
            else:
                print("Madness overwhelms you from all of the clutter. \n Game Over.")
        else:
            print('You stand in awe of the junk and waste away wondering how this could happen. \n Game Over.')

    def bags():
        print('Old shopping bags from Whole Foods pile up on top of the boxes.')
        print('Explore or leave them be.')

        choice_bags = input('> ')

        if 'explore' in choice_bags:
            print('Old moldy, half-eaten produce. Mold spores fill the air and your lungs. \n Game Over.')
        else:
            hallway_reset()


    def boxes():
        print("The boxes are sealed tightly with lots of tape. Perhaps you require a tool to open them.")
        print('Look for a tool or leave the boxes be?')

        choice_boxes = input('> ')

        if 'tool' in choice_boxes or 'look' in choice_boxes:
            print("You see a pair of rusty scissors and decide to use them to open the boxes.")

            dice_roll = randint(1,20)

            if dice_roll >= 10:
                print('You open the box successfully and find it is full of hair care products.')
            else:
                print("The scissors don't agree with your hands and you accidently slice open a major artery, and bleed out. \n Game Over.")

        else:
            hallway_reset()

        choice_boxes = input


    if 'explore' in choice_hall:
        print(" 'Let's take a look', you think to yourself.")
        print('There are three boxes and four bags of items to your immediate right.')
        print('You also have five thresholds before you.')
        print('Doorways, boxes, or bags?')

        choice_hall_stuff = input('> ')

        if 'door' in choice_hall_stuff:
            hallway_thresholds()

        if 'box' in choice_hall_stuff:
            boxes()
        
        if 'bag' in choice_hall_stuff:
            bags()

    elif 'ignore' in choice_hall:
        print("You're ready to see what else is in store in this madhouse of mess.")
        hallway_thresholds()


    else:
        print('You stand in awe of the junk and waste away wondering how this could happen. \n Game Over.')

#hallway()

#LIVING ROOM

def living_room():
    print("""
    Inside is a large room stacked from floor to ceiling with couches. Nothing but couches. 
    Apart from the legos on the floor, there is nothing in the room but couches...
    
    ... and a narrow path.

    You follow the narrow path to a hallway.""")
    hallway()

#START

def start():
    print("""
    You walk up to the doorstep of an eerie home
    on the eastside of Detroit. The door is ajar and you push it open.
    Inside the smell of old shoes assaults your nose. There is a giant wall 
    directly in front of you. To your left is a small step. Do you:
    Walk up the step and explore? 
    or
    Pull out your cell phone and use it as a flashlight?""")

    choice = input('> ')

    if 'walk' in choice or "explore" in choice:
        print("You step on a pile of legos and trip and break your a finger. The pain is amazing, but you soldier on.")
        living_room()
    elif choice == "look" or choice == "flashlight" or choice == "phone" or choice == "cell":
        print("You see a dangerous pile of loose legos on the floor. You decide to proceed with caution.")
        living_room()

start() 
#EXECUTE START FUNCTION