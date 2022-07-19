import pygame


class Piece:
    def __init__(self,x,y, tile, image_path, color):
        self.x = x
        self.y = y
        self.tile = tile
        self.image_path = image_path
        self.color = color
        self.movable = False


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


    def validate_move(self,  move_direction, jump, target_tile, tiles, diagonal, selected_piece):
        valid_moves = ['N', 'E', 'S', 'W']
        if move_direction in valid_moves or jump == True:
            if tiles[target_tile]['isOcuppied'] == True or selected_piece.movable == False:
                # print('INVALID, despite ^^')
                return False
            if diagonal == True:
                # print('dagonal')
                return False
            # print('VALID MOVE')

            return True
        else:
            print('INVALID')
            return False

    def move(self, selected_tile, target_tile,tiles, lb_dict, db_dict, valid_move):

        """Checking to see if piece in lb_dict is being selected"""
        for i in lb_dict:
            if selected_tile != None:

                if lb_dict[i].x == tiles[selected_tile]['center'][0] and lb_dict[i].y == tiles[selected_tile]['center'][1]: #and lb_dict[i].movable == True
                    # print('Lb selected')    #If selected,
                    moveable = lb_dict[i] # The selected piece gets stored in the variable moveable
                    # print('is this moveable',moveable.movable)
            else:
                pass
        for i in db_dict:
            if selected_tile!= None:

                if db_dict[i].x == tiles[selected_tile]['center'][0] and db_dict[i].y == tiles[selected_tile]['center'][1]: #and db_dict[i].movable == True

                    # print('db selected')    #If selected,
                    moveable = db_dict[i] # The selected piece gets stored in the variable moveable
                    # print('is this moveable', moveable.movable)
            else:
                pass

        """ If target_tile is not None and the isSelected attribute equals false, then we move AND if movable attribute is true"""
        if target_tile != None:

            if tiles[target_tile]['isSelected'] == False and valid_move == True and moveable.movable == True:

                centerx = tiles[target_tile]['center'][0]
                centery = tiles[target_tile]['center'][1]

                # print('Target: ', centerx, centery)


                moveable.x = centerx
                moveable.y = centery

                """Changing previous tile's attributes to an empty tile"""
                tiles[selected_tile]['isSelected'] = False
                tiles[selected_tile]['isOcuppied'] = False

            else:
                pass
    def check_direction(self, current_tile, target_tile):
        c_tile_number = int(current_tile[5:])
        t_tile_number = int(target_tile[5:])

        if c_tile_number -1 == t_tile_number:
            print('W')
            return 'W'
        elif c_tile_number + 1 == t_tile_number:
            print('E')
            return 'E'
        elif c_tile_number - 6 == t_tile_number:
            print('N')
            return 'N'
        elif c_tile_number + 6 == t_tile_number:
            print('S')
            return 'S'
    def check_surround(self,current_tile, tiles, clicked_tiles):

        tile_str = 'tile_'
        surround_pieces = []

        if tiles[current_tile]['isOcuppied'] == True and current_tile in clicked_tiles:
            for i in tiles:

                #Check to the right of the tile
                if tiles[i]['isOcuppied'] == True and tiles[i]['center'][0] == tiles[current_tile]['center'][0] + 100 and tiles[i]['center'][1] == tiles[current_tile]['center'][1]:
                    surround_pieces.append(i)
                elif tiles[i]['isOcuppied'] == True and tiles[i]['center'][0] == tiles[current_tile]['center'][0] - 100 and tiles[i]['center'][1] == tiles[current_tile]['center'][1]:
                    surround_pieces.append(i)
                elif tiles[i]['isOcuppied'] == True and tiles[i]['center'][1] == tiles[current_tile]['center'][1] + 100 and tiles[i]['center'][0] == tiles[current_tile]['center'][0]:
                    surround_pieces.append(i)
                elif tiles[i]['isOcuppied'] == True and tiles[i]['center'][1] == tiles[current_tile]['center'][1] - 100 and tiles[i]['center'][0] == tiles[current_tile]['center'][0]:
                    surround_pieces.append(i)

        return surround_pieces

    def check_target_surround(self, current_tile,target_tile, tiles):
        surround_pieces = []


        for i in tiles:
            if tiles[i]['isOcuppied'] == True and tiles[i]['center'][0] == tiles[target_tile]['center'][0] + 100 and tiles[i]['center'][1] == tiles[target_tile]['center'][1]:
                surround_pieces.append(i)
            elif tiles[i]['isOcuppied'] == True and tiles[i]['center'][0] == tiles[target_tile]['center'][0] - 100 and tiles[i]['center'][1] == tiles[target_tile]['center'][1]:
                surround_pieces.append(i)
            elif tiles[i]['isOcuppied'] == True and tiles[i]['center'][1] == tiles[target_tile]['center'][1] + 100 and tiles[i]['center'][0] == tiles[target_tile]['center'][0]:
                surround_pieces.append(i)
            elif tiles[i]['isOcuppied'] == True and tiles[i]['center'][1] == tiles[target_tile]['center'][1] - 100 and tiles[i]['center'][0] == tiles[target_tile]['center'][0]:
                surround_pieces.append(i)


        if current_tile in surround_pieces:

            surround_pieces.remove(current_tile)


        return surround_pieces

    def check_jump(self, current_surround, target_surround):
        for i in current_surround:
            for j in target_surround:
                if i == j:
                    jump = True
                    return jump
        return False

    def check_diagonal(self, selected_tile, target_tile, tiles):
        s_tile_num = int(selected_tile[5:])
        t_tile_num = int(target_tile[5:])
        # print(s_tile_num, t_tile_num, 'check diag')
        if s_tile_num + 5 == t_tile_num or s_tile_num - 5 == t_tile_num:
            diagonal = True
            return diagonal
        elif s_tile_num + 7 == t_tile_num or s_tile_num - 7 == t_tile_num:
            diagonal = True
            return diagonal
        else:
            return False


    def get_piece(self, lb_dict, db_dict, selected_tile, tiles):
        for i in lb_dict:
            if lb_dict[i].x == tiles[selected_tile]['center'][0] and lb_dict[i].y == tiles[selected_tile]['center'][1]:
                print(i,lb_dict[i], 'is selected')
                return lb_dict[i]

        for i in db_dict:
            if db_dict[i].x == tiles[selected_tile]['center'][0] and db_dict[i].y == tiles[selected_tile]['center'][1]:
                print(i,db_dict[i], 'is selected')
                return db_dict[i]
