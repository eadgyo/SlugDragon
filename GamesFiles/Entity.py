from Maths.Vector2D import Vector2D
from Maths.Point2D import Point2D

class Entity:
    def __init__(self, mass = 0.0, velocity = Vector2D(), acceleration = Vector2D(), life = 0.0, image = None) :
        self.mass = mass
        self.velocity = velocity
        self.acceleration = acceleration
        self.life = life
        self.image = image
        self.last_position = self.image.p2DCenter.copy()
        self.down = False
        self.jump = False

    def manageCollision(self, _entity):
        x = False
        y = False
        vx = 0
        vy = 0
        if self.image.collision(_entity.image) :
            actual_pos = self.image.p2DCenter.copy()
            self.image.setPosition(Point2D(self.last_position.x, actual_pos.y))
            if self.image.collision(_entity.image) :
                y = True
                self.velocity.y = 0
            self.image.setPosition(Point2D(actual_pos.x, self.last_position.y))
            if self.image.collision(_entity.image) :
                x = True
                self.velocity.x = 0
            self.image.setPosition(actual_pos)
            while self.image.collision(_entity.image) :
                if x :
                    if actual_pos.x - self.last_position.x > 0 :
                        vx = -1
                    else :
                        vx = 1
                if y :
                    if actual_pos.y - self.last_position.y > 0 :
                        vy = -1
                    else :
                        vy = 1
                        self.velocity.y = 1
                if not x and not y :
                    if actual_pos.x - self.last_position.x > 0 :
                        vx = -1
                    else :
                        vx = 1
                    if actual_pos.y - self.last_position.y > 0 :
                        vy = -1
                    else :
                        vy = 1
                self.image.translate(Vector2D(vx, vy))

    def update(self, dt) :
        self.last_position = self.image.p2DCenter.copy()
        vx = self.velocity.x
        vy = self.mass*self.acceleration.y*dt + self.velocity.y
        if vy >= 0 :
            self.jump = False
        x = self.velocity.x*dt + self.image.p2DCenter.x
        y = self.mass*self.acceleration.y*0.5*dt*dt + self.velocity.y*dt + self.image.p2DCenter.y
        self.velocity.define(vx, vy)
        self.image.setPosition(Point2D(x, y))