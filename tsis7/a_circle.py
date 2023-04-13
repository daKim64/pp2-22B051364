import pygame

pygame.init()

WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = 25

    def draw(self):
        pygame.draw.circle(SCREEN, RED, (self.x, self.y), self.radius)


def main():
    running = True
    ball = Ball()

    while running:
        SCREEN.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and ball.y - ball.radius - 20 >= 0:
                    ball.y -= 20
                elif event.key == pygame.K_DOWN and ball.y + ball.radius + 20 <= WIDTH:
                    ball.y += 20
                elif event.key == pygame.K_LEFT and ball.x - ball.radius - 20 >= 0:
                    ball.x -= 20
                elif event.key == pygame.K_RIGHT and ball.x + ball.radius + 20 <= HEIGHT:
                    ball.x += 20

        ball.draw()
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()