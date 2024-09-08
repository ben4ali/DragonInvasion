import pygame

class Dragon:
    def __init__(self,di_game):
        self.screen = di_game.screen
        self.settings = di_game.settings

        self.screen_rect = di_game.screen.get_rect()

        self.image = pygame.image.load('PROJECT_1\images\dragon.gif')

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def center_dragon(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x+=self.settings.dragon_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.dragon_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)