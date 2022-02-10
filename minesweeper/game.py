import pygame, sys
from pygame.locals import *

from minesweeper.gameboard import GameBoard


class Game:
    BLACK = (0, 0, 0)
    WHITE = (200, 200, 200)
    BLUE = (100, 120, 200)
    RED = (200, 50, 50)

    def __init__(self):
        self.x_tiles = 10
        self.y_tiles = 10

        self.game_board = GameBoard(self.x_tiles, self.y_tiles, 5)
        self.tile_size = 20

        self.window_height = self.y_tiles * self.tile_size
        self.window_width = self.x_tiles * self.tile_size

        pygame.init()

        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.clock = pygame.time.Clock()

        self.screen.fill(Game.BLACK)

        font = pygame.freetype.SysFont(["DejaVu Sans", "Arial", "Helvetica"], self.tile_size - 2)
        self.numbers = [font.render(str(i), Game.WHITE) for i in range(8)]

        self.dead = False

    def draw_grid(self):
        for x in range(self.x_tiles):
            for y in range(self.y_tiles):
                if not self.game_board.is_checked(x, y):
                    pygame.draw.rect(self.screen,
                                     Game.WHITE,
                                     [self.tile_size * x + 1,
                                      self.tile_size * y + 1,
                                      self.tile_size - 2,
                                      self.tile_size - 2])
                    if self.game_board.is_marked(x, y):
                        pygame.draw.circle(self.screen,
                                           Game.BLUE,
                                           (x * self.tile_size + self.tile_size / 2,
                                            y * self.tile_size + self.tile_size / 2),
                                           (self.tile_size-2) / 2)
                else:
                    num = self.game_board.count_bombs(x, y)
                    if num != 0:
                        self.screen.blit(self.numbers[num][0], (x * self.tile_size+2, y * self.tile_size+2))

                if self.dead and self.game_board.is_bomb(x, y):
                    pygame.draw.circle(self.screen,
                                       Game.RED,
                                       (x * self.tile_size + self.tile_size / 2,
                                        y * self.tile_size + self.tile_size / 2),
                                       (self.tile_size-2) / 2)

    def main_loop(self):
        self.screen.fill(Game.BLACK)
        self.draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP and not self.dead:
                pos = event.pos
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos_grid_x = mouse_pos[0] // self.tile_size
                mouse_pos_grid_y = mouse_pos[1] // self.tile_size
                if event.button == 1:  # left click
                    self.dead = self.game_board.check_tile(mouse_pos_grid_x, mouse_pos_grid_y)

                if event.button == 3:  # right click
                    self.game_board.mark_tile(mouse_pos_grid_x, mouse_pos_grid_y)

        self.clock.tick(60)
        pygame.display.flip()

    def run(self):
        while True:
            self.main_loop()
