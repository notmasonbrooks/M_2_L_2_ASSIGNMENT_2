place = input("Choose a place: forest or cave?\n ").lower()

if place == "forest":
    action = input("climb a tree or cross a river?\n").lower()
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input(
        "Whats your next move?: light torch or proceed in the dark?\n"
    ).lower()
    if action == "light torch":
        print("You find a hidden treasure!")
    elif action == "proceed in the dark":
        print("Too dark to see! Maybe find a light source.")
    else:
        pass
