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

    def target_selector(self,mouse_clicks):
            if mouse_clicks %2 == 0: #Every two clicks (even clciks) target selector activates
                target_selector = True
                return target_selector
            else:
                return False

    def mouse_button_down_event(self, mouse_clicks, selected_tile, target_tile,tiles, lb_piece_dict, db_dict,
                                mouse_pos,t,p):



        target_selector_mode = self.target_selector(mouse_clicks) #Activates this function every 2 clicks
        if target_selector_mode:
            target_tile, target_tile_info = t.tile_selector(mouse_pos, tiles)
            print('target mode: ', target_tile, target_tile_info)
            p.move(selected_tile, target_tile, tiles, lb_piece_dict, db_dict, target_selector_mode)
            return target_tile, target_tile_info


        else:

            selected_tile, selected_tile_info = t.tile_selector(mouse_pos, tiles)

            p.move(selected_tile, target_tile, tiles, lb_piece_dict, db_dict, target_selector_mode)
            t.highlight_tile(tiles, selected_tile, self.clicked_tiles)

            print(selected_tile, " ", selected_tile_info)
            return selected_tile, selected_tile_info



    def run(self, tile_list, lb_piece_surfs, lb_piece_dict, db_surfs, db_dict, tiles):
        run = True
        create_red_block = False

        t = Tile()
        p = BoardPiece()


        mouse_clicks = 0
        selected_tile_info = None
        selected_tile = None
        target_tile = None
        while run:
            self.clock.tick(60)
            self.win.fill('black')

            t.draw_tiles(tile_list,self.win)
            p.draw_pieces(lb_piece_surfs, lb_piece_dict, db_surfs, db_dict,self.win)
            p.check_occupied(lb_piece_dict,db_dict,tiles)
            mouse_pos = pygame.mouse.get_pos()


            """ draw_fonts: Uses Pixeltype.tff to write the selected tile info"""
            self.draw_fonts(selected_tile_info, selected_tile)

            """ Draws the rect rect around the selected tile if one is selected"""
            t.draw_red_rect(selected_tile, tiles, self.win) #Takes selected_tile, tiles list(dict of str tiles, with values of dicts), and win srf

            p.check_piece(lb_piece_dict, db_dict, selected_tile, tiles)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_clicks += 1
                    selected_tile, selected_tile_info = self.mouse_button_down_event(mouse_clicks,selected_tile,
                                                            target_tile,tiles,lb_piece_dict,db_dict,mouse_pos,t,p)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        print(tiles)
                    elif event.key == pygame.K_ESCAPE:

                        mouse_clicks -=1
                        selected_tile = None
                        target_tile = None

                        self.mouse_button_down_event(mouse_clicks,selected_tile, target_tile, tiles,
                                                     lb_piece_dict, db_dict, mouse_pos, t,p)







                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    exit()
            # print(tiles)
            pygame.display.update()

