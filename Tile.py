from TileFactory import TileFactory

class Tile:



    def createTile(self, imagePathList):
        # tileFactory = TileFactory()
        imageList = imagePathList

        x,y=50,50
        tiles = {}
        for i in range(1,37):
            image_cap = imageList[i-1][11:13]
            image_path = imageList[i-1]

            if "." in image_cap:

                image_cap = image_cap.removesuffix('.')
            tile = 'tile_' + str(i)
            if x==550:
                tiles[tile] = {'isSelected': False, 'isOcuppied': False, 'type': image_cap, 'imagePath': image_path,
                               'center': (x, y)}
                x=50
                y+=100
            else:

                tiles[tile] = {'isSelected': False, 'isOcuppied': False, 'type': image_cap, 'imagePath': image_path,
                               'center': (x,y)}
                x += 100







        print("Tile.py: {}".format(tiles))
        return tiles



