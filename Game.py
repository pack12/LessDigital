import time

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
    def mouse_pos_tile(self, mouse_pos, lb_piece_dict, db_dict, tiles,red_block):
        # print(mouse_pos)

        for i in tiles:
            if mouse_pos[0]>= tiles[i]['center'][0]-43 and mouse_pos[0]<=tiles[i]['center'][0]+ 43:
                if mouse_pos[1]>=tiles[i]['center'][1]-43 and mouse_pos[1]<=tiles[i]['center'][1]+43:



                    red_block = True
                    return red_block

    def draw_red_rect(self, mouse_pos, red_block, tiles):
        tile_selected = []
        if red_block == True:
            for i in tiles:
                if mouse_pos[0] >= tiles[i]['center'][0] - 43 and mouse_pos[0] <= tiles[i]['center'][0] + 43:
                    if mouse_pos[1] >= tiles[i]['center'][1] - 43 and mouse_pos[1] <= tiles[i]['center'][1] + 43:
                        red_rect = pygame.Rect(tiles[i]['center'][0] - 50, tiles[i]['center'][1] - 50, 100, 100)
                        tiles[i]['isSelected'] = True
                        if len(tile_selected) > 1:
                            tile_selected.remove(-1)
                        tile_selected.append(i)
                        # print(tiles[i])




                        pygame.draw.rect(self.win,'red', red_rect, 5)


                        return tiles[i]


    def draw_fonts(self,isSelected):
        font = (pygame.font.Font('font/Pixeltype.ttf',25))


        isSelected = str(isSelected)
        isSelected_1 = isSelected[:int(len(isSelected)/2)]
        isSelected_2 = isSelected[int(len(isSelected)/2):]

        font_srf = pygame.font.Font.render(font, isSelected_1,False,'white')
        self.win.blit(font_srf,(615,70))

        font_srf = pygame.font.Font.render(font, isSelected_2, False, 'white')
        self.win.blit(font_srf, (615, 170))









    def run(self, tile_list, lb_piece_surfs, lb_piece_dict, db_surfs, db_dict, tiles):
        run = True
        red_block = False

        mouse_clicks = 0

        while run:
            self.clock.tick(60)
            self.win.fill('black')
            self.draw_tiles(tile_list)
            self.draw_pieces_init(lb_piece_surfs, lb_piece_dict, db_surfs, db_dict)
            # print(self.clock.get_fps())
            mouse_pos = pygame.mouse.get_pos()

            """Draw_red_rect: Draws red rect, and returns the specific rectangle, stored in variable block"""
            block = self.draw_red_rect(mouse_pos, red_block, tiles)

            """ draw_fonts: Uses Pixeltype.tff to write the selected tile info"""
            self.draw_fonts(block)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_clicks += 1
                    if mouse_clicks % 2 ==0:
                        red_block = False
                    else:
                        red_block = self.mouse_pos_tile(mouse_pos, lb_piece_dict, db_dict, tiles, red_block)
                        print(tiles)


                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    exit()
            # print(tiles)
            pygame.display.update()

