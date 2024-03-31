import os
import random

import pygame

WIDTH = 500
HEIGHT = 500
SPRITE_SIZE = 70, 70
BOMBS_NUM = 20


def main():
    coords = pygame.sprite.Group()
    all_sprites = BombsBooms()
    for _ in range(BOMBS_NUM):
        Bomb(all_sprites, coords)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                bombs = []
                for bomb in all_sprites:
                    if bomb.get_event(event):
                        bombs.append(bomb)
                if len(bombs) > 0:
                    for bomb in bombs:
                        all_sprites.add(Boom(bomb, all_sprites, coords))
                        all_sprites.remove(bomb)
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Boom them all')
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)

    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        image = pygame.image.load(fullname).convert_alpha()
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    class Bomb(pygame.sprite.Sprite):
        image = load_image("bomb.png")
        image = pygame.transform.scale(image, SPRITE_SIZE)

        def __init__(self, group, coords):
            super().__init__(group)
            self.image = Bomb.image
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(WIDTH - SPRITE_SIZE[0])
            self.rect.y = random.randrange(HEIGHT - SPRITE_SIZE[0])
            while pygame.sprite.spritecollideany(self, coords):
                self.rect.x = random.randrange(WIDTH - SPRITE_SIZE[0])
                self.rect.y = random.randrange(HEIGHT - SPRITE_SIZE[0])
            self.add(coords)

        def get_event(self, event):
            if self.rect.collidepoint(event.pos):
                return True
            return False

    class Boom(Bomb):
        image_boom = load_image("boom.png", -1)
        image_boom = pygame.transform.scale(image_boom, SPRITE_SIZE)

        def __init__(self, bomb, group, coords):
            super().__init__(group, coords)
            self.image = self.image_boom
            self.rect = self.image_boom.get_rect()
            self.rect = bomb.rect

        def get_event(self, event):
            return False

    class BombsBooms(pygame.sprite.Group):
        def __init__(self):
            super(BombsBooms, self).__init__()

        def add(self, *sprites: Bomb | Boom):
            super().add(*sprites)

    main()
    pygame.quit()
