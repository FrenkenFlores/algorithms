import pygame


FPS = 60


def main():
    mx, my, delta_x, delta_y = 0, 0, 0, 0
    size = 501, 501
    screen = pygame.display.set_mode(size)
    running = True

    clock = pygame.time.Clock()

    pygame.draw.circle(screen, pygame.Color('red'), (250, 250), 20)
    on_action = False
    current_x, current_y = 250, 250

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                on_action = True
                mx, my = event.pos
                if current_x < mx:
                    delta_x = 1
                elif current_x > mx:
                    delta_x = -1
                else:
                    delta_x = 0
                if current_y < my:
                    delta_y = 1
                elif current_y > my:
                    delta_y = -1
                else:
                    delta_y = 0
        if on_action and current_x != mx and current_y != my:
            current_x += delta_x
            current_y += delta_y
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, pygame.Color('red'), (current_x, current_y), 20)
        elif on_action and current_x == mx and current_y == my:
            on_action = False
            delta_x = 0
            delta_y = 0
        elif on_action and current_x == mx and current_y != my:
            delta_x = 0
            current_x += delta_x
            current_y += delta_y
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, pygame.Color('red'), (current_x, current_y), 20)
        elif on_action and current_x != mx and current_y == my:
            delta_y = 0
            current_x += delta_x
            current_y += delta_y
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, pygame.Color('red'), (current_x, current_y), 20)
        clock.tick(FPS)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.display.set_caption('К щелчку')

    pygame.quit()
