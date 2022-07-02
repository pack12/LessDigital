import pygame


class Piece:
    def __init__(self,x,y, tile, image_path, color):
        self.x = x
        self.y = y
        self.tile = tile
        self.image_path = image_path
        self.color = color

    def validate_move(self, current_tile, target_tile):
        pass
    def move(self, current_tile, target_tile, piece, tiles):
        pass
    # def load_piece(self, piece_dict):
    #     piece_surfs = []
    #     for i in piece_dict:
    #         surface = pygame.image.load(piece_dict[j])
    #         piece_surfs.append(surface)






