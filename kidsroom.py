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

        if 'gaming' in choice:
            gaming_setup()
        else:
            print("You're confused by the chaos of the room and decide to leave it all alone.")


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

kids_room()

    