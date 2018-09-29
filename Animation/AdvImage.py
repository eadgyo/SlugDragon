import pygame
from Maths.myRectangle import myRectangle
from Maths.Point2D import Point2D
from Maths.Vector2D import Vector2D
from types import NoneType
"""_aSprites pour a == array"""
class AdvImage(myRectangle):
    def __init__(self, _aSprites, _p2DCenter = None, _p2DRotation = None, _p2DDist = None, _fTheta = 0.0):
        l_aSprites = _aSprites
        if(not isinstance(_aSprites, (list, tuple))):
            l_aSprites = [_aSprites]
        if(_p2DDist == None):
            """On va creer un rectangle en recuperant le rectangle de l image"""
            myRectangle.__init__(self, rec = l_aSprites[0].get_rect())
            self.p2DRotation = self.p2DCenter  
        else:
            """On cree un rectangle avec les dimensions donnees"""
            myRectangle.__init__(self, _p2DCenter, _p2DDist, 0.0)
            self.p2DRotation = _p2DRotation

        self.bFlipX = False
        self.iActualImage = 0
        self.aSprites = l_aSprites
        self.scaledImage = l_aSprites[0]
        self.rotImage = l_aSprites[0]
        self.scaleImage(1.0)
        self.rotateImage(_fTheta)
        if(_p2DCenter != None):
                self.setPosition(_p2DCenter)
    
    def flipX(self, _p2DCenter):
        myRectangle.flipY(self, _p2DCenter)
        self.p2DRotation.flipY(_p2DCenter)
        self.flipImageX()
        self.bFlipX = not self.bFlipX

    def flipImageX(self):
        self.scaledImage = pygame.transform.flip(self.scaledImage, False, True)
        self.rotate(0)
    
    def define(self, _p2DCenter = Point2D(), _p2DDist = Point2D(), _p2DRotation = None, _fTheta = 0.0):
        myRectangle.define(self, _p2DCenter, _p2DDist, _fTheta)
        assert(isinstance(_p2DRotation, (NoneType, Point2D))), 'Error advImage define, P2d est un Float'
        if(_p2DRotation != None):
            self.p2DRotation = _p2DRotation
        
    
    """Translation relative a la derniere position"""
    def translateImage(self, _vec):
        self.translate(_vec)
        self.p2DRotation += (_vec)
    
    """Rotation relative au dernier angle, on prend l image mise a l echelle pour effectuer une rotation"""
    def rotateImage(self, _fTheta, _p2DcentRot = None):
        l_p2DcentRot = self.p2DCenter
        if(_p2DcentRot != None):
            l_p2DcentRot = _p2DcentRot
        self.rotate(_fTheta, _p2DcentRot)
        self.p2DRotation.rotate(_fTheta, l_p2DcentRot)
        if(self.scaledImage != None):
            self.rotImage = pygame.transform.rotate(self.scaledImage, self.fTheta)
    
    def setPosition(self, _p2DPos):
        self.translateImage(Vector2D(self.p2DCenter, _p2DPos))
        
    """Mise a l echelle absolue, on reprend l image non retoucher l agrandissement"""
    def scaleImage(self, _fScale = 1.0, _p2DcentScale = None, _fLength = None, _bRectOnly = False):
        l_p2DcentScale = self.p2DCenter
        l_fScale = _fScale
        if(_p2DcentScale != None):
            l_p2DcentScale = _p2DcentScale
        if(_fLength != None):
            l_fScale = _fLength/float(self.p2DLength.y)
        self.scale(l_fScale, l_p2DcentScale)
        self.p2DRotation.scale(l_fScale, l_p2DcentScale)
        if(self.scaledImage != None and not _bRectOnly):
            orig_rect = self.aSprites[self.iActualImage].get_rect()
            self.scaledImage = pygame.transform.scale(self.aSprites[self.iActualImage], (abs(int(l_fScale * orig_rect.width)),abs(int(l_fScale * orig_rect.height))))
        if(self.bFlipX):
            self.flipImageX()
        self.rotateImage(0)
    
    """Affichage de l image avec rotation et mise a l echelle"""
    def display(self, _screen, _vec):
        if(self.scaledImage != None):
            rot_rect = self.rotImage.get_rect()
            l_p2DImageCenter = Point2D(self.p2DCenter.x - rot_rect.width * 0.5 + _vec.x,
                                  self.p2DCenter.y - rot_rect.height * 0.5 + _vec.y)
            _screen.blit(self.rotImage, l_p2DImageCenter.getList(), self.rotImage.get_rect())

            
    """Operator"""
    """getter"""
    def __getitem__(self, _indice):
        assert(_indice < len(self.aSprites)), "Error: indice superieur aux nombres d AdvImage"
        return self.aSprites[_indice]

    def __len__(self):
        return len(self.aSprites)