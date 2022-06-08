from TileFactory import TileFactory
from Tile import Tile
from Square import Square
from Board import Board
from Game import Game
def main():

    """ Creating Tile factory object that uses randomImage method to create imageListPaths"""
    fact = TileFactory()
    imageList = fact.randomImage()


    """ Creating Tile object from Tile class that uses createTile method to create dictionaires of tiles"""
    t = Tile()
    tiles = t.createTile(imageList)

    print("Main: {}".format(tiles))
    """ Creating sq object from sq class that groups tiles (that get converted to str) into a key
    value pair where we have: square_1: [tile_1, tile_2, tile_3, tile_4]"""
    sq = Square()
    squares = sq.createSquares(tiles)

    """ Creating board class that returns a tile_list which is a list of surfaces that go into 
    the game.run method"""
    board = Board()
    tile_list = board.display_board(squares,tiles)


    game = Game()
    game.run(tile_list)


main()
