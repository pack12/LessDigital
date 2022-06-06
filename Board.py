import pygame
from Square import Square
from Tile import Tile

class Board:
    def display_board(self):
        s = Square()
        squares = s.createSquares()
        print(squares)
        for i in squares:
            print(i)
            for j in squares[i]:

                print(j)

                # pygame.image.load(filePath)

def main():

    b = Board()
    b.display_board()
main()