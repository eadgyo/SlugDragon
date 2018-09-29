import pygame
from Maths.Point2D import Point2D

class SpriteSheet:
    def __init__(self, _fileName, _distFrame):
        try:
            self.sprites = pygame.image.load(_fileName).convert_alpha()
        except IOError:
            print 'file does not exist: ', _fileName
        
        self.dist = _distFrame
        #get number of frames in the image
        self.colLin = Point2D(self.sprites.get_width()/self.dist.x,
                              self.sprites.get_height()/self.dist.y)
    
    def loadFrame(self, _beginframe):
        assert(_beginframe < self.colLin.x * self.colLin.y), ('beginFrame over image limit ' + str(_beginframe))
        leftPoint = Point2D((_beginframe%self.colLin.x)*self.dist.x,
                            int(_beginframe/self.colLin.x)*self.dist.y)
        pyRect = pygame.Rect(leftPoint.getList(), self.dist.getList())
        image = pygame.Surface(pyRect.size, flags=pygame.SRCALPHA)
        image.blit(self.sprites, (0,0), pyRect)
        return image
    
    def loadFrames(self, _beginFrame, _numberOfFrames):
        frames = []
        i = _beginFrame
        while i < _beginFrame + _numberOfFrames:
            frames.append(self.loadFrame(i))
            i += 1
        return frames