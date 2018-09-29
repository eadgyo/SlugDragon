import math
class Point2D:
    def __init__(self, _x = 0.0, _y = 0.0, _z = 0.0):
        self.x = _x
        self.y = _y
        self.z = _z

    def define(self, _x = 0.0, _y = 0.0, _z = 0.0):
        self.x = _x
        self.y = _y
        self.z = _z
    
    def addVec(self, _vec):
        self.x += _vec.x
        self.y += _vec.y
        self.z += _vec.z
    
    def translate(self, _v):
        self.x = self.x + _v.x
        self.y = self.y + _v.y
        self.z = self.z + _v.z

    def intersectionVector2D(self, _v1, _v2, _p1, _p2):
        from Vector2D import Vector2D
        if(_v1.x*_v2.y -_v2.x*_v1.y != 0):
            if(_v1.y != 0):
                self.y = (-(_p1.x*_v1.y-_p1.y*_v1.x)*_v2.y + (_p2.x*_v2.y-_p2.y*_v2.x)*_v1.y)/(_v1.x*_v2.y-_v2.x*_v1.y)
                self.x = (_p1.x*_v1.y-_p1.y*_v1.x+_v1.x*self.y)/_v1.y
            else:
                self.y = (-(_p2.x*_v2.y-_p2.y*_v2.x)*_v1.y + (_p1.x*_v1.y-_p1.y*_v1.x)*_v2.y)/(_v2.x*_v1.y-_v1.x*_v2.y)
                self.x = (_p2.x*_v2.y-_p2.y*_v2.x+_v2.x*self.y)/_v2.y
            return True
        return False
    
    """Methode complexe, revoir les cours de semestre 2 geometrie analytique"""
    def rotate(self, _fangle, _center):#2D
        l_fangle = (int(100000*_fangle)/100000)%360
        l_fTheta = -((l_fangle*math.pi)/180)
        l_x = self.x
        l_y = self.y
        self.x = math.cos(l_fTheta)*(l_x - _center.x) - math.sin(l_fTheta)*(l_y - _center.y) + _center.x
        self.y = math.cos(l_fTheta)*(l_y - _center.y) + math.sin(l_fTheta)*(l_x - _center.x) + _center.y
        self.z = 0
        
    def scale(self, _fscale, _center):#2D
        l_x = self.x
        l_y = self.y
        self.x = _fscale*(l_x - _center.x) + _center.x
        self.y = _fscale*(l_y - _center.y) + _center.y
        self.z = 0.0
        
    def flipX(self, _center):
        self.x = -self.x + 2*_center.x
        self.y = self.y
        self.z = 0.0 
   
    def flipY(self, _center):
        self.x = self.x
        self.y = -self.y + 2*_center.y
        self.z = 0.0
    

    
    def getList(self):
        return (self.x, self.y)
    
    
    
    
    
    """operators"""
    def __add__(self, _value):
        from Vector2D import Vector2D
        if(isinstance(_value, (Point2D, Vector2D))):
            return Point2D(self.x + _value.x,
                            self.y + _value.y,
                            self.z + _value.z)
        else:
            raise "Error: addition avec un element de type inconnu"
            
    def __iadd__(self, _value):
        return self.__add__(_value)
    
    def __mul__(self, _value):
        if(isinstance(_value, (int, float))):
            return Point2D(self.x * _value, self.y * _value, self.z*_value)
        else:
            raise "Error: multiplication par un element de type inconnu"
        
    def __imul__(self, _value):
        return self.__mul__(_value)

    """Accession de type tableau"""
    """getter"""
    def __getitem__(self, _indice):
        if(_indice == 0):
            return self.x
        elif(_indice == 1):
            return self.y
        elif(_indice == 2):
            return self.z
        else:
            raise AssertionError
    
    """setter"""
    def __setitem__(self, _indice, _value):
        if(_indice == 0):
            self.x = _value
        elif(_indice == 1):
            self.y = _value
        elif(_indice == 2):
            self.z = _value
        else:
            raise AssertionError
    
    def copy(self):
        return Point2D(self.x, self.y, self.z)
    