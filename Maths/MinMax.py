class MinMax:
    def __init__(self):
        self.xMin = 0.0
        self.xMax = 0.0
        self.yMin = 0.0
        self.yMax = 0.0
        

    def define(self, _p1, _p2):
        from Point2D import Point2D
        if(_p1.x <= _p2.x):
            self.xMax = _p2.x
            self.xMin = _p1.x
            
        else:
            self.xMax = _p1.x
            self.xMin = _p2.x
        
        if(_p1.y <= _p2.y):
            self.yMax = _p2.y
            self.yMin = _p1.y
        
        else:
            self.yMax = _p1.y
            self.yMin = _p2.y