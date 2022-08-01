from TileFactory import TileFactory
from Tile import Tile
from Square import Square
from Board import Board
from Game import Game
from Piece import Piece
import pygame
def main():

    """ Creating Tile factory object that uses randomImage method to create imageListPaths"""
    fact = TileFactory()
    imageList = fact.randomImage()


    """ Creating Tile object from Tile class that uses createTile method to create dictionaires of tiles"""
    t = Tile()
    tiles = t.createTile(imageList)

    print("Main: {}".format(tiles))
    # print(tiles['tile_1']['center'][1])

    """ Creating sq object from sq class that groups tiles (that get converted to str) into a key
    value pair where we have: square_1: [tile_1, tile_2, tile_3, tile_4]"""
    sq = Square()
    squares = sq.createSquares(tiles)

    """ Creating board class that returns a tile_list which is a list of surfaces that go into 
    the game.run method"""
    board = Board()
    tile_list = board.display_board(squares,tiles)

    lb_pieces = {'lb_1':Piece(450, 50,'tile_5', 'Images/brownpi.png', 'lb'), 'lb_2':Piece(550, 50,'tile_6', 'Images/brownpi.png', 'lb'),
              'lb_3':Piece(450, 150,'tile_11', 'Images/brownpi.png', 'lb'), 'lb_4':Piece(550, 150,'tile_12', 'Images/brownpi.png', 'lb')}
    db_pieces = {'db_1': Piece(50, 450, 'tile_25', 'Images/darkbrownpi.png', 'db'),
                 'db_2': Piece(150, 450, 'tile_26', 'Images/darkbrownpi.png', 'db'),
                 'db_3': Piece(50, 550, 'tile_31', 'Images/darkbrownpi.png', 'db'),
                 'db_4': Piece(150, 550, 'tile_32', 'Images/darkbrownpi.png', 'db')}

    # """Testing victory conditions >>>>"""
    # lb_pieces = {'lb_1': Piece(50, 50, 'tile_25', 'Images/brownpi.png', 'lb'),
    #              'lb_2': Piece(350, 150, 'tile_26', 'Images/brownpi.png', 'lb'),
    #              'lb_3': Piece(250, 150, 'tile_31', 'Images/brownpi.png', 'lb'),
    #              'lb_4': Piece(250, 350, 'tile_32', 'Images/brownpi.png', 'lb')}
    # db_pieces = {'db_1': Piece(450, 50, 'tile_5', 'Images/darkbrownpi.png', 'db'),
    #              'db_2': Piece(550, 50, 'tile_6', 'Images/darkbrownpi.png', 'db'),
    #              'db_3': Piece(450, 150, 'tile_11', 'Images/darkbrownpi.png', 'db'),
    #              'db_4': Piece(550, 250, 'tile_12', 'Images/darkbrownpi.png', 'db')}

    def load_piece(piece_dict):
        piece_surfs = []

        for i in piece_dict:
            surface = pygame.image.load(piece_dict[i].image_path)
            piece_surfs.append(surface)



        return piece_surfs
    lb_piece_surfs = load_piece(lb_pieces)
    db_piece_surfs = load_piece(db_pieces)


    game = Game()
    game.run(tile_list, lb_piece_surfs, lb_pieces,db_piece_surfs, db_pieces, tiles )


main()
