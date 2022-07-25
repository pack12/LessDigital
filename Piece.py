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


    def validate_move(self,  move_direction,  inverse_direction, current_tile_type, target_tile_type,jump, target_tile, tiles, diagonal, selected_piece, wall_jump, moves_left):
        valid_moves = ['N', 'E', 'S', 'W']

        if tiles[target_tile]['isOcuppied'] == True or selected_piece.movable == False or diagonal == True:
            print('INvalid move')
            return False
        elif move_direction in valid_moves and wall_jump != True and jump != True:
            potential_walls = {'current_tile_types': [], 'target_tile_types': []}
            for i in current_tile_type:
                potential_walls['current_tile_types'].append(i)

            for i in target_tile_type:
                potential_walls['target_tile_types'].append(i)

            print('Potential Walls : ', potential_walls)

            if move_direction in potential_walls['current_tile_types'] or inverse_direction in potential_walls['target_tile_types']:
                return False

            return True
        elif move_direction in valid_moves and wall_jump == True:
            if moves_left - 2 >= 0:
                return True
            else:
                return False
        elif move_direction in valid_moves and jump == True :
            potential_walls = {'current_tile_types': [], 'target_tile_types': []}
            for i in current_tile_type:
                potential_walls['current_tile_types'].append(i)

            for i in target_tile_type:
                potential_walls['target_tile_types'].append(i)

            print('Potential Walls : ', potential_walls)

            if move_direction in potential_walls['current_tile_types'] or inverse_direction in potential_walls['target_tile_types']:
                print('invalid jump')

                return False
            elif moves_left - 1 >= 0 and move_direction not in potential_walls['current_tile_types'] and inverse_direction not in potential_walls['target_tile_types']:
                print('valid jump')
                return True
            else:
                return False

    def check_wall(self, tiles, current_tile_type, current_tile, target_tile, target_tile_type, move_direction, inverse_direction):
        potential_walls = {'current_tile_types':[], 'target_tile_types':[]}
        for i in current_tile_type:
            potential_walls['current_tile_types'].append(i)


        for i in target_tile_type:
            potential_walls['target_tile_types'].append(i)

        print('Potential Walls : ', potential_walls)

        if move_direction in potential_walls['current_tile_types'] and inverse_direction not in potential_walls['target_tile_types']:
            print('Wall jump true')
            wall_jump = True
            return wall_jump
        elif inverse_direction in potential_walls['target_tile_types'] and move_direction not in potential_walls['current_tile_types']:
            print('Wall Jump True')
            wall_jump = True
            return wall_jump
        elif move_direction in potential_walls['current_tile_types'] and inverse_direction in potential_walls['target_tile_types']:

            print('Wall Jump False')
            wall_jump = False
            return wall_jump


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

        if c_tile_number -1 == t_tile_number or c_tile_number - 6 == t_tile_number:
            print('W')
            return 'W'
        elif c_tile_number + 1 == t_tile_number or c_tile_number + 6 == t_tile_number:
            print('E')
            return 'E'
        elif c_tile_number - 6 == t_tile_number or c_tile_number - 12 == t_tile_number:
            print('N')
            return 'N'
        elif c_tile_number + 6 == t_tile_number or c_tile_number + 12 == t_tile_number:
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

    def check_piece_jump(self, current_surround, target_surround):
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
