#add this to the master code at the top

from random import randint

def hallway():
    print("""You observe a fairly short, and narrow hallway in front of you.
    Along one side of the hall are several boxes and bags.
    You notice five thresholds. Two doorways are on the west side of the hallway, one on the north, and two on the east.
    Do you explore or ignore the boxes and bags on the hall floor in front of you?""")

    choice_hall = input("> ")

        

    def hallway_reset():
        print("You stand back and reassess the situation. Do you go the thresholds or search the containers once more.")

        choice_reset = input("> ")

        if 'doorway' in choice_reset or 'threshold' in choice_reset:
            print('You decide to see what other mysteries lie before you in this home of hoarding.')
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
        print('There are three boxes and four bags of items.')
        print('Boxes or bags?')

        choice_hall_stuff = input('> ')

        if 'box' in choice_hall_stuff:
            boxes()
        
        if 'bag' in choice_hall_stuff:
            bags()

    elif 'ignore' in choice_hall:
        print("You're ready to see what else is in store in this madhouse of mess.")


    else:
        print('You stand in awe of the junk and waste away wondering how this could happen. \n Game Over.')

hallway()