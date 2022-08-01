import pygame
from Tile import Tile
from Piece import BoardPiece
class Game:

    def __init__(self):
        self.width = 1100
        self.height = 600
        pygame.init()
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Less")
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.clicked_tiles = []



        # print("Game class")



    def draw_fonts(self,isSelected, selected_tile, moves_left, lb_turn, db_turn):
        font = (pygame.font.Font('font/Pixeltype.ttf',25)) #Loading the font


        # isSelected = str(isSelected)
        # isSelected_1 = isSelected[:int(len(isSelected)/2)]
        # isSelected_2 = isSelected[int(len(isSelected)/2):]
        # isSelected_3 = selected_tile
        #
        moves_left = 'Moves left: ' + str(moves_left)
        tile_selected = 'Selected Tile:' + str(selected_tile)
        #
        # font_srf = pygame.font.Font.render(font, isSelected_1,False,'white') # Creating the font srf using font.render
        # self.win.blit(font_srf,(615,70))
        #
        # font_srf = pygame.font.Font.render(font, isSelected_2, False, 'white') #using same variable to render isSelected2
        # self.win.blit(font_srf, (615, 170))
        #
        # font_srf = pygame.font.Font.render(font, isSelected_3, False, 'white')
        # self.win.blit(font_srf, (615, 270))

        font_srf = pygame.font.Font.render(font, tile_selected, False, 'white')
        font_srf = pygame.transform.scale(font_srf,(font_srf.get_size()[0] * 2, font_srf.get_size()[1] *2))
        self.win.blit(font_srf, (615, 80))

        font_srf = pygame.font.Font.render(font, moves_left, False, 'white')
        # print(font_srf.get_size())
        font_srf = pygame.transform.scale(font_srf,(200,32))
        self.win.blit(font_srf, (615,30))
        if lb_turn:

            font_srf = pygame.font.Font.render(font, 'Team: LB', False, 'burlywood1')

            font_srf = pygame.transform.scale(font_srf, (138, 32))
            self.win.blit(font_srf, (875, 30))
        elif db_turn:
            font_srf = pygame.font.Font.render(font, 'Team: DB', False, 'burlywood4')
            font_srf = pygame.transform.scale(font_srf, (138, 32))
            self.win.blit(font_srf, (875, 30))
    def draw_victory_font(self, team):
        font = (pygame.font.Font('font/Pixeltype.ttf', 25))  # Loading the font

        if team == 'lb':
            print('something shourld be bhapeing')
            font_srf = pygame.font.Font.render(font,'LB wins!', False, 'white')

            self.win.blit(font_srf, (750,400))

            font_srf = pygame.font.Font.render(font, '(Press Space to see game details)', False, 'white')
            self.win.blit(font_srf, (750, 420))
        if team == 'db':
            font_srf = pygame.font.Font.render(font,'DB wins!', False, 'white')
            print('something shourld be bhapeing')
            self.win.blit(font_srf, (950,400))

            font_srf = pygame.font.Font.render(font, '(Press Space to see game details)', False, 'white')
            self.win.blit(font_srf, (750, 420))




    def sub_moves(self, valid_move, moves, jump, wall_jump, potential_walls, move_direction, inverse_direction, normal_move, super_jump):
        if valid_move == True and jump == True:
            moves -= 1
            # print('MOVES',moves)
            print('SUB Jump 1')
            return moves
        elif valid_move == True and super_jump == True:
            print('SUB SuperWAll 3')
            moves-=3
            return moves

        elif valid_move == True and wall_jump == True:

            moves -= 2
            print('Sub Wall Moves 2')
            return moves
        elif valid_move == True:
            moves -= 1
            print('SUB Normal Move')
            return moves
        else:
            return moves

    def change_teams(self, lb_turn, db_turn, lb_dict, db_dict):
        if lb_turn == True:
            db_turn = True
            lb_turn = False

            for i in lb_dict:
                lb_dict[i].movable = False
            for i in db_dict:
                db_dict[i].movable = True
            return lb_turn, db_turn
        elif db_turn == True:
            db_turn = False
            lb_turn = True
            for i in lb_dict:
                lb_dict[i].movable = True
            for i in db_dict:
                db_dict[i].movable = False
            return lb_turn, db_turn

    def set_up_turn(self, lb_dict, db_dict):
        for i in lb_dict:
            lb_dict[i].movable = True

        for k in db_dict:
            db_dict[k].movable = False
    def victory_conditions(self, lb_dict, db_dict, tiles):
        if tiles['tile_5']['pieceColor'] == 'db' and tiles['tile_6']['pieceColor'] == 'db' and tiles['tile_11']['pieceColor'] == 'db' and tiles['tile_12']['pieceColor'] == 'db':
            return True, 'db'
        elif tiles['tile_25']['pieceColor'] == 'lb' and tiles['tile_26']['pieceColor'] == 'lb' and tiles['tile_31']['pieceColor'] == 'lb' and tiles['tile_32']['pieceColor'] == 'lb':
            return True, 'lb'
        else:
            return False, None


    def run(self, tile_list, lb_piece_surfs, lb_piece_dict, db_surfs, db_dict, tiles):
        run = True
        create_red_block = False

        t = Tile()
        p = BoardPiece()

        total_player_moves = 3
        mouse_clicks = 0
        selected_tile_info = None
        selected_tile = None
        target_tile = None
        move_direction = None
        lb_turn = True
        db_turn = False
        victory = False
        team = None
        self.set_up_turn(lb_piece_dict, db_dict)


        cyan_srf = pygame.Surface((500, 600))

        rect_color = (0, 115, 164)






        while run:
            victory, team = self.victory_conditions(lb_piece_dict, db_dict, tiles)



            # print('victor is ', victory)
            if victory == True:

                print('vict, team', team, 'wins')



            self.clock.tick(60)
            self.win.fill('black')
            pygame.draw.rect(cyan_srf, rect_color, pygame.Rect(0, 0, 500, 600))
            self.win.blit(cyan_srf, (600, 0))
            self.draw_victory_font(team)

            t.draw_tiles(tile_list,self.win)
            p.draw_pieces(lb_piece_surfs, lb_piece_dict, db_surfs, db_dict,self.win)
            p.check_occupied(lb_piece_dict,db_dict,tiles) # Goes through each dict, checking to see if lb/db piece xy match up with a tile location, if so, sets ocuppied to TRUE
            p.check_color_ontile(lb_piece_dict, db_dict, tiles)
            mouse_pos = pygame.mouse.get_pos()
           


            """ draw_fonts: Uses Pixeltype.tff to write the selected tile info"""
            self.draw_fonts(selected_tile_info, selected_tile, total_player_moves, lb_turn, db_turn)

            """ Draws the rect rect around the selected tile if one is selected"""
            t.draw_red_rect(selected_tile, tiles,self.win)  # Takes selected_tile, tiles list(dict of str tiles, with values of dicts), and win srf
            # p.check_piece(lb_piece_dict, db_dict, selected_tile, tiles) # Takes selected tile and sees whether a piece occupies there, returns boolean value



            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:

                    selected_tile, selected_tile_info = t.tile_selector(mouse_pos, tiles)
                    self.clicked_tiles.append(selected_tile)
                    t.check_clicked_tiles(tiles,self.clicked_tiles) # Every click, clicked tiles in list are checked
                    t.highlight_tile(tiles, selected_tile, self.clicked_tiles) # Highlights tiles that are occupied, depending on selected tile


                    if len(self.clicked_tiles) == 2:
                        current_tile = self.clicked_tiles[0]
                        target_tile = self.clicked_tiles[1]
                        current_tile, target_tile = t.sort_clicked_tiles(current_tile,target_tile,tiles)
                        selected_piece = p.get_piece(lb_piece_dict, db_dict, current_tile, tiles)
                        move_direction = p.check_direction(current_tile,target_tile)
                        surround_pieces = p.check_surround(current_tile, tiles, self.clicked_tiles)
                        target_surround = p.check_target_surround(current_tile,target_tile, tiles)

                        print('surround pieces: ', surround_pieces)
                        print('target pieces: ', target_surround)

                        diagonal = p.check_diagonal(current_tile, target_tile, tiles)
                        target_tile_type = t.get_target_tile_type(target_tile, tiles) # Gets the wall type of target tile
                        current_tile_type = t.get_current_tile_type(current_tile, tiles) # Gets wall type of current tile type
                        potential_walls = p.potential_wall_types(current_tile_type, target_tile_type) #Splits up wall types into dict, current_tile:[list of wall types on tile], target_tile:[list of wall types on tile]
                        inverse_direction = t.get_inverse_wall(move_direction)
                        jump, middle_piece = p.check_piece_jump(surround_pieces, target_surround, current_tile, target_tile, diagonal)
                        print('MDDLE: ', middle_piece)
                        middle_piece_walls = t.get_current_tile_type(middle_piece, tiles) #Using get_c_type for middle_tile
                        normal_move = p.check_normal_move(potential_walls, move_direction, inverse_direction,target_tile, current_tile)
                        # print('Inverse:', inverse_direction)
                        wall_jump = p.check_wall(tiles, current_tile_type, current_tile, target_tile, target_tile_type, move_direction, inverse_direction, jump, normal_move)
                        super_jump, wall_jump = p.check_super_wall(current_tile_type, target_tile_type, move_direction, inverse_direction,wall_jump)
                        valid_move = p.validate_move(move_direction, inverse_direction, current_tile_type, target_tile_type, jump, target_tile, tiles, diagonal, selected_piece, wall_jump, total_player_moves, potential_walls, normal_move, middle_piece, middle_piece_walls, super_jump) # Depending on move direction, returns whether move is valid


                        total_player_moves= self.sub_moves(valid_move,total_player_moves,jump,wall_jump, potential_walls, move_direction, inverse_direction, normal_move, super_jump)

                        # print('MOVES in game.py:', total_player_moves)

                        p.move(current_tile,target_tile,tiles,lb_piece_dict,db_dict, valid_move)




                        if total_player_moves == 0:
                            lb_turn, db_turn = self.change_teams(lb_turn, db_turn, lb_piece_dict, db_dict)
                            # print('lb turn is: ', lb_turn)
                            # print('db_turn is: ', db_turn)
                            total_player_moves = 3


                        self.clicked_tiles.clear()



                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        print(tiles)
                        # print(lb_piece_dict['lb_2'].tile)
                        print(db_dict)
                        print(db_dict['db_1'].x, db_dict['db_1'].y)
                        # print('Player Moves: ', total_player_moves)
                        # print(db_dict['db_1'].movable)
                        # print(lb_piece_dict['lb_1'].movable)
                        print('MOVES: ',total_player_moves)
                        for i in tiles:
                            if tiles[i]['isSelected'] == True:
                                for j in lb_piece_dict:
                                    if lb_piece_dict[j].x == tiles[i]['center'][0]and lb_piece_dict[j].y == tiles[i]['center'][1]:
                                        print(j, 'is', lb_piece_dict[j].movable, 'movable')
                                for k in db_dict:
                                    if db_dict[k].x == tiles[i]['center'][0] and db_dict[k].y == tiles[i]['center'][1]:
                                        print(k, 'is', db_dict[k].movable, 'movable')
                    if event.key == pygame.K_SPACE and victory == True:
                        run = False




                    elif event.key == pygame.K_ESCAPE:

                        mouse_clicks -=1
                        tiles[selected_tile]['isSelected'] = False





                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    exit()
            # print(tiles)
            pygame.display.update()

        while victory and run == False:
            time = pygame.time.get_ticks()


            print(time)
            print(pygame.event.get())

            if team == 'db':
                self.win.fill((75,47,31))
            elif team == 'lb':
                self.win.fill((185, 122, 87))
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    pygame.quit()
                    exit()
            pygame.display.update()
    # def menu(self):
    #     menu = True
    #     while menu:
    #         self.win.fill('white')
    #
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #