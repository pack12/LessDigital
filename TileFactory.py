import random
class TileFactory:
    def __init__(self):
        self.imageList = []
    def randomImage(self):


        for i in range(36):

            rand_number = random.randint(1,16)

            if rand_number == 1:
                filePath = "Images/lessN.png"
                self.imageList.append(filePath)
            elif rand_number == 2:
                filePath = "Images/lessE.png"
                self.imageList.append(filePath)
            elif rand_number == 3:
                filePath = "Images/lessS.png"
                self.imageList.append(filePath)
            elif rand_number == 4:
                filePath = "Images/lessW.png"
                self.imageList.append(filePath)
            elif rand_number == 5:
                filePath = "Images/lessNS.png"
                self.imageList.append(filePath)
            elif rand_number == 6:
                filePath = "Images/lessNE.png"
                self.imageList.append(filePath)
            elif rand_number == 7:
                filePath = "Images/lessNW.png"
                self.imageList.append(filePath)
            elif rand_number == 8:
                filePath = "Images/lessSE.png"
                self.imageList.append(filePath)
            elif rand_number == 9:
                filePath = "Images/lessSW.png"
                self.imageList.append(filePath)
            elif rand_number == 10:
                filePath = "Images/lessWE.png"
                self.imageList.append(filePath)
            elif rand_number>= 11 and rand_number<=16:
                filePath = "Images/lessb.png"
                self.imageList.append(filePath)
        return self.imageList




