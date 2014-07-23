import png #The pypng library
import random
from pygame.locals import *
from pygameUtil import *

r = random.Random()
r.seed()
SIZE = 1025

class HeightMap:
    def __init__(self):
        self.tiles = []
        for i in range(SIZE):
            self.tiles.append( [] )
            for k in range(SIZE):
                self.tiles[i].append(0.0)

        self.max = 1.0
        self.min = 0.0

        self.range = 4.0
        self.divisor = 1.5

        seed = random.random()
        self.tiles[0][0] = seed
        self.tiles[SIZE-1][0] = seed
        self.tiles[0][SIZE-1] = seed
        self.tiles[SIZE-1][SIZE-1] = seed

    def dsGetValue(self, points):
        val = 0.0
        for p in points:
            if p[0] < 0:
                p[0] = -1*p[0]
                p[0] = SIZE - p[0] - 1
            else:
                p[0] = p[0] % SIZE

            if p[1] < 0:
                p[1] = -1*p[1]
                p[1] = SIZE - p[1] - 1
            else:
                p[1] = p[1] % SIZE
            val += self.tiles[p[1]][p[0]]/4

        val += r.random()*self.range - self.range/2
        return val

    def diamondSquare(self):
        step = SIZE - 1

        while step > 1:
            #Diamond Step
            for y in range(0, SIZE-1, step ):
                for x in range(0, SIZE-1, step ):
                    sx = x + step/2
                    sy = y + step/2
                    points = [[x, y],
                            [x+step,y],
                            [x,y+step],
                            [x+step,y+step]];
                    self.tiles[sy][sx] = self.dsGetValue( points )
                    val = self.tiles[sy][sx]

                    #Update min/max values
                    if self.min > val:
                        self.min = val
                    if self.max < val:
                        self.max = val

            #Square Step
            for y in range(0, SIZE - 1, step ):
                for x in range(0, SIZE-1, step ):
                    hs = step/2
                    x1 = x + hs
                    y1 = y
                    x2 = x
                    y2 = y + hs

                    points1 = [[x1 - hs,y1],[x1,y1-hs],[x1+hs,y1],[x1,y1+hs]]
                    points2 = [[x2-hs,y2],[x2,y2-hs],[x2+hs,y2],[x2,y2+hs]]
                    
                    self.tiles[y1][x1] = self.dsGetValue( points1 )
                    self.tiles[y2][x2] = self.dsGetValue( points2 )

                    #See if any wrapping needs to occur, this allows for
                    #tiling and gets rid of weirdness on the edges
                    if x1 == 0:
                        self.tiles[y1][SIZE - 1] = self.tiles[y1][x1]

                    if y1 == 0:
                        self.tiles[SIZE - 1][x1] = self.tiles[y1][x1]

                    if x1 == SIZE - 1:
                        self.tiles[y1][0] = self.tiles[y1][x1]

                    if y1 == SIZE - 1:
                        self.tiles[0][x1] = self.tiles[y1][x1]

                    if x2 == 0:
                        self.tiles[y2][SIZE - 1] = self.tiles[y2][x2]

                    if y2 == 0:
                        self.tiles[SIZE - 1][x2] = self.tiles[y2][x2]

                    if x2 == SIZE - 1:
                        self.tiles[y2][0] = self.tiles[y2][x2]

                    if y2 == SIZE - 1:
                        self.tiles[0][x2] = self.tiles[y2][x2]


                    #Update min/max if we need to
                    val = self.tiles[y1][x1]
                    if self.min > val:
                        self.min = val
                    if self.max < val:
                        self.max = val

                    val = self.tiles[y2][x2]
                    if self.min > val:
                        self.min = val
                    if self.max < val:
                        self.max = val

            self.range /= self.divisor
            step /= 2

    def getNormalized(self):
        result = []
        for y in range(SIZE):
            result.append( [] )
            for x in range( SIZE ):
                result[y].append( (self.tiles[y][x] - self.min)/(self.max-self.min) )

        return result

    def getGrayscaleImg(self):
        img = []
        for y in range(0,SIZE):
            img.append( [] )
            for x in range(0,SIZE):
                norm_val = (self.tiles[y][x] - self.min)/(self.max-self.min)
                img[y].append( int(norm_val*255) )

        return img

    def getColorImg(self):
        img = []

        for y in range(SIZE):
            img.append([])
            for x in range(SIZE):
                norm_val = (self.tiles[y][x] - self.min)/(self.max-self.min)

                color = [0,0,0]
                if norm_val < .5:
                    color = [0,0,255]
                elif norm_val < .75:
                    color = [0,255,0]
                else:
                    color = [127,81,1]
                
                img[y].append( int(color[0]) )
                img[y].append( int(color[1]) )
                img[y].append( int(color[2]) )

        return img

    def getTiledImg(self, w, h):
        base = self.getColorImg()

        img_1 = []
        for y in range(SIZE):
            img_1.append([])
            for i in range(w):
                img_1[y].extend( base[y] )
        
        img = []
        for i in range(h):
            img.extend( img_1 )

        return img


if __name__ == "__main__":
    foo = HeightMap()

    foo.diamondSquare()
    f = open( "grayscale.png", "wb" )
    w = png.Writer( SIZE, SIZE, greyscale=True )
    w.write(f, foo.getGrayscaleImg() )
    f.close()

    f = open( "color.png", "wb" )
    w = png.Writer( SIZE*1, SIZE*1)
    w.write( f, foo.getTiledImg( 1 , 1 ) )
    f.close()

