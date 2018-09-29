from Maths.myRectangle import myRectangle
from Maths.Point2D import Point2D
from Animation.KeyFrames import KeyFrames
from Animation.AdvImage import AdvImage
from Maths.Vector2D import Vector2D
import pygame
"""Arbre"""
"""Correspond a chaque os/membre principal du squellette humain"""
class Bone:
    def __init__(self, _advImage):
        self.advImage = _advImage
        """Constituant principal de l arbre, un membre peut posseder des sous membres"""
        self.bone = []
        self.aKeyFrames = None
        self.time = 0.0
        self.iActualKey = -1
        self.velocityTheta = 0.0
        self.lastTheta = 0.0
    
    def clearAnimation(self, _vec):
        self.setThetaBone(0.0, _vec, self.advImage.p2DRotation)
        for i in range(0,len(self.bone)):
            self.bone[i].clearAnimation(self.getVec())
    
    """Toutes les cles ont ete jouees, on peut les effacer"""
    def resetAnimation(self):
        self.aKeyFrames = None
        self.time = 0.0
        self.iActualKey = -1
        self.velocityTheta = 0.0
    
    def initAnimation(self, _vec):
        self.time = 0.0
        self.iActualKey += 1
        self.lastTheta = self.advImage.getAngle(_vec)
        if(self.iActualKey < len(self.aKeyFrames.afEndT)):
            """Calcul de la vitesse de rotation entre 2 cles"""
            self.velocityTheta = -((self.advImage.getAngle(_vec) - self.aKeyFrames.afTheta[self.iActualKey])/(self.aKeyFrames.afEndT[self.iActualKey]))
            return False
        else:
            if(self.aKeyFrames.bRepeat and len(self.aKeyFrames.afEndT) > 0):
                """Si l animation se repete on remet la cle actuelle a 0"""
                self.iActualKey = 0
                """Calcul de la vitesse de rotation entre 2 cles"""
                self.velocityTheta = -((self.advImage.getAngle(_vec) - self.aKeyFrames.afTheta[self.iActualKey])/(self.aKeyFrames.afEndT[self.iActualKey]))
                return False
            else:
                self.resetAnimation()
                return True
  
    
    """Symetrie vertical"""
    def flipX(self, _p2DCenter = None):
        l_p2DCenter = self.advImage.p2DCenter
        if(_p2DCenter != None):
            l_p2DCenter = _p2DCenter
        self.advImage.flipX(l_p2DCenter)
        self.flipAnimationX()
        for i in range(0, len(self.bone)):
            self.bone[i].flipX(l_p2DCenter)
        
    
    def flipAnimationX(self):
        if(self.aKeyFrames != None):
            if(not self.aKeyFrames.bFlipX):
                """On travail sur une reference les modifications touchent l objet inital"""
                for i in range(0, len(self.aKeyFrames.afTheta)):
                    self.aKeyFrames.afTheta[i] = -self.aKeyFrames.afTheta[i]
                self.aKeyFrames.bFlipX = True

                
                
    def flipNormalAnimation(self):
        if(self.aKeyFrames != None):
            if(self.aKeyFrames.bFlipX):
                """On travail sur une reference les modifications touchent l objet inital"""
                for i in range(0, len(self.aKeyFrames.afTheta)):
                    self.aKeyFrames.afTheta[i] = -self.aKeyFrames.afTheta[i]
                self.aKeyFrames.bFlipX = False
                
    """translation relative a la dernier position"""
    def translateBone(self, _vec):
        self.advImage.translateImage(_vec)
        for i in range(0, len(self.bone)):
            self.bone[i].translateBone(_vec)
    
    """rotation relative, on ne connait pas l angle de depart avec le membre parent"""
    def rotateBone(self, _fTheta, _p2DcentRot = None):
        l_p2DcentRot = self.advImage.p2DRotation
        if(_p2DcentRot != None):
            l_p2DcentRot = _p2DcentRot
        self.advImage.rotateImage(_fTheta, l_p2DcentRot)
        for i in range(0, len(self.bone)):
            self.bone[i].rotateBone(_fTheta, l_p2DcentRot)
    
    """rotation absolue par rapport au membre parent"""
    def setThetaBone(self, _fTheta, _vec, _p2DcentRot = None):
        l_fTheta = -(self.advImage.getAngle(_vec) - _fTheta)
        l_p2DcentRot = self.advImage.p2DRotation
        if(_p2DcentRot != None):
            l_p2DcentRot = _p2DcentRot
        self.advImage.rotateImage(l_fTheta, l_p2DcentRot)
        for i in range(0, len(self.bone)):
            self.bone[i].rotateBone(l_fTheta, l_p2DcentRot)

    """agrandissement/retrecissement absolue par rapport a la premiere image"""
    def scaleBone(self, _fFactor, _p2DScaleCenter = None, _bRectOnly = False):
        l_p2DScaleCenter = self.advImage.p2DRotation
        if(_p2DScaleCenter != None):
            l_p2DScaleCenter = _p2DScaleCenter
        self.advImage.scaleImage(_fFactor, l_p2DScaleCenter, _bRectOnly = _bRectOnly)
        for i in range(0, len(self.bone)):
            self.bone[i].scaleBone(_fFactor, l_p2DScaleCenter, _bRectOnly)
    
    """On ajoute un membre"""
    def addBone(self, _advImage):
        self.bone.append(Bone(_advImage))
    
    """On met en place l animation en donnant des cles"""
    def setKeyFrames(self, _aKeyFrames):
        self.aKeyFrames = _aKeyFrames
        self.time = 0.0
        self.iActualKey = -1
        i = 0
        while(i<len(_aKeyFrames.aKeyFrames) and i<len(self.bone)):
            self.bone[i].setKeyFrames(_aKeyFrames.aKeyFrames[i])
            i += 1
        if(self.advImage.bFlipX):
            self.flipAnimationX()
        else:
            self.flipNormalAnimation()
        
    def update(self, dt, _vec):

        """Si des cles pour l animation sont presentes, on peut mettre a jour l animation"""
        if(self.aKeyFrames != None):
            if(self.iActualKey == -1 and self.initAnimation(_vec)):
                pass
            elif(self.iActualKey < len(self.aKeyFrames.afEndT)):
                self.time += dt
                if(self.time >= self.aKeyFrames.afEndT[self.iActualKey]):
                    self.setThetaBone(self.aKeyFrames.afTheta[self.iActualKey], _vec)
                    self.initAnimation(_vec)
                    
                elif(self.iActualKey < len(self.aKeyFrames.afTheta)):
                    if(not self.advImage.bFlipX):
                        self.setThetaBone(self.lastTheta + self.time * self.velocityTheta, _vec)   
                    else:
                        self.setThetaBone((self.lastTheta + self.time * self.velocityTheta), _vec)      
        """On met a jour les sous membres"""
        for i in range(0,len(self.bone)):
            self.bone[i].update(dt, Vector2D(self.advImage.aPoints[0], self.advImage.aPoints[3]))

    """bImage pour afficher les Images
    bRect pour afficher les rectangles lies au membre
    bLast pour n afficher que les derniers elements de l arbre
    bFirst pour n afficher que les premiers elements de l arbre"""
    
    """On se sert de bLast pour un test rapide et bFirst pour afficher les membres dans un ordre correspondant precis"""
    def display(self, _screen, _vec = Vector2D(), _bImage = True, _bRec = False, _bLast = False, _bFirst = False):
        if(not _bFirst):
            """On affiche les autres membres"""
            for i in range(len(self.bone) - 1, -1, -1):
                self.bone[i].display(_screen, _vec, _bImage, _bRec, _bLast)
        
        if(_bLast):
            if(len(self.bone) == 0):
                """l arbre est vide, on est au dernier membre, on peut l afficher"""
                if(_bImage):
                    self.advImage.display(_screen, _vec)
                if(_bRec):
                    pygame.draw.line(_screen, [255,0,0], (self.advImage.p2DRotation.x - 4 + _vec.x,self.advImage.p2DRotation.y + _vec.y),
                                      (self.advImage.p2DRotation + _vec).getList())
                    self.advImage.drawRectangle(_screen, _vec)
        else:
            if(_bImage):
                    self.advImage.display(_screen, _vec)
            if(_bRec):
                pygame.draw.line(_screen, [255,0,0], (self.advImage.p2DRotation.x - 4 + _vec.x,self.advImage.p2DRotation.y + _vec.y),
                                      (self.advImage.p2DRotation + _vec).getList())
                self.advImage.drawRectangle(_screen, _vec)
                
    def getVec(self):
        return Vector2D(self.advImage.aPoints[0], self.advImage.aPoints[3])
        
    def getCenter(self):
        return self.advImage.p2DCenter
    
    def getLowerY(self):
        l_Lower = self.advImage.aPoints[0].y
        for i in range(1,4):
            if(l_Lower < self.advImage.aPoints[i].y):
                l_Lower = self.advImage.aPoints[i].y
        return l_Lower
    
    def getLowerX(self):
        l_Lower = self.advImage.aPoints[0].x
        for i in range(1,4):
            if(l_Lower < self.advImage.aPoints[i].x):
                l_Lower = self.advImage.aPoints[i].x
        return l_Lower
    
    def getHigherY(self):
        l_Higher = self.advImage.aPoints[0].y
        for i in range(1,4):
            if(l_Higher > self.advImage.aPoints[i].y):
                l_Higher = self.advImage.aPoints[i].y
        return l_Higher
    
    def getHigherX(self):
        l_Higher = self.advImage.aPoints[0].x
        for i in range(1,4):
            if(l_Higher > self.advImage.aPoints[i].x):
                l_Higher = self.advImage.aPoints[i].x
        return l_Higher