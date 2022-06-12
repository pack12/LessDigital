import pygame
class Game:

    def __init__(self):
        self.width = 600
        self.height = 600
        pygame.init()
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Less")


        print("Game class")
    def draw_tiles(self, tile_list):
        # self.win.blit()
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




    def run(self, tile_list, lb_piece_surfs, lb_piece_dict, db_surfs, db_dict):
        run = True



        while run:
            self.draw_tiles(tile_list)
            self.draw_pieces_init(lb_piece_surfs, lb_piece_dict, db_surfs, db_dict)


            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

