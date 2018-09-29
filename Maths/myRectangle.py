from Maths.Point2D import Point2D
from Maths.Vector2D import Vector2D
from Maths.MinMax import MinMax
import math
import pygame


class myRectangle:
    def __init__(self, _p2DCenter = Point2D(), _p2DDist = Point2D(), _fTheta = 0.0, rec = None):
        self.LastCollide = []
        if(rec == None):
            self.aPoints = [Point2D(),Point2D(),Point2D(),Point2D()]
            self.p2DCenter = _p2DCenter
            self.p2DLength = _p2DDist
            self.fTheta = _fTheta
            myRectangle.define(self, _p2DCenter, _p2DDist, _fTheta)
        else:
            self.aPoints = [Point2D(),Point2D(),Point2D(),Point2D()]
            self.p2DCenter = Point2D(rec.left/2 + rec.right/2, rec.top/2 + rec.bottom/2)
            self.p2DLength = Point2D(abs(rec.right - rec.left), abs(rec.bottom - rec.top))
            myRectangle.define(self, self.p2DCenter, self.p2DLength, _fTheta)
            
    def define(self, _p2DCenter = Point2D(), _p2DDist = Point2D(), _fTheta = 0.0):
        self.p2DCenter = _p2DCenter
        self.p2DLength = _p2DDist
        self.fTheta = _fTheta
        
        l_fTheta = ((_fTheta * math.pi)/180)
        self.aPoints[0].x = (_p2DCenter.x - (math.cos(l_fTheta)*0.5*_p2DDist.x) + (math.sin(l_fTheta)*0.5*_p2DDist.y))
        self.aPoints[0].y = (_p2DCenter.y - (math.sin(l_fTheta)*0.5*_p2DDist.x) - (math.cos(l_fTheta)*0.5*_p2DDist.y))
        self.aPoints[1].x = (_p2DCenter.x - (math.cos(l_fTheta)*0.5*_p2DDist.x) - (math.sin(l_fTheta)*0.5*_p2DDist.y))
        self.aPoints[1].y = (_p2DCenter.y - (math.sin(l_fTheta)*0.5*_p2DDist.x) + (math.cos(l_fTheta)*0.5*_p2DDist.y))
        self.aPoints[2].x = (_p2DCenter.x + (math.cos(l_fTheta)*0.5*_p2DDist.x) - (math.sin(l_fTheta)*0.5*_p2DDist.y))
        self.aPoints[2].y = (_p2DCenter.y + (math.sin(l_fTheta)*0.5*_p2DDist.x) + (math.cos(l_fTheta)*0.5*_p2DDist.y))
        self.aPoints[3].x = (_p2DCenter.x + (math.cos(l_fTheta)*0.5*_p2DDist.x) + (math.sin(l_fTheta)*0.5*_p2DDist.y))
        self.aPoints[3].y = (_p2DCenter.y + (math.sin(l_fTheta)*0.5*_p2DDist.x) - (math.cos(l_fTheta)*0.5*_p2DDist.y))
    
    def getVectors(self):
        l_aVec = []
        for i in range(0,4):
            l_aVec.append(Vector2D(self.aPoints[i], self.aPoints[(i+1)%4]))
        return l_aVec
    
    """Test de collision avec Rotation"""
    def collision(self, _rectangle, _withEdges = True, _insideOnly = False):
        """withEdges = avec ou sans les bords des rectangles
        insideOnly permet de detecter si un rectangle est dans un autre"""
        l_vector1 = Vector2D()
        l_vector2 = Vector2D()
        l_point = Point2D()
        l_compare = MinMax()
        for c in range(0,2):
            if(c==0):
                l_vector1.define(self.aPoints[0],self.aPoints[3])
                l_vector1.normalize()
    
                l_vector2.define(l_point,self.aPoints[0])
                l_compare.xMin = l_compare.xMax = l_vector2.scalarProduct(l_vector1)
                l_vector2.define(l_point,self.aPoints[3])
    
                if(l_vector2.scalarProduct(l_vector1) < l_compare.xMin):
                    l_compare.xMin = l_vector2.scalarProduct(l_vector1)
                elif(l_vector2.scalarProduct(l_vector1) > l_compare.xMax):
                    l_compare.xMax = l_vector2.scalarProduct(l_vector1)
            
            else:
                l_vector1.define(self.aPoints[0],self.aPoints[1])
                l_vector1.normalize()
    
                l_vector2.define(l_point,self.aPoints[0])
                l_compare.xMin = l_compare.xMax = l_vector2.scalarProduct(l_vector1)
                l_vector2.define(l_point,self.aPoints[1])
    
                if(l_vector2.scalarProduct(l_vector1) < l_compare.xMin):
                    l_compare.xMin = l_vector2.scalarProduct(l_vector1)
                elif(l_vector2.scalarProduct(l_vector1) > l_compare.xMax):
                    l_compare.xMax = l_vector2.scalarProduct(l_vector1)
            
    
            l_vector2.define(l_point,_rectangle.aPoints[0])
            l_compare.yMin = l_compare.yMax = l_vector2.scalarProduct(l_vector1)
            
            for i in range(0,4):
                l_vector2.define(l_point,_rectangle.aPoints[i])
                if(l_vector2.scalarProduct(l_vector1) < l_compare.yMin):
                    l_compare.yMin = l_vector2.scalarProduct(l_vector1)
                elif(l_vector2.scalarProduct(l_vector1) > l_compare.yMax):
                    l_compare.yMax = l_vector2.scalarProduct(l_vector1)
                    
            if(_insideOnly):
                if(_withEdges):
                    if((l_compare.xMax < l_compare.yMin) or (l_compare.xMin > l_compare.yMax) or
                        (l_compare.xMax > l_compare.yMax) or (l_compare.xMin < l_compare.yMin)):
                        return False
                else:
                    if((l_compare.xMax <= l_compare.yMin) or (l_compare.xMin >= l_compare.yMax) or
                        (l_compare.xMax >= l_compare.yMax) or (l_compare.xMin <= l_compare.yMin)):
                            return False
            else:
                if(_withEdges):
                    if((l_compare.xMax < l_compare.yMin) or (l_compare.xMin > l_compare.yMax)):
                        return False
                else:
                    if((l_compare.xMax <= l_compare.yMin) or (l_compare.xMin >= l_compare.yMax)):
                        return False
                
        return True

    
    def drawRectangle(self, screen, _vec, color = [255,255,255]):
        for i in range(0,4):
            pygame.draw.line(screen, color, (self.aPoints[i] + _vec).getList(), (self.aPoints[(i+1)%4] + _vec).getList())
    
    def translate(self, _vec):
        for i in range(0,4):
            self.aPoints[i] += _vec
        self.p2DCenter += _vec

    def rotate(self, _fTheta, _p2DcentRot = None):
        l_p2DcentRot = self.p2DCenter
        if(_p2DcentRot != None):
            l_p2DcentRot = _p2DcentRot
        for i in range(0,4):
            self.aPoints[i].rotate(_fTheta, l_p2DcentRot)
        if(_fTheta != 0):
            True
        self.p2DCenter.rotate(_fTheta, l_p2DcentRot)
        l_vec2 = Vector2D(Point2D(0,0), Point2D(1,0))
        self.fTheta = self.getAngle(l_vec2)
        
    def scale(self, _fFactor, _p2DCenterScale = None):
        l_p2DCenterScale = self.p2DCenter
        if(_p2DCenterScale != None):
            l_p2DCenterScale = _p2DCenterScale
        for i in range(0,4):
            self.aPoints[i].scale(_fFactor, l_p2DCenterScale)
        self.p2DLength = self.p2DLength * _fFactor
        self.p2DCenter.scale(_fFactor, l_p2DCenterScale)
    
    def flipX(self, _p2DCenter):
        self.p2DCenter.flipX(_p2DCenter)
        for i in range(0, 4):
            self.aPoints[i].flipX(_p2DCenter)
 
        
    def flipY(self, _p2DCenter):
        self.p2DCenter.flipY(_p2DCenter)
        for i in range(0, 4):
            self.aPoints[i].flipY(_p2DCenter)

    
    def getAngle(self, _vec):
        l_vec1 = Vector2D(self.aPoints[0], self.aPoints[3])
        l_fTheta = l_vec1.getAngle(_vec)
        return l_fTheta
        
        
    """getter"""
    def __getitem__(self, _indice):
        if(_indice >= 0 and _indice <=3):
            return self.aPoints[_indice]
        else:
            raise AssertionError
        
    def copy(self):
        return myRectangle(self.p2DCenter, self.p2DDist, self.fTheta)