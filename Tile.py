from TileFactory import TileFactory
import pygame
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

    def draw_tiles(self, tile_list,win):
        # testing commits
        x, y = 0, 0
        numero = 0
        for i in tile_list:

            i = pygame.transform.scale(i, (100, 100))
            if x == 500:
                rect = i.get_rect()

                # pygame.draw.circle(i,'red',(i.get_width()/2, i.get_height()/2),5)

                win.blit(i, (x, y))
                # pygame.draw.circle(self.win, 'red', (x+50, y+50), 5)

                numero += 1
                x = 0
                y += 100
            else:

                win.blit(i, (x, y))

                x += 100
                numero += 1


    def highlight_tile(self, tiles,selected_tile, clicked_tiles):

        clicked_tiles.append(selected_tile)
        recent_tile = clicked_tiles[-1]
        # print("Recent Tiles: ",recent_tile)

        for i in clicked_tiles:
            if i == None:
                clicked_tiles.remove(i)


                # print(self.clicked_tiles)

        if recent_tile == None:
            pass
        # elif tiles[recent_tile]['isOcuppied'] == False:
        #     tiles[recent_tile]['isSelected'] = False

        else:


            tiles[recent_tile]['isSelected'] = True



        for i in tiles:
            if i != recent_tile:
                tiles[i]['isSelected'] = False
    def draw_red_rect(self, selected_tile, tiles,win):
        if selected_tile == None:
            pass
        else:

            if tiles[selected_tile]['isSelected'] == True:
                red_rect = pygame.Rect(tiles[selected_tile]['center'][0] - 50, tiles[selected_tile]['center'][1] - 50, 100, 100)
                pygame.draw.rect(win, 'red', red_rect, 5)



    def tile_selector(self, mouse_pos,tiles):
        # print(mouse_pos[0], mouse_pos[1])

        for i in tiles:

            if mouse_pos[0]>= tiles[i]['center'][0]-43 and mouse_pos[0]<=tiles[i]['center'][0]+ 43:

                # print("This is the tile selected: ", i, ":", tiles[i])
                if mouse_pos[1]>=tiles[i]['center'][1]-43 and mouse_pos[1]<=tiles[i]['center'][1]+43:






                    # print("Tile",i," ", tiles[i])

                    # print(type(i))
                    # (type(tiles[i]))

                    return i, tiles[i]
        return None, None




