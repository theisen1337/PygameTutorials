"""
    Simple PyGame Example
"""
import sys
import pygame
from pygame.locals import *
from random import *

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

# Bring in system font to display in the game.
font1 = pygame.font.SysFont('chalkduster.ttf', 16)
text1 = font1.render('coins: ', True, (50, 105, 50))
textRect1 = text1.get_rect()
textRect1.center = (100, 10)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super(Coin, self).__init__()
        self.surf = pygame.Surface((8, 8))  # patch 30px x 30px of the display.
        self.surf.fill((228, 255, 40))  # color patch
        self.rect = self.surf.get_rect(center=(50, 420))  # get positioning and rectangle parameters
        self.points = 1

    def give_points(self):
        return self.points

    def update_position(self):
        """
            randomize location
        """
        self.rect.x = randint(10, WIDTH - 10)
        self.rect.y = randint(10, HEIGHT - 10)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))  # patch 30px x 30px of the display.
        self.surf.fill((50, 205, 50))  # color patch
        self.rect = self.surf.get_rect(center=(50, 420))  # get positioning and rectangle parameters

        # Add parameters for movement.
        self.pos = vector((10, 385))
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)

        # Store points from coins
        self.score = 0

    def move(self):
        # reset acceleration
        self.acc = vector(0, 0)

        # retrieve all keys pressed.
        pressed_keys = pygame.key.get_pressed()

        # Update Acceleration on key press
        if pressed_keys[K_a]:
            self.acc.x = -ACC  # Change acceleration in the left direction
        if pressed_keys[K_d]:
            self.acc.x = ACC  # Change acceleration in the right direction
        if pressed_keys[K_w]:
            self.acc.y = -ACC  # Change acceleration in the Up direction
        if pressed_keys[K_s]:
            self.acc.y = ACC  # Change acceleration in the Down direction

        # Do the Vector math to apply acceleration and Friction to the velocity
        self.acc.x += self.vel.x * FRIC  # Multiple friction with velocity add it to acceleration
        self.acc.y += self.vel.y * FRIC  # Multiple friction with velocity add it to acceleration
        self.vel += self.acc  # Add Acceleration to velocity
        self.pos += self.vel + 0.5 * self.acc  # Add velocity, constant times acceleration to position

        # Player Bounds to the window, wrapping the player to the opposite side when they try to go off.
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        if self.pos.y > HEIGHT + 15:
            self.pos.y = 15
        if self.pos.y < 15:
            self.pos.y = HEIGHT + 15

        # Translate the position value calculated above to the player object accords.
        self.rect.midbottom = self.pos

    def update(self):
        # Check the sprite group "coins" for collisions
        hits = pygame.sprite.spritecollide(P1, coins, False)
        if hits:
            # Get points
            points = hits[0].give_points()
            # Update score
            self.add_points(points)
            # Update random position of coin
            hits[0].update_position()
        # return player score.
        return self.get_score()

    def get_score(self):
        return self.score

    def add_points(self, points_add):
        self.score += points_add


# Create Sprites
C1 = Coin()
P1 = Player()

all_spirtes = pygame.sprite.Group()
all_spirtes.add(P1)
all_spirtes.add(C1)

coins = pygame.sprite.Group()
coins.add(C1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Call player move calculations during the game loop.
    P1.move()
    points_to_display = P1.update()

    # Clearing the screen and setting to black.
    display.fill((0, 0, 0))

    # sprites draw
    for entity in all_spirtes:
        display.blit(entity.surf, entity.rect)  # drawing

    # Draw font to screen.
    text1 = font1.render('coins: ' + str(points_to_display), True, (50, 205, 50))
    display.blit(text1, textRect1)

    pygame.display.update()
    FramePerSec.tick(FPS)
