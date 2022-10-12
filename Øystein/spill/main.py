import util, player, environment

def main():
    name = util.slow_input("Navn: ")
    pl = player.Player(name)
    env = environment.START_ENVIRONMENT

    while not pl.dead:
        actions = ["Let etter mat", "Let etter monster", "Åpne sekken", "Sjekk tilstanden din"]
        choice = util.choice(actions)
        if choice == 0:
            pl.look_for_food()
        elif choice == 1:
            pl.look_for_monster(env)
        elif choice == 2:
            pl.open_backpack()
        elif choice == 3:
            pl.print_status()

if __name__ == "__main__":
    main()