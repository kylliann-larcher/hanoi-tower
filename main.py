from display.graphics import HanoiGame
from display.menu_graphics import display_menu

if __name__ == "__main__":
    game = HanoiGame(display_menu())
    game.run()
