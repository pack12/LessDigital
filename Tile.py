from TileFactory import TileFactory

class Tile:



    def createTile(self):
        tileFactory = TileFactory()
        imageList = tileFactory.randomImage()


        tiles = {}
        for i in range(1,37):
            image_cap = imageList[i-1][11:13]
            image_path = imageList[i-1]

            if "." in image_cap:

                image_cap = image_cap.removesuffix('.')


            tile = 'tile_' + str(i)
            tiles[tile] = {'isSelected': False, 'isOcuppied': False, 'type': image_cap, 'imagePath': image_path}




        # print(tiles)
        return tiles



def main():
    tile = Tile()

    tiles = tile.createTile()
main()