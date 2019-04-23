#establish rand int library, include other libraries from the exercise
from random import randint

#BATHROOM
def bathroom():
    print("You slowly open the door to reveal...Unholy Crap!\n ...no, literally it is a poop demon! It devours you and your soul.\n Game Over.")

#BEDROOM
def pile_num_loop():
    print("Stinky filth.")
    print("""Continue searching 
    choose a pile: write a number between 1-8 
    or 
    LEAVE""")

    pile_num = input("> ")
    
    if "2" in pile_num:
        print("Your efforts have paid off. You found $20 in a pocket.")
        #send player back to the hallway
    else:
        print("The smell is overwhelming. CONTINUE or give up this disgusting search.")
        
        choice = input('> ')
        if "CONTINUE" in choice:
            pile_num_loop()
        else:
            print("After you barf, you decide to call it quits and return to the hallway.")
            hallway()
    

def bedroom():
    print('''
    Pushing open the damaged door reveals
    eight piles of smelly dirty laundry surrounding the king size bed against the south wall.
    
    Do you:
    
    RUMMAGE for treasure...
    or
    LEAVE immediately, the stench is overwhelming.''')

    decision = input('> ')

    if 'RUMMAGE' in decision or 'treasure' in decision:
        print('You choose to brave the mildewy masses for treasure.')
        print('Which pile do you choose: 1-8.')

        pile_num = input('> ')
        if "2" in pile_num:
            print("Hooray, you found twenty dollars in the pocket of some overalls.")
            #return the player to the hallway
        else:
            print("Stinking filth.")
            print("CONTINUE or QUIT.")

            choice = "> "

            if "QUIT" in choice:
                print("This is to gross to go on, you decide.")

            elif 'CONTINUE' in choice:
                print("Apparently you're a sucker for punishment.")
                pile_num_loop()

            else: 
                print('You\'re mind melts into mush and you can seem to make clear decisions. \n Game Over.')

#bedroom()   
#KITCHEN
def kitchen():
    print("""
    Behind the door is a kitchen. 
    
    To your immediate left is a large pile of dishes.

    You try to walk cautiously into the space, but the disturbance of your movment causes the dishes to tumble all over you. 
    A coffee mug with the image of a sparrow is lodged into your jugular. You die slowly...slowly. \n Game Over.""")

#TEEN ROOM

def explore_teen_room():
    print("Where will you start? BED, DRESSER, CLOSET.")

    explore_choice = input("> ")

    if 'BED' in explore_choice:
        print("You observe the a filthy mattress covered in various liquid spots. You hurl so much that it actually kills you. \n Game Over.")
    elif 'DRESSER' in explore_choice:
        print('The drawers are completely empty. You realize all of the clothes are actually on the floor. You wonder what will become of humanity. \n Game Over.')
    elif 'CLOSET' in explore_choice:
        print('Big mistake. \n Game Over.')



def teenroom():
    print("""
    You open the door and the smell of corn chips, old pizza, and b.o. assaults your nose.

    Video game cases, empty fast food containers, and a moldy cup of what appears to be milk adorn the room.
    EXPLORE, CLEAN, or EXIT?""")

    teen_room_choice = input("> ")

    if 'EXPLORE' in teen_room_choice:
        print("You are a brave soul indeed. You decide to snoop around.")
        explore_teen_room()

    elif 'CLEAN' in teen_room_choice:
        print("Your benevolence and self-sacrifice is greatly rewarded. You fight through the turmoil and obtain Nirvana. \n Congratulations, You Win!")
        print("""
                                    --CREDITS--
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
        
                                THANKS FOR PLAYING""")

    elif 'EXIT' in teen_room_choice:
        print('You try to leave, but you can never unsee what you have witnessed. Madness takes you over. \n Game Over.')


#teenroom()

#KIDS ROOM
def kids_room():
    print("""
    At the end of the hallway to the your left appears to be a playroom.
    You enter and see stacks of what appear to be toy boxes, books and various gaming consoles.
    
    To your right in the room is a massive bookshelf.
    To your left  six toy boxes stacked high.
    
    In front of you is a massive television connected to seven different gaming consoles.
    
    You decide to explore:
    The BOOKSHELF
    The toy BOXES
    The gaming SET""")

    #add exit room as an option when adding to the rest of the script

    choice = input("> ")

    def reset_kids_room():
        print("You decide to do something else.")

        choice = input ('> ')
        
        if 'BOOKSHELF' in choice:
            bookshelf()
    
        if 'BOXES' in choice:
            toy_boxes()

        if 'GAMING' or 'SET' in choice:
            gaming_setup()
        else:
            print("You're confused by the chaos of the room and decide to leave it all alone.")
            hallway_thresholds()


    def bookshelf():
        print("The shelf appears to be unstable.")
        print("EXPLORE or LEAVE.")

        choice_bookshelf = input("> ")

        if "EXPLORE" in choice_bookshelf:
            print("You grab a book, and the entire shelf falls on you. \n Game Over.")

        elif 'LEAVE' in choice_bookshelf:
            reset_kids_room()

    def toy_boxes():
        print("The toy boxes are bright and colorful. They appear unstable.")
        print("EXPLORE or LEAVE.")

        choice_toys = input("> ")

        if 'EXPLORE' in choice_toys:
            print("The boxes topple over and crush you. \n Game Over.")

        elif 'LEAVE' in choice_toys:
            reset_kids_room()

    def gaming_setup():
        print("""The gaming setup is too glorious to resist. 
        You begin playing and never stop. \n Game Over.""")

    if 'BOOKSHELF' in choice:
        bookshelf()
    
    if 'BOXES' in choice:
        toy_boxes()

    if 'SET' in choice:
        gaming_setup()

#kids_room()

    
#HALLWAY (don't forget to run all the other functions of the individual rooms.)
    #teenroom()
    #kids_room()

def hallway_thresholds():
    print("""
    You stand before the five choices in front of you. 
    
    All doors are closed. 
    
    Anything can be behind them.

    There are two doors to your right, and three doors to your left. 

    Clockwise from your perspective the doors are oddly labeled as follows:

    MOMMY
    JUNIOR
    REBEL
    POOP
    Endless DISHES

    Which path you choose?""")

    hallway_thresholds_choice = input('> ')

    if 'MOMMY' in hallway_thresholds_choice:
        print("Let us see what mother has to hide.")
        bedroom()

    elif 'JUNIOR' in hallway_thresholds_choice or 'jr' in hallway_thresholds_choice:
        print("What does the child have to show us?")
        kids_room()
 
    elif 'REBEL' in hallway_thresholds_choice:
        print('You sense a way out is here. You proceed through the creaky door.')
        teenroom()

    elif 'POOP' in hallway_thresholds_choice:
        print('You enjoyed typing poop, didn\'t you?')
        bathroom()

    elif 'DISHES' in hallway_thresholds_choice or 'endless' in hallway_thresholds_choice:
        print('You walk through the threshold to your immediate right. Will it be the right choice?')
        kitchen()
    
    else:
        print('Clarity is vital in the game of life, the house does not understand your intent. \n Game Over')



def hallway():
    print("""
    The hallway in front of you is made ever more narrow by several boxes and bags along side the eastern wall of the hall.

    You also notice five thresholds. Two doorways are on the west side of the hallway, one on the north, and two on the east.

    Do you EXPLORE or IGNORE the boxes and bags on the hall floor in front of you?""")

    choice_hall = input("> ")

        

    def hallway_reset():
        print("""You stand back and reassess the situation. 
        
        Do you:
        
        Go the DOORWAYS or SEARCH the containers once more.""")

        choice_reset = input("> ")

        if 'DOORWAYS' in choice_reset or 'threshold' in choice_reset:
            print('You decide to see what other mysteries lie before you in this home of hoarding.')
            hallway_thresholds()
            #add options for each threshold here (kidsroom, bedroom, teenroom, bathroom, kitchen)
        elif 'SEARCH' in choice_reset or 'containers' in choice_reset:
            print('BOXES. BAGS. What will it be?')

            choice_reset_again = input('> ')

            if 'BOXES' in choice_reset_again:
                boxes()
            elif 'BAGS' in choice_reset_again:
                bags()
            else:
                print("Madness overwhelms you from all of the clutter. \n Game Over.")
        else:
            print('You stand in awe of the junk and waste away wondering how this could happen. \n Game Over.')

    def bags():
        print('Old shopping bags from Whole Foods pile up on top of the boxes.')
        print('EXPLORE or LEAVE them be.')

        choice_bags = input('> ')

        if 'EXPLORE' in choice_bags:
            print('Old moldy, half-eaten produce. Mold spores fill the air and your lungs. \n Game Over.')
        else:
            hallway_reset()


    def boxes():
        print("The boxes are sealed tightly with lots of tape. Perhaps you require a tool to open them.")
        print('LOOK for a tool or LEAVE the boxes be?')

        choice_boxes = input('> ')

        if 'tool' in choice_boxes or 'LOOK' in choice_boxes:
            print("You see a pair of rusty scissors and decide to use them to open the boxes.")

            dice_roll = randint(1,20)

            if dice_roll >= 10:
                print('You open the box successfully and find it is full of hair care products.')
            else:
                print("The scissors don't agree with your hands and you accidently slice open a major artery, and bleed out. \n Game Over.")

        else:
            hallway_reset()

        choice_boxes = input


    if 'EXPLORE' in choice_hall:
        print(" 'Let's take a look', you think to yourself.")
        print('There are three boxes and four bags of items to your immediate right.')
        print('You also have five thresholds before you.')
        print('DOORS, BOXES, or BAGS?')

        choice_hall_stuff = input('> ')

        if 'DOORS' in choice_hall_stuff:
            hallway_thresholds()

        if 'BOXES' in choice_hall_stuff:
            boxes()
        
        if 'BAGS' in choice_hall_stuff:
            bags()

    elif 'IGNORE' in choice_hall:
        print("You're ready to see what else is in store in this madhouse of mess.")
        hallway_thresholds()


    else:
        print('You stand in awe of the junk and waste away wondering how this could happen. \n Game Over.')

#hallway()

#LIVING ROOM

def living_room():
    print("""
    A slither of light shines from a crack in the ceiling.

    You are in, what appears, to be a small living room.

    From floor to ceiling the room is stacked with... 
    
    
    ...couches. 
    
    
    Nothing but couches. 

    Apart from the legos on the floor, there is nothing in the room but couches...
    
    ... and a narrow path.

    You follow the narrow path to a hallway.""")
    hallway()

#START

def start():
    print("""
    ********* WELCOME TO THE HOUSE OF HOARDING **********

                         A
                         SURVIVAL
                         HORROR
                         CHOOSE YOUR ADVENTURE
                         BY
                         EDMUND ALYN JONES

                         DA' RULES
            1. READ
            2. YOUR OPTIONS ARE IN ALL CAPS
            3. WRITE THE YOUR SELECTION IN ALL CAPS
            4. EXPLORE THE HORROR OF HOARDING

                THANKS FOR PLAYING!!!

    You walk up to the doorstep of an eerie home.
    The door is ajar and you push it open.
    *WHOOSH* 
    An intense chill and the musty odor of old shoes assaults your nose. 
    There is a giant wall directly in front of you. 
    To your left is a small step. 
    The room is quite dark.
    
    Do you:

    EXPLORE
    or
    USE your phone for light.\n""")

    choice = input('> ')

    if "EXPLORE" in choice:
        print("You step on a pile of legos and bruise your arm. The pain is amazing, but you soldier on.")
        living_room()
    elif choice == 'USE':
        print("You see a dangerous pile of loose legos on the floor. You decide to proceed with caution.")
        living_room()

start() 
#EXECUTE START FUNCTION