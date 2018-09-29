from Maths import myRectangle
from Animation.Skeleton import Skeleton

class AI (Skeleton) :
    def __init__(self, _mass, _pos, _velocity, _accelerat, _life, _image) :
        Skeleton.__init__(self, _mass, _pos, _velocity, _accelerat, _life, _image)
        self.show = False
        self.alive = True
        
    def enemy_commands(self, entity) :
        pass