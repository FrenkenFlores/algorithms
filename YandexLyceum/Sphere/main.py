import pygame


WIDTH = 300
HEIGHT = 300


def draw(n, screen):
    dx = 150 / n
    for i in range(n):
        pygame.draw.ellipse(
            screen,
            pygame.Color('white'),
            (dx * i, 0, 300 - dx * i * 2, 300),
            width=1
        )
    for j in range(n):
        pygame.draw.ellipse(
            screen,
            pygame.Color('white'),
            (0, dx * j, 300, 300 - dx * j * 2),
            width=1
        )


def main():
    try:
        n = int(input())
        size = (WIDTH, HEIGHT)
        screen = pygame.display.set_mode(size)
        screen.fill(color=pygame.Color('black'))
        draw(n, screen)
    except ValueError:
        print('Введены данные в неверном формате')
        exit(1)
    pygame.display.flip()
    while True:
        if pygame.event.wait().type == pygame.QUIT:
            break
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.display.set_caption('Сфера')
