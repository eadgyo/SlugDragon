from Point2D import Point2D
import math
class Vector2D:
    
    """z seulement utilise pour le calcul vectoriel"""
    def __init__(self, _value1 = 0.0, _value2 = 0.0, _value3 = 0.0):
        if(isinstance(_value1, (tuple, list))):
            self.x = _value1[0]
            self.y = _value1[1]
            self.z = 0.0
            
        elif(isinstance(_value1, (int, float))):
            self.x = _value1
            self.y = _value2
            self.z = _value3
            
        elif(isinstance(_value1, Point2D) and isinstance(_value2, Point2D)):
            self.x = _value2.x - _value1.x
            self.y = _value2.y - _value1.y
            self.z = _value2.z - _value1.z
        
        else:
            raise "Error: Initialisation par un element de type inconnu"
        
    
    def define(self, _value1, _value2 = 0.0, _value3 = 0.0):
        if(isinstance(_value1, (tuple, list))):
            self.x = _value1[0]
            self.y = _value1[1]
            self.z = 0.0
        elif(isinstance(_value1, (int, float))):
            self.x = _value1
            self.y = _value2
            self.z = _value3
            
        elif(isinstance(_value1, Point2D)):
            self.x = _value2.x - _value1.x
            self.y = _value2.y - _value1.y
            self.z = _value2.z - _value1.z
    
    def magnitude(self):
        return math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)

    def normalize(self):
        l = self.magnitude()
        if(l>0):
            self.x *= (1.0/l)
            self.y *= (1.0/l)

    def getNormalize(self):
        l_v = Vector2D()
        l = self.magnitude()
        l_v.x = self.x * (1.0/l)
        l_v.y = self.y * (1.0/l)
        l_v.z = self.z * (1.0/l)
        return l_v

    def scalarProduct(self, _v):
        return self.x * _v.x + self.y * _v.y + self.z * _v.z
    
    def vectoriel(self, _v):
        l_v = Vector2D()
        l_v.x = self.y*_v.z - self.z*_v.y
        l_v.y = self.z*_v.x - self.x*_v.z
        l_v.z = self.x*_v.y - self.y*_v.x
        return l_v
    
    def colinear(self, _v):#2d
        if((self.x * _v.y - self.y * _v.x) == 0):#*100/100 = correct float precision
            return True
        return False

    def perpendicular(self):
        temp = self.x
        self.x = -self.y
        self.y = temp

    def getPerpendicular(self):
        l_v = Vector2D()
        l_v.x = -self.y
        l_v.y = self.x
        return l_v
    
    def getAngle(self, _v):
        scalar = self.getNormalize().scalarProduct(_v.getNormalize())
        if(scalar > 1):
            l_fTheta = 0.0
        elif(scalar < -1.0):
            l_fTheta = 180
        else:
            l_fTheta = math.acos(self.getNormalize().scalarProduct(_v.getNormalize()))
            
        if(self.vectoriel(_v).z > 0):
            l_fTheta = l_fTheta
        else:
            l_fTheta =  -l_fTheta
        return (l_fTheta*180)/math.pi
    
    def getList(self):
        return (self.x, self.y)
    
    def distTwoParralel(self, _v, _p1, _p2):
        if not self.colinear(_v):
            return -1.0
        l_v = self.getPerpendicular()
        l_P2DCollision = Point2D()
        l_P2DCollision.intersectionVector2D(l_v, _v, _p1, _p2);
        l_v.define(l_P2DCollision, _p1);
        return l_v.magnitude();
    
    



    """Operator"""
    def __add__(self, _value):
        if(isinstance(_value, Vector2D)):
            return Vector2D(self.x + _value.x,
                            self.y + _value.y,
                            self.z + _value.z)
        elif(isinstance(_value, Point2D)):
            return Point2D(self.x + _value.x,
                            self.y + _value.y,
                            self.z + _value.z)
        else:
            raise "Error: addition avec un element de type inconnu"
            
    def __iadd__(self, _value):
        return self.__add__(_value)
    
    """Multiplication par un scalaire"""
    def __mul__(self, _value):
        if(isinstance( _value, (int, float))):
            return Vector2D(self.x * _value, self.y * _value, self.z*_value)
        elif(isinstance(_value, Vector2D)):
            return self.scalarProduct(_value)
        else:
            raise "Error: multiplication par un element de type inconnu, autre qu un scalaire"

    def __imul__(self, _value):
        return self.__mul__(_value)
    

    
    """Vectoriel"""
    def __mod__(self, _v):
        return self.vectoriel(_v)
    
    def __neg__(self):
        return self*-1
    
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
        return Vector2D(self.x, self.y, self.z)
        