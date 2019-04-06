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
    

def bedroom():
    print('''You push open the damaged door.
    Inside you see eight piles of smelly dirty laundry surrounding the king size bed against the south wall.
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

            choice = input("> ")

            if "quit" in choice:
                print("This is to gross to go on, you decide.")

            else:
                print("Apparently you're a sucker for punishment.")
                pile_num_loop()

bedroom()   
