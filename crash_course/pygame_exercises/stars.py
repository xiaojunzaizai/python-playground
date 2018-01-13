import random
import sys

import pygame
from pygame.sprite import Group, Sprite

DISPLAY_MODE = 1920, 1080
BACKGROUND_COLOR = 0, 0, 0
STAR_IMAGE_PATH = 'images/star.png'


class Star(Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        image = pygame.image.load(STAR_IMAGE_PATH)
        self.screen = screen
        self.image = pygame.transform.scale(image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def get_star_rect(screen):
    star = Star(screen, 0, 0)
    return star.rect


def make_stars(screen):
    screen_rect = screen.get_rect()

    star_rect = get_star_rect(screen)
    star_x_spacing = star_rect.width * 2
    star_y_spacing = star_rect.height * 2

    space_available_x = screen_rect.width - star_x_spacing * 2
    number_of_stars_x = space_available_x // (star_x_spacing * 2)

    space_available_y = screen_rect.height - star_y_spacing * 2
    number_of_stars_y = space_available_y // (star_y_spacing * 2)

    print(number_of_stars_x, number_of_stars_y)

    stars = Group()
    for row_number in range(number_of_stars_y):
        for star_number in range(number_of_stars_x):
            x = star_x_spacing + star_number * star_x_spacing * 2
            y = star_y_spacing + row_number * star_y_spacing * 2
            # using random offsets to create a bit more realistic stars placing
            x += random.randint(-30, 30)
            y += random.randint(-30, 30)
            stars.add(Star(screen, x, y))

    return stars

pygame.init()
screen = pygame.display.set_mode(DISPLAY_MODE)
stars = make_stars(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BACKGROUND_COLOR)
    for star in stars.sprites():
        star.blitme()
    pygame.display.flip()
