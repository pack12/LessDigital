import pygame

class Game:
    def __init__(self):
        self.width = 600
        self.height = 600
        self.win = pygame.display.set_mode((self.width, self.height))
        print("Game class")

    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
