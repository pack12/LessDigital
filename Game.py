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



        print("Game class")



    def draw_fonts(self,isSelected, selected_tile):
        font = (pygame.font.Font('font/Pixeltype.ttf',25)) #Loading the font


        isSelected = str(isSelected)
        isSelected_1 = isSelected[:int(len(isSelected)/2)]
        isSelected_2 = isSelected[int(len(isSelected)/2):]
        isSelected_3 = selected_tile

        font_srf = pygame.font.Font.render(font, isSelected_1,False,'white') # Creating the font srf using font.render
        self.win.blit(font_srf,(615,70))

        font_srf = pygame.font.Font.render(font, isSelected_2, False, 'white') #using same variable to render isSelected2
        self.win.blit(font_srf, (615, 170))

        font_srf = pygame.font.Font.render(font, isSelected_3, False, 'white')
        self.win.blit(font_srf, (615, 270))


    def sub_moves(self, valid_move, moves):
        if valid_move == True:
            moves -= 1
            print(moves)
            return moves
        else:
            return moves

    def change_teams(self, lb_turn, db_turn, lb_dict, db_dict):
        if lb_turn == True:
            db_turn = True
            lb_turn = False

            for i in lb_dict:
                lb_dict[i].moveable = False
            for i in db_dict:
                db_dict[i].moveable = True
            return lb_turn, db_turn
        elif db_turn == True:
            db_turn = False
            lb_turn = True
            for i in lb_dict:
                lb_dict[i].moveable = True
            for i in db_dict:
                db_dict[i].moveable = False
            return lb_turn, db_turn

    def set_up_turn(self, lb_dict, db_dict):
        for i in lb_dict:
            lb_dict[i].movable = True

        for k in db_dict:
            db_dict[i].movable = False

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
        lb_turn = False
        db_turn = True
        self.set_up_turn(lb_piece_dict, db_dict)
        while run:
            self.clock.tick(60)
            self.win.fill('black')

            t.draw_tiles(tile_list,self.win)
            p.draw_pieces(lb_piece_surfs, lb_piece_dict, db_surfs, db_dict,self.win)
            p.check_occupied(lb_piece_dict,db_dict,tiles) # Goes through each dict, checking to see if lb/db piece xy match up with a tile location, if so, sets ocuppied to TRUE
            mouse_pos = pygame.mouse.get_pos()


            """ draw_fonts: Uses Pixeltype.tff to write the selected tile info"""
            self.draw_fonts(selected_tile_info, selected_tile)

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
                        move_direction = p.check_direction(current_tile,target_tile)
                        surround_pieces = p.check_surround(current_tile, tiles, self.clicked_tiles)
                        target_surround = p.check_target_surround(current_tile,target_tile, tiles)

                        # print('surround pieces: ', surround_pieces)
                        # print('target pieces: ', target_surround)
                        jump = p.check_jump(surround_pieces, target_surround)
                        diagonal = p.check_diagonal(current_tile, target_tile, tiles)
                        target_tile_type = t.get_target_tile_type(target_tile, tiles) # Gets the wall type of target tile
                        current_tile_type = t.get_current_tile_type(current_tile, tiles) # Gets wall type of current tile type
                        # check_ontile = t.get_inside_wall(move_direction, current_tile_type)
                        # check_targettile = t.get_inverse_wall(move_direction, target_tile_type)

                        valid_move = p.validate_move(move_direction, jump, target_tile, tiles, diagonal) # Depending on move direction, returns whether move is valid
                        total_player_moves = self.sub_moves(valid_move,total_player_moves)
                        p.move(current_tile,target_tile,tiles,lb_piece_dict,db_dict, valid_move)

                        if total_player_moves == 0:

                            total_player_moves = 3
                            lb_turn, db_turn = self.change_teams(lb_turn, db_turn, lb_piece_dict, db_dict)
                        self.clicked_tiles.clear()


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        print(tiles)
                        # print(lb_piece_dict['lb_2'].tile)
                        # print(db_dict)
                        # print('Player Moves: ', total_player_moves)
                        print(db_dict['db_1'].movable)
                        print(lb_piece_dict['lb_1'].movable)


                    elif event.key == pygame.K_ESCAPE:

                        mouse_clicks -=1
                        tiles[selected_tile]['isSelected'] = False





                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    exit()
            # print(tiles)
            pygame.display.update()

