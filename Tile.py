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

        # clicked_tiles.append(selected_tile)
        if len(clicked_tiles) == 0:
            recent_tile = None
        else:

            recent_tile = clicked_tiles[-1]
        # print("Recent Tiles: ",recent_tile)

        # for i in clicked_tiles:
        #     if i == None:
        #         clicked_tiles.remove(i)




        if recent_tile == None:
            pass
        # elif tiles[recent_tile]['isOcuppied'] == False:
        #     tiles[recent_tile]['isSelected'] = False

        elif tiles[recent_tile]['isOcuppied'] == False:

            tiles[recent_tile]['isSelected'] = False

        elif tiles[recent_tile]['isOcuppied'] == True:

            tiles[recent_tile]['isSelected'] = True


        for i in tiles:
            if i != recent_tile:
                tiles[i]['isSelected'] = False
        print(clicked_tiles)
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
    def sort_clicked_tiles(self, current_tile, target_tile, tiles):

        if current_tile != None and target_tile != None:

            if tiles[current_tile]['isOcuppied'] == True:

                if tiles[target_tile]['isOcuppied'] == True:
                    tiles[target_tile]['isSelected'] = False
                    target_tile = current_tile
                    print('both are not great')
                    tiles[current_tile]['isSelected'] = False

                    return current_tile, target_tile
                elif tiles[target_tile]['isOcuppied'] == False:
                    return current_tile, target_tile


            else:
                return None, None
        else:
            return None, None
    def check_clicked_tiles(self, tiles, clicked_tiles):

        for i in clicked_tiles:
            if i != None:

                if tiles[i]['isOcuppied'] == False and tiles[i]['isSelected'] == False and clicked_tiles.index(i) == 0:
                    clicked_tiles.remove(i)
                    # clicked_tiles.remove(clicked_tiles[0])
                    # clicked_tiles.clear()
                    print('CheckedClicks: ',clicked_tiles)
            # elif i == None:
            #     clicked_tiles.remove(i)

            elif i == None:
                clicked_tiles.clear()

            else:
                pass



