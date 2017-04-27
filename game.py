import pygame
from game_functions import * 
from player import Player

def runGame():
    pygame.init()
    screen_size = (1000, 800)
    background_color = (82, 111, 53) # amounts RGB out of 250 each
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("A heroic 3rd person shooter")
    the_player = Player(screen)

    while True:     #main game loop
        screen.fill(background_color)
        checkEvents()


        the_player.drawMe()#Draw player

        pygame.display.flip()  # clear screen for next event





runGame()
