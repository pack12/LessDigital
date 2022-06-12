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
    def move(self, current_tile, target_tile, piece):
        pass
    # def load_piece(self, piece_dict):
    #     piece_surfs = []
    #     for i in piece_dict:
    #         surface = pygame.image.load(piece_dict[j])
    #         piece_surfs.append(surface)






def main():
    lb_1 = Piece(2,3,'tile_3','Images/brownpi.png','lb')
    lb_2 = Piece(4,5,'tile_7','Images/brownpi.png','lb')
    pieces = {'lb_1':lb_1, 'lb_2': lb_2}
    lb_2.tile = 'tile_4'







main()