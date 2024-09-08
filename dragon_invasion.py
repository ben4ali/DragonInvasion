import sys
import pygame
from time import sleep

from settings import Settings
from dragon import Dragon
from bullet import Bullet
from gem import Gem

from game_stats import GameStats


class DragonInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Dragon Invasion")

        self.dragon = Dragon(self)
        self.bullets = pygame.sprite.Group()
        self.gems = pygame.sprite.Group()

        self.stats = GameStats(self)

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.dragon.update()
                self.bullets.update()
                self._update_bullets()
                self._update_gems()


            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.dragon.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.dragon.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.dragon.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.dragon.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        gem = Gem(self)
        gem_width, gem_height = gem.rect.size
        available_space_x = self.settings.screen_width - (2*gem_width)
        number_gems_x = available_space_x // (2*gem_width)

        dragon_height = self.dragon.rect.height
        available_space_y = (self.settings.screen_height -
                            (3*gem_height) - dragon_height)
        number_rows = available_space_y // (2*gem_height)
        for row_number in range(number_rows):
            for gem_number in range(number_gems_x):
                self._create_gem(gem_number,row_number)

    def _create_gem(self, gem_number, row_number):
            gem = Gem(self)
            gem_width, gem_height = gem.rect.size
            gem.x = gem_width + 2 * gem_width * gem_number
            gem.rect.x = gem.x
            gem.rect.y = gem.rect.height + 2 * gem.rect.height * row_number
            self.gems.add(gem)
                    
    def _check_fleet_edges(self):
        for gem in self.gems.sprites():
            if gem.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for gem in self.gems.sprites():
            gem.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction*= -1

    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


        self._check_bullet_gems_collisions()

    def _check_bullet_gems_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets,self.gems,True,True)
        if not self.gems:
            self.bullets.empty()
            self._create_fleet()

    def _check_gems_bottom(self):
        screen_rect = self.screen.get_rect()
        for gem in self.gems.sprites():
            if gem.rect.bottom>=screen_rect.bottom:
                self._dragon_hit
                break

    def _dragon_hit(self):

        if self.stats.dragons_left > 0:
            self.stats.dragons_left -=1
            sleep(0.5)
        else:
            self.stats.game_active = False

        self.gems.empty()
        self.bullets.empty()

        self._create_fleet()
        self.dragon.center_dragon()

    def _update_gems(self):
        self._check_fleet_edges()
        self.gems.update()

        if pygame.sprite.spritecollideany(self.dragon,self.gems):
            self._dragon_hit
        
        self._check_gems_bottom()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.dragon.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.gems.draw(self.screen)

        pygame.display.flip()

if __name__== '__main__':
    di = DragonInvasion ()
    di.run_game()


