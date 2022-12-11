"""
    Simple PyGame Example
"""
import sys
import pygame
from pygame.locals import *

pygame.init()
vector = pygame.math.Vector2

HEIGHT = 650
WIDTH = 600
ACC = 0.5
FRIC = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))  # patch 30px x 30px of the display.
        self.surf.fill((50, 205, 50))  # color patch
        self.rect = self.surf.get_rect(center=(50, 420))  # get positioning and rectangle parameters



# Create Sprites
P1 = Player()


all_spirtes = pygame.sprite.Group()
all_spirtes.add(P1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Clearing the screen and setting to black.
    display.fill((0, 0, 0))

    # sprites draw
    for entity in all_spirtes:
        display.blit(entity.surf, entity.rect)  # drawing

    pygame.display.update()
    FramePerSec.tick(FPS)