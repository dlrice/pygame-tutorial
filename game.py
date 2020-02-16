#!/usr/bin/env python3
# Import the pygame module
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Import random for random numbers
import random
import time
from PIL import Image

# Initialize pygame
pygame.init()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

FPS = 30

pygame.mixer.music.load('music.ogg')
pygame.mixer.music.play(loops=-1)


lose_sound = pygame.mixer.Sound('lose.ogg')

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # self.surf = pygame.image.load('jasper.png').convert()
        self.surf = pygame.image.load('polly.png').convert()
        self.surf.set_colorkey(None, RLEACCEL)
        self.rect = self.surf.get_rect()
        self.speed = 5
        self.bark_sound = pygame.mixer.Sound('barking.ogg')

    def bark(self):
        self.bark_sound.play(maxtime=250)

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
            self.bark()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
            self.bark()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
            self.bark()
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
            self.bark()

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen.get_height():
            self.rect.bottom = screen.get_height()

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        # self.surf = pygame.image.load('squirrel.png').convert()
        self.surf = pygame.image.load('carrot.png').convert()
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen.get_width() + 20, screen.get_width() + 100),
                random.randint(0, screen.get_height()),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# background_image_path = 'forest.800x532.png'
background_image_path = 'kitchen.png'

# Create the screen object
screen = pygame.display.set_mode(
    Image.open(background_image_path).size
    )

background_image = pygame.image.load(background_image_path).convert()

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)


# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Update enemy position
    enemies.update()

    # screen.fill((135, 206, 250))
    screen.blit(background_image, (0, 0))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.music.stop()
        lose_sound.play()
        time.sleep(4) 
        running = False

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(FPS)


