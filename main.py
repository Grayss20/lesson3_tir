import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Shooting range')
icon = pygame.image.load("img/Shooting_Range_Game_Icon.png")
pygame.display.set_icon(icon)

image_list = ['img/target.png', 'img/klipartz.com (1).png', 'img/klipartz.com (2).png',
              'img/klipartz.com (3).png', 'img/klipartz.com (4).png', 'img/klipartz.com (5).png']
target_img = pygame.image.load(random.choice(image_list))
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

hit_count = 0

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                target_img = pygame.image.load(random.choice(image_list))
                hit_count += 1

    font = pygame.font.Font(None, 36)
    text = font.render('Hits: ' + str(hit_count), True, (0, 0, 0))
    screen.blit(text, (10, 10))

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()
