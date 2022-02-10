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

        # PROBLEM 1: Create 2 matrix (an array of arrays) with size_x columns and size_y lines. The initial values
        # should be self.grid should GameBoard.EMPTY for self.grid and GameBoard.HIDDEN for self.clear
        self.grid = [[GameBoard.EMPTY]]
        self.clear = [[GameBoard.HIDDEN]]

        # PROBLEM 5: Place GameBoard.BOMB in the self.grid. Take care of no placing two bombs int the same cell
        # Tip: You can use random.randint(min,max) to get a random number or random.sample to get a sample from a list
        self.grid[0][0] = GameBoard.BOMB

    def is_bomb(self, x: int, y: int) -> bool:
        # Problem 3: Check if a cell is a bomb. Return True if it is and False if not
        return False

    def count_bombs(self, x: int, y: int) -> int:
        # Problem 4: Count the number of bombs around the cell x, y and return the value
        bombs = 0
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
        # Problem 2: Return True if x and y corresponds to a cell in the grid and False otherwise
        return True

    def check_tile(self, x: int, y: int) -> bool:
        tiles_to_be_checked = [(x, y)]
        while tiles_to_be_checked:
            tile = tiles_to_be_checked.pop()
            if self.is_bomb(*tile):
                return True

            bombs = self.count_bombs(*tile)
            self.clear[tile[1]][tile[0]] = GameBoard.CLEAR

            if bombs == 0:
                # Problem 7: Create a list of tuples containing the x and y coordinates of all cells around the actual
                # cell. It shouldn't contain the actual cell, nor cells outside the grid, nor the cells that are
                # actually checked
                next_to_check = []

                tiles_to_be_checked += next_to_check

        return False

    def mark_tile(self, x: int, y: int) -> None:
        # Problem 6: Set the cell x, y in self.clear as GameBoard.MARKED if it is not checked (you can use
        # self.is_checked(x,y)). If it is already marked, return it to GameBoard.HIDDEN
        self.clear[0][0] = GameBoard.MARKED
