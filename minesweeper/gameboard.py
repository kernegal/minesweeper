import random


class GameBoard:
    EMPTY = 0
    BOMB = 1

    HIDDEN = 0
    CLEAR = 1
    MARKED = 2

    def __init__(self, size_x: int, size_y: int, num_bombs: int):
        self.size_x = size_x
        self.size_y = size_y
        self.grid = [list(GameBoard.EMPTY for _ in range(size_x)) for _ in range(size_y)]
        self.clear = [list(GameBoard.HIDDEN for _ in range(size_x)) for _ in range(size_y)]

        bombs_options = [(x, y) for x in range(size_x) for y in range(size_y)]
        for x, y in random.sample(bombs_options, num_bombs):
            self.grid[y][x] = GameBoard.BOMB

    def is_bomb(self, x: int, y: int) -> bool:
        return self.grid[y][x] == GameBoard.BOMB

    def count_bombs(self, x: int, y: int) -> int:
        bombs = 0
        for a in range(x-1, x+2):
            for b in range(y-1, y+2):
                if self.is_valid(a, b):
                    bombs += self.is_bomb(a, b)

        return bombs

    def is_checked(self, x: int, y: int) -> bool:
        """
        Check if a tile is already visited
        :param x: x position
        :param y: y position
        :return: True if visited
        """
        return self.clear[y][x] == GameBoard.CLEAR

    def is_marked(self, x: int, y: int) -> bool:
        return self.clear[y][x] == GameBoard.MARKED

    def is_valid(self, x: int, y: int) -> bool:
        return 0 <= x < self.size_x and 0 <= y < self.size_y

    def check_tile(self, x: int, y: int) -> bool:
        tiles_to_be_checked = [(x, y)]
        while tiles_to_be_checked:
            tile = tiles_to_be_checked.pop()
            if self.is_bomb(*tile):
                return True

            bombs = self.count_bombs(*tile)
            self.clear[tile[1]][tile[0]] = GameBoard.CLEAR

            if bombs == 0:
                next_to_check = [(a, b)
                                 for a in range(tile[0]-1, tile[0]+2) for b in range(tile[1]-1, tile[1]+2)
                                 if self.is_valid(a, b) and not self.is_checked(a, b) ]

                tiles_to_be_checked += next_to_check

        return False

    def mark_tile(self, x: int, y: int) -> None:
        if self.is_valid(x, y) and not self.is_checked(x, y):
            if self.is_marked(x, y):
                self.clear[y][x] = GameBoard.HIDDEN
            else:
                self.clear[y][x] = GameBoard.MARKED
