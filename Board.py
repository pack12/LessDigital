import pygame


class Board:
    def __init__(self):
        self.tile_list = []
    def display_board(self, squares, tiles):

        for i in squares:
            for j in squares[i]:
                # print(j)
                if j in tiles:

                    tile = pygame.image.load(tiles[j]['imagePath'])
                    self.tile_list.append(tile)
        print("Board.py: {}".format(tiles))
        return self.tile_list


