import pygame
import datetime

pygame.init()
WIDTH, HEIGHT = 829, 836
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
clock = pygame.time.Clock()
lhand = pygame.image.load('left-hand.png')
rhand = pygame.image.load('right-hand.png')
background = pygame.image.load('main-clock.png')


def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    blitRotateCenter(screen, rhand, (WIDTH // 2 - rhand.get_width() // 2, HEIGHT // 2 - rhand.get_height() // 2), minute*(360/60)-90)
    blitRotateCenter(screen, lhand, (WIDTH // 2 - lhand.get_width() // 2, HEIGHT // 2 - lhand.get_height() // 2), second*(360/60)-90)

    pygame.display.flip()
    clock.tick(60)
