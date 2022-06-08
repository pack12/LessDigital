class Square:
    def createSquares(self,tiles):
        # t = Tile()
        # tiles = t.createTile()

        squares ={}
        square_number = 1
        square_list = []

        for i in range(9):
            square = 'square_' + str((square_number))
            squares[square] = []
            square_number+=1

        square_number = 1
        for i in tiles:

            square = 'square_' + str((square_number))

            num_slice = i[len(i)-2:]

            if '_' in num_slice:
                num_slice = num_slice.removeprefix('_')
            num_slice = int(num_slice)
            if num_slice % 4 ==0:
                squares[square].append(i)
                square_number+=1
            else:
                squares[square].append(i)

        # print(squares)
        return squares