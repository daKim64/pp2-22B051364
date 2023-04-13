import random
import pygame

pygame.init()
WIDTH, HEIGHT = 400, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Street Racer v0')
background = pygame.image.load("./materials/AnimatedStreet.png")
score_font = pygame.font.SysFont("Verdana", 30)
SCORE = 0
COINS = 0


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 3
        self.image = pygame.image.load('./materials/Coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH - self.rect.width), self.rect.height // 2)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        global COINS

        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randint(0, WIDTH - self.rect.width)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('./materials/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH - self.rect.width), self.rect.height // 2)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        global SCORE

        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            SCORE += 1
            self.speed += 1
            self.rect.y = 0
            self.rect.x = random.randint(0, WIDTH - self.rect.width)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.image = pygame.image.load('./materials/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x >= self.speed:
            self.rect.x -= self.speed
        if pressed[pygame.K_RIGHT] and self.rect.x + self.rect.width + self.speed <= WIDTH:
            self.rect.x += self.speed


def main():
    running = True
    player = Player()
    enemy = Enemy()

    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    enemies.add(enemy)

    for i in range(10):
        coin = Coin()
        coin.rect.y = random.randint(0, HEIGHT // 3)
        coins.add(coin)

    while running:
        SCREEN.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
        enemy.update()
        coins.update()

        global COINS

        player.draw(SCREEN)
        enemy.draw(SCREEN)
        coins.draw(SCREEN)

        score = score_font.render(f" Your Score: {str(SCORE)}", True, (0, 0, 0))
        SCREEN.blit(score, (0, 0))

        coins_score = score_font.render(f" Coins: {str(COINS)}", True, (0, 0, 0))
        SCREEN.blit(coins_score, (WIDTH - coins_score.get_width(), 0))

        if pygame.sprite.spritecollideany(player, enemies):
            running = False

        if pygame.sprite.spritecollide(player, coins, True):
            COINS += 1

            coin = Coin()
            coins.add(coin)

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
