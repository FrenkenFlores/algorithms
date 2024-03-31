import pygame


WIDTH = 500
HEIGHT = 600
CELL_SIZE = 100


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    color = pygame.Color('black')
                    pygame.draw.rect(
                        screen,
                        color,
                    (
                            self.left + j * self.cell_size,
                            self.top + i * self.cell_size,
                            self.cell_size,
                            self.cell_size
                        )
                    )

                elif self.board[i][j] == 1:
                    color = pygame.Color('red')
                    pygame.draw.rect(
                        screen,
                        color,
                     (
                            self.left + j * self.cell_size,
                            self.top + i * self.cell_size,
                            self.cell_size,
                            self.cell_size
                        )
                     )
                elif self.board[i][j] == 2:
                    color = pygame.Color('blue')
                    pygame.draw.rect(
                        screen,
                        color,
                        (
                            self.left + j * self.cell_size,
                            self.top + i * self.cell_size,
                            self.cell_size,
                            self.cell_size
                        )
                    )
                pygame.draw.rect(
                    screen,
                    pygame.Color('white'),
                 (
                        self.left + j * self.cell_size,
                        self.top + i * self.cell_size,
                        self.cell_size,
                        self.cell_size
                    ),
                    1
                )

    def square_pushed(self, mouse_pos):
        mx, my = mouse_pos
        if not self.left < mx < self.cell_size * self.width + self.left or \
                not self.top < my < self.cell_size * self.height + self.top:
            return None
        square_coords = ((mx - self.left) // self.cell_size + 1,
                         (my - self.top) // self.cell_size + 1)
        self.recolor(square_coords)

    def recolor(self, coords):
        x, y = coords
        x -= 1
        y -= 1
        if self.board[y][x] == 1:
            self.board[y][x] = 2
        elif self.board[y][x] == 0:
            self.board[y][x] = 1
        else:
            self.board[y][x] = 0


def main():
    board = Board(WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE)
    board.set_view(0, 0, CELL_SIZE)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.square_pushed(event.pos)
        screen.fill((0, 0, 0))
        board.render()
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    main()
