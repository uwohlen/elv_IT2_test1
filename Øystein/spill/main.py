import ioutil, player, weapon

def main():
    name = ioutil.slow_input("Navn: ")
    pl = player.Player(name)

    while not pl.dead:
        actions = ["Let etter monster", "Åpne sekken", "Info om deg selv"]
        choice = ioutil.choice(actions)
        if choice == 0:
            pl.look_for_monster()
        elif choice == 1:
            pl.open_backpack()
        elif choice == 2:
            pl.print_info()

if __name__ == "__main__":
    main()