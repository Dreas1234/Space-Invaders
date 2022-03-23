import pygame, sys

from settings import Settings
from ship import Ship
from bullet import Bullet 
class SpaceInvaders:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Space Invaders")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            
            
    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets:
                bullet.draw_bullet()
            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self._check_keydown_events(event)
                self._check_keyup_events(event)
            
    def _check_keydown_events(self, event):
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = False
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            bullet = Bullet(self)
            self.bullets.add(bullet)
        
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
                    if bullet.rect.bottom <= 0:
                            self.bullets.remove (bullet)

if __name__ == '__main__':
    si = SpaceInvaders()
    si.run_game()
            