import sys
import pygame

def check_keydown_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left =False

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
                
def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings,screen,ship,aliens)

def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)