from display.graphics import HanoiGame
from display.menu_graphics import display_menu

if __name__ == "__main__":
    pegs, disks = display_menu()
    print(f"Selected game mode: {pegs} pegs, {disks} disks")
    game = HanoiGame(pegs, disks)
    game.run()