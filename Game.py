import time
import types

import pygame
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
    def draw_tiles(self, tile_list):
        #testing commits
        x,y=0,0
        numero = 0
        for i in tile_list:

            i = pygame.transform.scale(i, (100,100))
            if x == 500:
                rect = i.get_rect()


                # pygame.draw.circle(i,'red',(i.get_width()/2, i.get_height()/2),5)

                self.win.blit(i,(x,y))
                # pygame.draw.circle(self.win, 'red', (x+50, y+50), 5)

                numero+=1
                x = 0
                y += 100
            else:

                self.win.blit(i,(x,y))
                
                x += 100
                numero+=1
    def draw_pieces_init(self, lb_piece_surfs, lb_piece_dict, db_surfs, db_dict):
        num = 0
        for i in lb_piece_dict:

            lb_piece_surfs[num] = pygame.transform.scale(lb_piece_surfs[num],(25,25))
            self.win.blit(lb_piece_surfs[num], (lb_piece_dict[i].x-10, lb_piece_dict[i].y-10))
            num+=1
        num = 0
        for i in db_dict:

            db_surfs[num] = pygame.transform.scale(db_surfs[num], (25,25))
            self.win.blit(db_surfs[num], (db_dict[i].x-10, db_dict[i].y-10))
            num+=1
    def check_mouse_pos(self, mouse_pos,tiles):
        print(mouse_pos[0], mouse_pos[1])

        for i in tiles:

            if mouse_pos[0]>= tiles[i]['center'][0]-43 and mouse_pos[0]<=tiles[i]['center'][0]+ 43:

                # print("This is the tile selected: ", i, ":", tiles[i])
                if mouse_pos[1]>=tiles[i]['center'][1]-43 and mouse_pos[1]<=tiles[i]['center'][1]+43:



                    create_red_block = True


                    print("Tile",i," ", tiles[i])
                    return create_red_block, tiles[i]
                else:
                    create_red_block = False
                    print("Tile", i, " ", tiles[i])
                    print(tiles[i]['center'])
                    return create_red_block
    def tile_selector(self, mouse_pos,tiles):
        print(mouse_pos[0], mouse_pos[1])

        for i in tiles:

            if mouse_pos[0]>= tiles[i]['center'][0]-43 and mouse_pos[0]<=tiles[i]['center'][0]+ 43:

                # print("This is the tile selected: ", i, ":", tiles[i])
                if mouse_pos[1]>=tiles[i]['center'][1]-43 and mouse_pos[1]<=tiles[i]['center'][1]+43:






                    # print("Tile",i," ", tiles[i])

                    # print(type(i))
                    # print(type(tiles[i]))

                    return i, tiles[i]
        return None, None

    def highlight_tile(self, tiles,selected_tile):

        self.clicked_tiles.append(selected_tile)
        recent_tile = self.clicked_tiles[-1]
        print("Recent Tiles: ",recent_tile)

        for i in self.clicked_tiles:
            if i == None:
                self.clicked_tiles.remove(i)

                # print(self.clicked_tiles)

        if recent_tile == None:
            pass
        else:

            tiles[recent_tile]['isSelected'] = True



        for i in tiles:
            if i != recent_tile:
                tiles[i]['isSelected'] = False














    def draw_red_rect(self, selected_tile, tiles):
        for i in tiles:
            if i == selected_tile:
                red_rect = pygame.Rect(tiles[selected_tile]['center'][0] - 50, tiles[selected_tile]['center'][1] - 50, 100, 100)
                pygame.draw.rect(self.win, 'red', red_rect, 5)
            else:
                pass


    def draw_fonts(self,isSelected, selected_tile):
        font = (pygame.font.Font('font/Pixeltype.ttf',25))


        isSelected = str(isSelected)
        isSelected_1 = isSelected[:int(len(isSelected)/2)]
        isSelected_2 = isSelected[int(len(isSelected)/2):]
        isSelected_3 = selected_tile

        font_srf = pygame.font.Font.render(font, isSelected_1,False,'white')
        self.win.blit(font_srf,(615,70))

        font_srf = pygame.font.Font.render(font, isSelected_2, False, 'white')
        self.win.blit(font_srf, (615, 170))

        font_srf = pygame.font.Font.render(font, isSelected_3, False, 'white')
        self.win.blit(font_srf, (615, 270))




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







    def run(self, tile_list, lb_piece_surfs, lb_piece_dict, db_surfs, db_dict, tiles):
        run = True
        create_red_block = False

        mouse_clicks = 0
        selected_tile_info = None
        selected_tile = None
        while run:
            self.clock.tick(60)
            self.win.fill('black')
            self.draw_tiles(tile_list)
            self.draw_pieces_init(lb_piece_surfs, lb_piece_dict, db_surfs, db_dict)

            mouse_pos = pygame.mouse.get_pos()


            """ draw_fonts: Uses Pixeltype.tff to write the selected tile info"""
            self.draw_fonts(selected_tile_info, selected_tile)

            self.draw_red_rect(selected_tile, tiles)

            is_piece_here = self.check_piece(lb_piece_dict, db_dict, selected_tile, tiles)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:

                    selected_tile, selected_tile_info = self.tile_selector(mouse_pos, tiles)




                    self.highlight_tile(tiles,selected_tile)

                    # print(selected_tile, " ", selected_tile_info)
                    print(tiles)





                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    exit()
            # print(tiles)
            pygame.display.update()

