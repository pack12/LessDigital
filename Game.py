import pygame
class Game:

    def __init__(self):
        self.width = 600
        self.height = 600
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
                pygame.draw.circle(self.win, 'red', (x+50, y+50), 5)
                print(x+50, y+50)
                numero+=1
                x = 0
                y += 100
            else:

                self.win.blit(i,(x,y))
                print(x+50, y+50)
                x += 100
                numero+=1



    def run(self, tile_list):
        run = True


        self.draw_tiles(tile_list)
        while run:



            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

