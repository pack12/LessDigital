import sys

import pygame


from Board import Board
from Square import Square
from Tile import Tile
from Piece import BoardPiece
from Piece import Piece
from TileFactory import TileFactory

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
        self.turn = 'lb'
        self.moves = 3







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
        rect_color = (0, 115, 164)
        if team == 'lb':
            # print('something shourld be bhapeing')
            font_srf = pygame.font.Font.render(font,'LB wins!', False, 'white')

            self.win.blit(font_srf, (750,400))

            font_srf = pygame.font.Font.render(font, '(Press Space to see game details)', False, 'white')
            self.win.blit(font_srf, (750, 420))


        if team == 'db':
            font_srf = pygame.font.Font.render(font,'DB wins!', False, 'white')
            # print('something shourld be bhapeing')
            self.win.blit(font_srf, (950,400))

            font_srf = pygame.font.Font.render(font, '(Press Space to see game details)', False, 'white')
            self.win.blit(font_srf, (750, 420))


    def menu_music(self, time_stamp):
        if time_stamp >= 40000:
            pygame.mixer.music.fadeout(5000)
            if time_stamp >= 45000:
                pygame.mixer.music.play()
            # pygame.mixer.music.play()
            # pygame.mixer.music.rewind()
            # pygame.mixer.music.set_pos(0.0)











    def sub_moves(self, valid_move, moves, jump, wall_jump, potential_walls, move_direction, inverse_direction, normal_move, super_jump):
        if valid_move == True and jump == True:
            moves -= 1
            self.moves -= 1
            print('self.moves: ', self.moves)
            # print('MOVES',moves)
            print('SUB Jump 1')
            return moves
        elif valid_move == True and super_jump == True:
            print('SUB SuperWAll 3')
            moves-=3
            self.moves -= 3
            print('self.moves: ', self.moves)
            return moves

        elif valid_move == True and wall_jump == True:

            moves -= 2
            self.moves -= 2
            print('self.moves: ', self.moves)
            print('Sub Wall Moves 2')
            return moves
        elif valid_move == True:
            moves -= 1
            self.moves -= 1
            print('self.moves: ', self.moves)
            print('SUB Normal Move')
            return moves
        else:
            print('self.moves: ', self.moves)
            return moves

    def change_teams(self, lb_turn, db_turn, lb_dict, db_dict):
        if lb_turn == True:
            db_turn = True
            self.turn = 'db'
            lb_turn = False

            for i in lb_dict:
                lb_dict[i].movable = False
            for i in db_dict:
                db_dict[i].movable = True
            return lb_turn, db_turn
        elif db_turn == True:
            db_turn = False
            lb_turn = True
            self.turn = 'lb'
            for i in lb_dict:
                lb_dict[i].movable = True
            for i in db_dict:
                db_dict[i].movable = False
            return lb_turn, db_turn

    def get_turn(self, lb_turn, db_turn):
        if lb_turn == True:
            return  lb_turn
        elif db_turn == True:
            return db_turn

    def set_up_turn(self, lb_dict, db_dict):
        if self.turn == 'lb':

            for i in lb_dict:
                lb_dict[i].movable = True

            for k in db_dict:
                db_dict[k].movable = False
        elif self.turn == 'db':
            for i in lb_dict:
                lb_dict[i].movable = False

            for k in db_dict:
                db_dict[k].movable = True
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

        total_player_moves = self.moves
        mouse_clicks = 0
        selected_tile_info = None
        selected_tile = None
        target_tile = None
        move_direction = None
        lb_turn = True
        db_turn = False
        victory = False
        team = None
        exit = False
        self.set_up_turn(lb_piece_dict, db_dict)
        t.reset_tile_occupied(tiles)

        exit_logo = pygame.image.load('Images/exit.png')
        exit_logo = pygame.transform.scale2x(exit_logo)
        exit_logo_rect = exit_logo.get_rect(center = (850, 500))



        cyan_srf = pygame.Surface((500, 600))

        rect_color = (0, 115, 164)


        # print(one_move_rect.x, one_move_rect.y)





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
            # print(exit_logo_rect.x,exit_logo_rect.y)
            self.win.blit(exit_logo, (exit_logo_rect.x, exit_logo_rect.y))
            pygame.draw.rect(self.win, 'black', exit_logo_rect, 5)

            if exit_logo_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                exit = True
                exit_logo.set_alpha(200)
            else:
                exit = False
                exit_logo.set_alpha(255)


            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit:
                        run = False
                        self.menu(tile_list, lb_piece_surfs, lb_piece_dict, db_surfs, db_dict, tiles)


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

                        # print('surround pieces: ', surround_pieces)
                        # print('target pieces: ', target_surround)

                        diagonal = p.check_diagonal(current_tile, target_tile, tiles)
                        target_tile_type = t.get_target_tile_type(target_tile, tiles) # Gets the wall type of target tile
                        current_tile_type = t.get_current_tile_type(current_tile, tiles) # Gets wall type of current tile type
                        potential_walls = p.potential_wall_types(current_tile_type, target_tile_type) #Splits up wall types into dict, current_tile:[list of wall types on tile], target_tile:[list of wall types on tile]
                        inverse_direction = t.get_inverse_wall(move_direction)
                        jump, middle_piece = p.check_piece_jump(surround_pieces, target_surround, current_tile, target_tile, diagonal)
                        # print('MDDLE: ', middle_piece)
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
                            self.moves = 3


                        self.clicked_tiles.clear()



                if event.type == pygame.KEYDOWN:
                    print(pygame.key)

                    if event.key == pygame.K_SPACE and victory == True:
                        print('down')
                        run = False




                    elif event.key == pygame.K_ESCAPE:

                        mouse_clicks -=1
                        tiles[selected_tile]['isSelected'] = False





                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
            # print(tiles)
            pygame.display.update()

        while victory and run == False:
            time = pygame.time.get_ticks()
            self.clock.tick(30)

            # print(time)
            # print(pygame.event.get())

            if team == 'db':
                self.win.fill((75,47,31))

                font = (pygame.font.Font('font/Pixeltype.ttf',25)) #Loading the font
                play_again_srf = pygame.font.Font.render(font, 'Play Again?', False, rect_color)
                play_again_rect = play_again_srf.get_rect(center=(500, 500))
                self.win.blit(play_again_srf, play_again_rect.center)
                pygame.draw.rect(self.win, 'black', play_again_rect)
                pygame.display.flip()
            elif team == 'lb':
                self.win.fill((185, 122, 87))
                print('LB')
                font = (pygame.font.Font('font/Pixeltype.ttf',25)) #Loading the font
                play_again_srf = pygame.font.Font.render(font, 'Play Again?', True, rect_color)
                # play_again_srf = pygame.font.Font.render(font, 'Play Again?', False, 'red')
                play_again_rect = play_again_srf.get_rect(center=(300, 400))
                self.win.blit(play_again_srf, play_again_rect.center)
                pygame.draw.rect(self.win, 'black', play_again_rect, 5)
                pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    pygame.quit()
                    exit()
            pygame.display.update()
    def menu(self, tile_list, lb_piece_surfs, lb_piece_dict, db_surfs, db_dict, tiles):
        main_menu = True
        start_col = False
        rule_col = False
        pygame.mixer.music.load('Sound/endlessmotion.mp3')

        pygame.mixer.music.play()
        # pygame.mixer.music.set_pos(float(35))

        while main_menu:
            self.clock.tick(60)
            self.win.fill('white')
            time_music = pygame.mixer.music.get_pos()
            print(time_music)
            self.menu_music(time_music)

            mouse_pos = pygame.mouse.get_pos()

            start_rect = pygame.draw.rect(self.win, 'black', pygame.Rect(self.win.get_width()/3 + 70, self.win.get_height()/3 - 100, 200, 50),5)
            rule_rect = pygame.draw.rect(self.win, 'black',pygame.Rect(self.win.get_width() / 3 + 70, self.win.get_height() / 3, 200, 50),5)
            self.menu_font(start_rect, rule_rect)


            if start_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                # new_size = start_rect.size * 2

                # start_rect = pygame.draw.rect(self.win)
                self.win.fill('white')

                start_rect = pygame.draw.rect(self.win, 'black', pygame.Rect(self.win.get_width()/3 + 50, self.win.get_height()/3 - 90, 250, 100), 5)


                rule_rect = pygame.draw.rect(self.win, 'black',pygame.Rect(self.win.get_width() / 3 + 70, self.win.get_height() / 3 + 30, 200,50), 5)
                self.menu_font(start_rect, rule_rect)
                start_col = True
            elif rule_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                self.win.fill('white')

                start_rect = pygame.draw.rect(self.win, 'black', pygame.Rect(self.win.get_width()/3 + 70, self.win.get_height()/3 - 100, 200, 50),5)

                rule_rect = pygame.draw.rect(self.win, 'black',
                                             pygame.Rect(self.win.get_width() / 3 + 50, self.win.get_height() / 3 ,
                                                         250, 100), 5)
                self.menu_font(start_rect, rule_rect)
                rule_col = True
            else:
                start_col = False
                rule_col = False

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN and rule_col == True:
                    back_arrow_img = pygame.image.load('Images/back_arrow.png')
                    back_arrow_img = pygame.transform.scale(back_arrow_img, (52, 56))
                    back_arrow_img.set_colorkey('white')
                    back_arrow_img_rect = back_arrow_img.get_rect(left = 0, top = 500)



                    rules = True
                    main_menu = False
                    while rules:
                        self.clock.tick(30)
                        self.win.fill('white')
                        # pygame.draw.rect(self.win, 'red', back_arrow_img_rect, 1)
                        self.win.blit(back_arrow_img, (back_arrow_img_rect.x, back_arrow_img_rect.y))

                        # print(back_arrow_img_rect.x, back_arrow_img_rect.y, back_arrow_img_rect.width, back_arrow_img_rect.height)
                        self.rules_font()

                        mouse_pos = pygame.mouse.get_pos()

                        if back_arrow_img_rect.collidepoint((mouse_pos[0], mouse_pos[1])):

                            # print('collision')
                            main_menu = True
                            # back_arrow_img_rect.move_ip(2, 0)
                            # back_arrow_img_rect.inflate_ip(0,2)

                            # back_arrow_img_rect.update(15, 500, 70, 74)
                            # back_arrow_img = pygame.transform.scale(back_arrow_img, (70, 74))
                            back_arrow_img.set_alpha(180)
                        else:
                            main_menu = False
                            back_arrow_img.set_alpha(255)
                            # back_arrow_img_rect.update(0, 500, 52, 56)
                            # back_arrow_img = pygame.transform.scale(back_arrow_img, (52,56))

                            # print('width and height of :', back_arrow_img_rect.width, back_arrow_img_rect.height)
                        # rules_img = pygame.image.load('Images/LessGameRules.PNG')
                        # rules_img = pygame.transform.scale(rules_img, (rules_img.get_size()[0] , rules_img.get_size()[1] - 250 ))
                        #
                        # self.win.blit(rules_img, (0,0))

                        for event in pygame.event.get():

                            if event.type == pygame.MOUSEBUTTONDOWN:

                                # print('down')
                                if main_menu == True:
                                    rules = False



                            if event.type == pygame.QUIT:
                                pygame.quit()
                                exit()

                        pygame.display.flip()
                elif event.type == pygame.MOUSEBUTTONDOWN and start_col == True:
                    main_menu = False

                    run = True
                    create_red_block = False

                    t = Tile()
                    p = BoardPiece()

                    restart = False
                    total_player_moves = self.moves
                    mouse_clicks = 0
                    selected_tile_info = None
                    selected_tile = None
                    target_tile = None
                    move_direction = None
                    if self.turn == 'lb':

                        lb_turn = True
                    else:
                        lb_turn = False

                    if self.turn == 'db':
                        db_turn = True
                    else:

                        db_turn = False
                    victory = False
                    team = None
                    exit = False
                    self.set_up_turn(lb_piece_dict, db_dict)

                    exit_logo = pygame.image.load('Images/exit.png')
                    exit_logo = pygame.transform.scale2x(exit_logo)
                    exit_logo_rect = exit_logo.get_rect(center=(950, 500))

                    restart_logo = pygame.image.load('Images/restart.png')
                    restart_logo = pygame.transform.scale2x(restart_logo)
                    restart_logo_rect = restart_logo.get_rect(center=(750, 500))

                    cyan_srf = pygame.Surface((500, 600))
                    play_again = False
                    rect_color = (0, 115, 164)
                    run = True
                    # pygame.mixer.music.pause()
                    pygame.mixer.music.fadeout(2500)
                    while run:
                        victory, team = self.victory_conditions(lb_piece_dict, db_dict, tiles)

                        # print('victor is ', victory)
                        # if victory == True:
                        #     print('vict, team', team, 'wins')

                        self.clock.tick(60)
                        self.win.fill('black')
                        pygame.draw.rect(cyan_srf, rect_color, pygame.Rect(0, 0, 500, 600))
                        self.win.blit(cyan_srf, (600, 0))

                        self.draw_victory_font(team)

                        t.draw_tiles(tile_list, self.win)
                        p.draw_pieces(lb_piece_surfs, lb_piece_dict, db_surfs, db_dict, self.win)
                        p.check_occupied(lb_piece_dict, db_dict,
                                         tiles)  # Goes through each dict, checking to see if lb/db piece xy match up with a tile location, if so, sets ocuppied to TRUE
                        p.check_color_ontile(lb_piece_dict, db_dict, tiles)
                        mouse_pos = pygame.mouse.get_pos()

                        """ draw_fonts: Uses Pixeltype.tff to write the selected tile info"""
                        self.draw_fonts(selected_tile_info, selected_tile, total_player_moves, lb_turn, db_turn)

                        """ Draws the rect rect around the selected tile if one is selected"""
                        t.draw_red_rect(selected_tile, tiles,
                                        self.win)  # Takes selected_tile, tiles list(dict of str tiles, with values of dicts), and win srf
                        # p.check_piece(lb_piece_dict, db_dict, selected_tile, tiles) # Takes selected tile and sees whether a piece occupies there, returns boolean value
                        # print(exit_logo_rect.x, exit_logo_rect.y)
                        self.win.blit(exit_logo, (exit_logo_rect.x, exit_logo_rect.y))
                        pygame.draw.rect(self.win, 'black', exit_logo_rect, 5)

                        self.win.blit(restart_logo, (restart_logo_rect.x, restart_logo_rect.y ))
                        pygame.draw.rect(self.win, 'black', restart_logo_rect, 5)

                        if exit_logo_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                            exit = True
                            exit_logo.set_alpha(200)
                        elif restart_logo_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                            restart = True
                            restart_logo.set_alpha(200)
                            # lb_pieces = {'lb_1': Piece(450, 50, 'tile_5', 'Images/brownpi.png', 'lb'),
                            #              'lb_2': Piece(550, 50, 'tile_6', 'Images/brownpi.png', 'lb'),
                            #              'lb_3': Piece(450, 150, 'tile_11', 'Images/brownpi.png', 'lb'),
                            #              'lb_4': Piece(550, 150, 'tile_12', 'Images/brownpi.png', 'lb')}
                            # db_pieces = {'db_1': Piece(50, 450, 'tile_25', 'Images/darkbrownpi.png', 'db'),
                            #              'db_2': Piece(150, 450, 'tile_26', 'Images/darkbrownpi.png', 'db'),
                            #              'db_3': Piece(50, 550, 'tile_31', 'Images/darkbrownpi.png', 'db'),
                            #              'db_4': Piece(150, 550, 'tile_32', 'Images/darkbrownpi.png', 'db')}

                        else:
                            exit = False
                            exit_logo.set_alpha(255)
                            restart = False
                            restart_logo.set_alpha(255)

                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if exit:
                                    run = False
                                    self.menu(tile_list, lb_piece_surfs, lb_piece_dict, db_surfs, db_dict, tiles)
                                if restart == True:
                                    t = TileFactory()
                                    image_list = t.randomImage()
                                    t = Tile()
                                    tiles = t.createTile(image_list)
                                    p.check_occupied(lb_piece_dict, db_dict,
                                                     tiles)  # Goes through each dict, checking to see if lb/db piece xy match up with a tile location, if so, sets ocuppied to TRUE
                                    p.check_color_ontile(lb_piece_dict, db_dict, tiles)
                                    print('Game.py:', tiles)

                                    sq = Square()
                                    squares = sq.createSquares(tiles)

                                    board = Board()
                                    tile_list = board.display_board(squares, tiles)
                                    # lb_piece_dict[]

                                    lb_piece_dict = {'lb_1': Piece(450, 50, 'tile_5', 'Images/brownpi.png', 'lb'),
                                                 'lb_2': Piece(550, 50, 'tile_6', 'Images/brownpi.png', 'lb'),
                                                 'lb_3': Piece(450, 150, 'tile_11', 'Images/brownpi.png', 'lb'),
                                                 'lb_4': Piece(550, 150, 'tile_12', 'Images/brownpi.png', 'lb')}

                                    db_dict = {'db_1': Piece(50, 450, 'tile_25', 'Images/darkbrownpi.png', 'db'),
                                                 'db_2': Piece(150, 450, 'tile_26', 'Images/darkbrownpi.png', 'db'),
                                                 'db_3': Piece(50, 550, 'tile_31', 'Images/darkbrownpi.png', 'db'),
                                                 'db_4': Piece(150, 550, 'tile_32', 'Images/darkbrownpi.png', 'db')}

                                    t.reset_tile_occupied(tiles)


                                    self.turn = 'lb'
                                    self.moves = 3
                                    total_player_moves = self.moves
                                    lb_turn = True
                                    db_turn = False
                                    self.set_up_turn(lb_piece_dict, db_dict)

                                # if play_again == True:
                                #     run = True




                                selected_tile, selected_tile_info = t.tile_selector(mouse_pos, tiles)
                                self.clicked_tiles.append(selected_tile)
                                t.check_clicked_tiles(tiles,
                                                      self.clicked_tiles)  # Every click, clicked tiles in list are checked
                                t.highlight_tile(tiles, selected_tile,
                                                 self.clicked_tiles)  # Highlights tiles that are occupied, depending on selected tile

                                if len(self.clicked_tiles) == 2:
                                    current_tile = self.clicked_tiles[0]
                                    target_tile = self.clicked_tiles[1]

                                    print('current and target: ', current_tile, target_tile)
                                    current_tile, target_tile = t.sort_clicked_tiles(current_tile, target_tile, tiles)
                                    selected_piece = p.get_piece(lb_piece_dict, db_dict, current_tile, tiles)
                                    move_direction = p.check_direction(current_tile, target_tile)
                                    surround_pieces = p.check_surround(current_tile, tiles, self.clicked_tiles)
                                    target_surround = p.check_target_surround(current_tile, target_tile, tiles)

                                    print('surround pieces: ', surround_pieces)
                                    print('target pieces: ', target_surround)

                                    diagonal = p.check_diagonal(current_tile, target_tile, tiles)
                                    target_tile_type = t.get_target_tile_type(target_tile,
                                                                              tiles)  # Gets the wall type of target tile
                                    current_tile_type = t.get_current_tile_type(current_tile,
                                                                                tiles)  # Gets wall type of current tile type
                                    potential_walls = p.potential_wall_types(current_tile_type,
                                                                             target_tile_type)  # Splits up wall types into dict, current_tile:[list of wall types on tile], target_tile:[list of wall types on tile]
                                    inverse_direction = t.get_inverse_wall(move_direction)
                                    jump, middle_piece = p.check_piece_jump(surround_pieces, target_surround,
                                                                            current_tile, target_tile, diagonal)
                                    # print('MDDLE: ', middle_piece)
                                    middle_piece_walls = t.get_current_tile_type(middle_piece,
                                                                                 tiles)  # Using get_c_type for middle_tile
                                    normal_move = p.check_normal_move(potential_walls, move_direction,
                                                                      inverse_direction, target_tile, current_tile)
                                    # print('Inverse:', inverse_direction)
                                    wall_jump = p.check_wall(tiles, current_tile_type, current_tile, target_tile,
                                                             target_tile_type, move_direction, inverse_direction, jump,
                                                             normal_move)
                                    super_jump, wall_jump = p.check_super_wall(current_tile_type, target_tile_type,
                                                                               move_direction, inverse_direction,
                                                                               wall_jump)
                                    valid_move = p.validate_move(move_direction, inverse_direction, current_tile_type,
                                                                 target_tile_type, jump, target_tile, tiles, diagonal,
                                                                 selected_piece, wall_jump, total_player_moves,
                                                                 potential_walls, normal_move, middle_piece,
                                                                 middle_piece_walls,
                                                                 super_jump)  # Depending on move direction, returns whether move is valid

                                    total_player_moves = self.sub_moves(valid_move, total_player_moves, jump, wall_jump,
                                                                        potential_walls, move_direction,
                                                                        inverse_direction, normal_move, super_jump)

                                    # print('MOVES in game.py:', total_player_moves)

                                    p.move(current_tile, target_tile, tiles, lb_piece_dict, db_dict, valid_move)

                                    if total_player_moves == 0:
                                        lb_turn, db_turn = self.change_teams(lb_turn, db_turn, lb_piece_dict, db_dict)
                                        # print('lb turn is: ', lb_turn)
                                        # print('db_turn is: ', db_turn)
                                        total_player_moves = 3
                                        self.moves = 3

                                    self.clicked_tiles.clear()

                            if event.type == pygame.KEYDOWN:
                                print(pygame.key)
                                if event.key == pygame.K_SPACE and victory == True:
                                    # print('something should happen')
                                    run = False




                                elif event.key == pygame.K_ESCAPE:

                                    mouse_clicks -= 1
                                    tiles[selected_tile]['isSelected'] = False

                            if event.type == pygame.QUIT:
                                run = False
                                pygame.quit()
                                sys.exit()
                        # print(tiles)
                        pygame.display.update()

                    while victory == True and run == False:
                        time = pygame.time.get_ticks()
                        mouse_pos = pygame.mouse.get_pos()

                        # print(pygame.event.get())

                        if team == 'db':
                            self.win.fill((75, 47, 31))
                            font = (pygame.font.Font('font/Pixeltype.ttf', 50))  # Loading the font
                            play_again_srf = pygame.font.Font.render(font, 'Play Again?', False, rect_color)
                            play_again_rect = play_again_srf.get_rect(center=(self.win.get_width() / 2, self.win.get_height() / 2))
                            self.win.blit(play_again_srf, (play_again_rect.center[0] - 70, play_again_rect.center[1]))

                            # print('Width of play again srf: ', play_again_srf.get_width())
                            # print('Width of play again rct: ', play_again_rect.width)
                            play_again_rect.width += 25
                            play_again_rect.height += 25
                            # play_again_rect.x += 55
                            pygame.draw.rect(self.win, 'black', play_again_rect, 5)

                            if play_again_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                                pygame.draw.rect(self.win, 'white', play_again_rect,0)
                                self.win.blit(play_again_srf,(play_again_rect.center[0] - 80, play_again_rect.center[1] - 10))
                                play_again = True



                            pygame.display.flip()
                        elif team == 'lb':
                            self.win.fill((185, 122, 87))


                            font = (pygame.font.Font('font/Pixeltype.ttf', 50))  # Loading the font
                            play_again_srf = pygame.font.Font.render(font, 'Play Again?', True, rect_color)
                            # play_again_srf = pygame.font.Font.render(font, 'Play Again?', False, 'red')
                            play_again_rect = play_again_srf.get_rect(center=(self.win.get_width() / 2, self.win.get_height() / 2))
                            self.win.blit(play_again_srf, (play_again_rect.x, play_again_rect.y))
                            play_again_rect.width += 10
                            play_again_rect.height += 10
                            play_again_rect.x -= 10
                            play_again_rect.y -= 5
                            pygame.draw.rect(self.win, 'black', play_again_rect, 1)

                            if play_again_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                                pygame.draw.rect(self.win, 'white', play_again_rect, 0)
                                self.win.blit(play_again_srf, (play_again_rect.x + 5, play_again_rect.y + 5))
                                play_again = True
                        self.clock.tick(60)
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if play_again == True:
                                    t = TileFactory()
                                    image_list = t.randomImage()
                                    t = Tile()
                                    tiles = t.createTile(image_list)

                                    sq = Square()
                                    squares = sq.createSquares(tiles)

                                    board = Board()
                                    tile_list = board.display_board(squares, tiles)

                                    lb_pieces = {'lb_1': Piece(450, 50, 'tile_5', 'Images/brownpi.png', 'lb'),
                                                 'lb_2': Piece(550, 50, 'tile_6', 'Images/brownpi.png', 'lb'),
                                                 'lb_3': Piece(450, 150, 'tile_11', 'Images/brownpi.png', 'lb'),
                                                 'lb_4': Piece(550, 150, 'tile_12', 'Images/brownpi.png', 'lb')}
                                    db_pieces = {'db_1': Piece(50, 450, 'tile_25', 'Images/darkbrownpi.png', 'db'),
                                                 'db_2': Piece(150, 450, 'tile_26', 'Images/darkbrownpi.png', 'db'),
                                                 'db_3': Piece(50, 550, 'tile_31', 'Images/darkbrownpi.png', 'db'),
                                                 'db_4': Piece(150, 550, 'tile_32', 'Images/darkbrownpi.png', 'db')}
                                    self.turn = 'lb'
                                    self.moves = 3

                                    self.run(tile_list, lb_piece_surfs, lb_pieces, db_surfs, db_pieces, tiles)






                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        pygame.display.update()


                if event.type == pygame.QUIT:

                    main_menu = False
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    def menu_font(self, start_rect, rules_rect):

        less_logo = pygame.image.load('Images/lesslogo.png')
        self.win.blit(less_logo, (self.win.get_width()/2 - 160, 10))


        font = pygame.font.Font('font/Pixeltype.ttf', 25)
        start_game_srf = font.render('Start Game', True, (0, 115, 164),'white')

        rules_srf = font.render('Rules', True, (0, 115, 164), 'white')


        # start_game_srf = pygame.font.Font.render('Start Game', False, 'Cyan', background= 'white')
        # self.win.blit(start_game_srf, (self.win.get_width()/3 + 50, self.win.get_height()/3 - 80))
        self.win.blit(start_game_srf, (start_rect.centerx - 45, start_rect.centery - 5))
        self.win.blit(rules_srf, (rules_rect.centerx - 20, rules_rect.centery - 5))

    def rules_font(self):
        font = pygame.font.Font('font/Pixeltype.ttf', 25)
        title_font = pygame.font.Font('font/Pixeltype.ttf', 25)
        title_font.set_bold(True)
        title_srf = title_font.render('Rules', True, 'black', 'white')
        # print(title_srf.get_size())
        title_srf = pygame.transform.scale(title_srf, (106, 32))
        self.win.blit(title_srf, (500, 10))

        obj_str = 'Objective of game is to reach opposite corner of board with all of your pieces, ' \
                  'but making fewer moves than your opponent!'
        obj_srf = font.render(obj_str, True, (0, 115, 164), 'white')
        self.win.blit(obj_srf,(30, 50))

        obj_str_2 = 'Each player gets 3 moves per turn'
        obj_srf_2 = font.render(obj_str_2, True, (0, 115, 164), 'white')
        self.win.blit(obj_srf_2, (30, 100))

        obj_str_3 = 'A piece moving to a blank space without going over a blue wall cost one move'
        obj_srf_3 = font.render(obj_str_3, True, (0, 115, 164), 'white')
        self.win.blit(obj_srf_3, (30, 150))

        obj_str_4 = 'A piece moving to a tile by going over a wall cost 2 moves! Jumping over a double wall cost 3 moves!'
        obj_srf_4 = font.render(obj_str_4, True, (0, 115, 164), 'white')
        self.win.blit(obj_srf_4, (30, 200))

        one_move_str = 'One Move'
        one_move_srf = title_font.render(one_move_str, True, (0, 115, 164), 'white')
        self.win.blit(one_move_srf, (30, 250))

        one_move_img = pygame.image.load('Images/one_move.png')
        one_move_img = pygame.transform.scale(one_move_img, (one_move_img.get_width() /2 , one_move_img.get_height() /2))
        one_move_rect = one_move_img.get_rect()
        self.win.blit(one_move_img, (30, 300))


        two_move_str = 'Two Moves'
        two_move_srf = title_font.render(two_move_str, True, (0, 115, 164), 'white')
        self.win.blit(two_move_srf, (650, 250))

        two_move_img = pygame.image.load('Images/twomoves.png')
        two_move_img = pygame.transform.scale(two_move_img, (two_move_img.get_width() / 2, two_move_img.get_height() / 2))
        self.win.blit(two_move_img, (one_move_img.get_width() + 100, 300))




