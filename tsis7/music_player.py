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

media_text = pygame.font.SysFont('Consolas', 36)
playlist = ['music-1.mp3', 'music-2.mp3', 'music-3.mp3', 'music-4.mp3']


def play():
    pygame.mixer.music.load('music/' + playlist[0])
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def play_next():
    global playlist
    playlist = playlist[1:] + [playlist[0]]
    pygame.mixer.music.load('music/' + playlist[0])
    pygame.mixer.music.play()


def play_previous():
    global playlist
    playlist = [playlist[-1]] + playlist[:-1]
    pygame.mixer.music.load('music/' + playlist[0])
    pygame.mixer.music.play()


def main():
    running = True

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play()
                elif event.key == pygame.K_w:
                    stop()
                elif event.key == pygame.K_q:
                    play_previous()
                elif event.key == pygame.K_e:
                    play_next()

        currentsong = media_text.render(playlist[0], True, (255, 255, 255))
        textrect = currentsong.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        SCREEN.blit(currentsong, textrect)
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()