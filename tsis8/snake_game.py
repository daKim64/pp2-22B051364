import random

import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLOCK_SIZE = 40
clock = pygame.time.Clock()
font = pygame.font.SysFont('Consolas', 36)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [
            Point(x=WIDTH // BLOCK_SIZE // 2, y=HEIGHT // BLOCK_SIZE // 2, ),
            Point(x=WIDTH // BLOCK_SIZE // 2 + 1, y=HEIGHT // BLOCK_SIZE // 2),
        ]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y
        self.body[0].x += dx
        self.body[0].y += dy

        if self.body[0].x > WIDTH // BLOCK_SIZE:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // BLOCK_SIZE
        elif self.body[0].y < 0:
            self.body[0].y = WIDTH // BLOCK_SIZE
        elif self.body[0].y > HEIGHT // BLOCK_SIZE:
            self.body[0].y = 0

    def check_collision(self, item):
        if item.location.x != self.body[0].x:
            return False
        if item.location.y != self.body[0].y:
            return False
        return True

    def self_collision(self):
        for segments in self.body[1:]:
            if self.body[0].x == segments.x and self.body[0].y == segments.y:
                return True
        return False


def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)


class Wall:
    def __init__(self, x, y):
        self.location = Point(x, y)
        self.rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            (3, 177, 252),
            self.rect
        )


class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            GREEN,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )


def main():
    running = True
    snake = Snake()
    food = Food(5, 5)
    walls = [Wall(5, 3), Wall(5, 2), Wall(5, 1)]
    score = 0
    dx, dy = 1, 0

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy != +1:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN and dy != -1:
                    dx, dy = 0, +1
                elif event.key == pygame.K_RIGHT and dx != -1:
                    dx, dy = 1, 0
                elif event.key == pygame.K_LEFT and dx != 1:
                    dx, dy = -1, 0

        snake.move(dx, dy)

        if snake.check_collision(food):
            score += 1
            snake.body.append(
                Point(snake.body[-1].x, snake.body[-1].y)
            )
            food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)

        if snake.self_collision():
            running = False
            quit()

        for wall in walls:
            if snake.check_collision(wall):
                running = False
                quit()

        snake.draw()

        for wall in walls:
            wall.draw()

        food.draw()
        draw_grid()

        score_text = font.render(f"Score: {score}", True, WHITE)
        SCREEN.blit(score_text, ((WIDTH // 2) - score_text.get_width() // 2, BLOCK_SIZE // 2))

        pygame.display.flip()
        clock.tick(5)


if __name__ == '__main__':
    main()
