from Maths.Point2D import Point2D
from Maths.Vector2D import Vector2D
class KeyFrames:
    def __init__(self, _afEndT = [], _afTheta = [], _aVec = [], _bRepeat = True):
        self.aVec = _aVec
        self.afTheta = _afTheta
        self.afEndT = _afEndT
        self.aKeyFrames = []
        self.bRepeat = _bRepeat
        self.bFlipX = False
        
    def addKeyFrames(self, _afEndT = [], _afTheta = [], _aVec = [], _bRepeat = True):
        self.aKeyFrames.append(KeyFrames(_afEndT, _afTheta, _aVec,_bRepeat))