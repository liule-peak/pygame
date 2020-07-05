import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    bg_color = (230,230,230)

    while True:
        gf.check_events()

        for event in pygame.event.grt():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        pygame.display.flip()

run_game()