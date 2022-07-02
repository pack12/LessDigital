import pygame


class Piece:
    def __init__(self,x,y, tile, image_path, color):
        self.x = x
        self.y = y
        self.tile = tile
        self.image_path = image_path
        self.color = color



    def check_piece(self, lb_piece_dict, db_piece_dict, selected_tile, tiles):
        if selected_tile != None:
            for i in lb_piece_dict:
                if lb_piece_dict[i].x == tiles[selected_tile]['center'][0] and lb_piece_dict[i].y == tiles[selected_tile]['center'][1]:
                    # print("Piece Here")
                    return True
            for i in db_piece_dict:
                if db_piece_dict[i].x == tiles[selected_tile]['center'][0] and db_piece_dict[i].y == tiles[selected_tile]['center'][1]:
                    # print("Piece Here")
                    return True


class BoardPiece():
    def draw_pieces(self, lb_piece_surfs, lb_piece_dict, db_surfs, db_dict,win):
        num = 0
        for i in lb_piece_dict:

            lb_piece_surfs[num] = pygame.transform.scale(lb_piece_surfs[num],(25,25))
            win.blit(lb_piece_surfs[num], (lb_piece_dict[i].x-10, lb_piece_dict[i].y-10))
            num+=1
        num = 0
        for i in db_dict:

            db_surfs[num] = pygame.transform.scale(db_surfs[num], (25,25))
            win.blit(db_surfs[num], (db_dict[i].x-10, db_dict[i].y-10))
            num+=1

    def validate_move(self, current_tile, target_tile):
        pass
    def move(self, current_tile, target_tile, piece, tiles):
        pass






