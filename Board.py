import pygame
from Square import Square
from Tile import Tile

class Board:
    def __init__(self):
        self.tile_list = []
    def display_board(self):
        s = Square()
        t = Tile()
        squares = s.createSquares()
        tiles = t.createTile()
        for i in squares:
            for j in squares[i]:
                # print(j)
                if j in tiles:
                    print(j)
                    # print(tiles[j]['imagePath'])
                    tile = pygame.image.load(tiles[j]['imagePath'])
                    self.tile_list.append(tile)


def main():

    b = Board()
    b.display_board()
main()