import util, character

def main():
    name = util.slow_input("Navn: ")
    player = character.Player(name)

    while True:
        actions = ["Let etter mat", "Åpne sekken", "Sjekk tilstanden din"]
        choice = util.choice(actions)
        if choice == 0:
            player.look_for_food()
        elif choice == 1:
            player.open_backpack()
        elif choice == 2:
            player.print_status()

if __name__ == "__main__":
    main()