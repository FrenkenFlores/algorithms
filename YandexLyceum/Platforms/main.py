import pygame


HEIGHT = 500
WIGHT = 500
FPS = 30


def main():
    clock = pygame.time.Clock()
    running = True
    all_sprites = pygame.sprite.Group()
    all_platforms = pygame.sprite.Group()
    all_heroes = pygame.sprite.Group()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    Platform(event.pos, all_sprites, all_platforms)
                if event.button == pygame.BUTTON_RIGHT:
                    if not all_heroes:
                        Hero(event.pos, all_sprites, all_heroes)
                    all_heroes.sprites()[0].move(event.pos)
            all_sprites.update(event, all_platforms=all_platforms)
        if all_heroes:
            all_heroes.sprites()[0].fall(all_platforms=all_platforms)
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Платформы')
    size = HEIGHT, WIGHT
    screen = pygame.display.set_mode(size)

    class Platform(pygame.sprite.Sprite):
        def __init__(self, pos, *groops):
            super().__init__(groops)
            self.image = pygame.Surface((50, 10))
            self.image.fill((192, 192, 192))
            self.rect = self.image.get_rect()
            self.rect.x = pos[0]
            self.rect.y = pos[1]

    class Hero(pygame.sprite.Sprite):
        def __init__(self, pos, *groops):
            super().__init__(groops)
            self.image = pygame.Surface((20, 20))
            self.image.fill((0, 0, 255))
            self.rect = self.image.get_rect()
            self.rect.x = pos[0]
            self.rect.y = pos[1]
            self.falling = True
            self.speed = 10

        def update(self, *args, all_platforms=None):
            sprites = None
            if args:
                if args[0].type == pygame.MOUSEBUTTONDOWN and args[0].button == 3:
                    self.rect.x, self.rect.y = args[0].pos
                    return
                if args[0].type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT]:
                        self.rect.x -= self.speed
                        sprites = pygame.sprite.spritecollide(self, all_platforms, False)
                        if sprites:
                            self.rect.x = sprites[0].rect.x + sprites[0].image.get_width() + 1
                    if keys[pygame.K_RIGHT]:
                        self.rect.x += self.speed
                        sprites = pygame.sprite.spritecollide(self, all_platforms, False)
                    if sprites:
                        self.rect.x = sprites[0].rect.x - sprites[0].image.get_width() - 1
                    return

        def fall(self, all_platforms=None):
            self.rect.y += 50 / FPS * int(self.falling)
            sprites = pygame.sprite.spritecollide(self, all_platforms, False)
            if sprites:
                self.rect.y = sprites[0].rect.y - \
                              self.image.get_height()
                self.falling = False
            else:
                self.falling = True

        def move(self, pos):
            self.rect.x, self.rect.y = pos
    main()
    pygame.quit()
