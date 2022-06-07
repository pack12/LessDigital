import pygame
from Board import Board
class Game:

    def __init__(self):
        self.width = 600
        self.height = 600
        self.win = pygame.display.set_mode((self.width, self.height))


        print("Game class")
    def draw_tiles(self, tile_list):
        # self.win.blit()
        x,y=0,0
        numero = 0
        for i in tile_list:

            i = pygame.transform.scale(i, (100,100))
            if x == 450:


                self.win.blit(i,(x,y))
                numero+=1
                x = 0
                y += 90
            else:

                self.win.blit(i,(x,y))
                x += 90
                numero+=1

        print("This is numero: {}".format(numero))

    def run(self):
        run = True
        b = Board()
        b.display_board()
        g = Game()
        print(len(b.tile_list))
        print(b.tile_list[0])
        g.draw_tiles(b.tile_list)
        while run:

            # g.draw_tiles(b.tile_list)

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

