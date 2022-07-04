import pygame


class Piece:
    def __init__(self,x,y, tile, image_path, color):
        self.x = x
        self.y = y
        self.tile = tile
        self.image_path = image_path
        self.color = color


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
    def check_occupied(self,lb_piece_dict, db_piece_dict, tiles):
        for i in tiles:
            for j in lb_piece_dict:
                if lb_piece_dict[j].x == tiles[i]['center'][0] and lb_piece_dict[j].y == tiles[i]['center'][1]:
                    tiles[i]['isOcuppied'] = True
            for k in db_piece_dict:
                if db_piece_dict[k].x == tiles[i]['center'][0] and db_piece_dict[k].y == tiles[i]['center'][1]:
                    tiles[i]['isOcuppied'] = True


    def validate_move(self, current_tile, target_tile):
        pass
    def move(self, selected_tile, target_tile,tiles, lb_dict, db_dict, target_selector):
        #I also need an actual piece object from lb_dict or db_dict
        #selected_tile is a str that can be used as a key
        #target_tile is also a str
        #All I need to move the piece is to take the piece x and y and move it to the target_tile center(x,y)
        #Then the piece.x y becomes target_tile center xy

        """Checking to see if piece in lb_dict is being selected"""
        for i in lb_dict:
            if selected_tile != None:

                if lb_dict[i].x == tiles[selected_tile]['center'][0] and lb_dict[i].y == tiles[selected_tile]['center'][1]:
                    print('Lb selected')
                    moveable = lb_dict[i]
            else:
                pass
        for i in db_dict:
            if selected_tile!= None:

                if db_dict[i].x == tiles[selected_tile]['center'][0] and db_dict[i].y == tiles[selected_tile]['center'][1]:

                    print('db selected')
                    moveable = db_dict[i]
            else:
                pass

        if target_tile != None:

            if tiles[target_tile]['isSelected'] == False:

                centerx = tiles[target_tile]['center'][0]
                centery = tiles[target_tile]['center'][1]

                print('Target: ', centerx, centery)


                moveable.x = centerx
                moveable.y = centery
            else:
                pass






