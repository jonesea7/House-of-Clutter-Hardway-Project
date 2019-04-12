def start():
    print("""You walk up to the doorstep of an eerie home
    on the eastside of Detroit. The door is ajar and you push it open.
    Inside the smell of old shoes assaults your nose. There is a giant wall 
    directly in front of you. To your left is a small step. Do you:
    Walk up the step and explore? 
    or
    Pull out your cell phone and use it as a flashlight?""")

    choice = input('> ')

    if choice == "Walk" or "explore" in choice:
        print("You step on a pile of legos and trip and break your neck.")
    elif choice == "look" or choice == "flashlight" or choice == "phone":
        print("You see a dangerous pile of loose legos on the floor. You decide to proceed with caution.")

start() 
