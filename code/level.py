import pygame
from settings import *

class Level:
    def __init__(self):

        #Draws the level with the same resolution configured in settings
        self.display_surface = pygame.display.get_surface()

        #Sprite groups
        self.all_sprites = pygame.sprite.Group()

    #Runs the level every frame using delta Time.
    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()