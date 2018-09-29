import pygame
import time
from GamesFiles.Input import Input
from GamesFiles.Display import Display
from GamesFiles.FileManager import FileManager
from GamesFiles.Entity import Entity
from Animation.AdvImage import AdvImage
from Maths.Vector2D import Vector2D
from Maths.Point2D import Point2D
from GamesFiles.SpriteSheet import SpriteSheet
from Animation.Skeleton import Skeleton

class Game :
    def __init__(self) :
        pygame.init()
        self.input = Input()
        self.display = Display()
        self.files = FileManager()
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.jumpSound = pygame.mixer.Sound("Others/Sounds/jump.wav")
        self.targetSound = pygame.mixer.Sound("Others/Sounds/target.wav")
        #self.targetSound = pygame.mixer.Sound("")
        self.reset()
        
    def reset(self):
        self.player = None
        self.enemies = []
        self.platforms = []
        self.targets = []
        self.bullets = []
        
        self.running = True
        self.paused = True
        self.fps = 60
        self.dt = 0
        self.last_dt = 0
        self.lastFrame = 0
        self.score = 0

        self.dt_weapon = 0
        self.current_bullets = 0
        self.max_bullets = 6
        self.dt_gun = 0.2
        self.dt_sword = 0
        
    def startGame(self) :
        self.reset()
        self.display.init()
        self.paused = False
        self.display.state = 'pause'
        self.loadLevel()
        self.score = time.time()
        self.lastFrame = time.time()

    def pauseGame(self) :
        if self.paused :
            self.paused = False
        else :
            self.paused = True

    def endGame(self) :
        self.paused= False
        self.running = False
        pygame.quit()

    def winGame(self) :
        self.score = time.time() - self.score
        self.paused = True
        self.display.state = 'end'
        name = self.input.input_box(self.display)
        self.files.saveFile('Others/Saves/scores.slug', str(name) + ' ' + str(int(self.score)))

    def updateTime(self) :
        self.clock.tick(self.fps)
        self.last_dt = self.dt
        self.dt = time.time() - self.lastFrame
        self.dt_weapon += self.dt
        if self.dt >= 0.5 :
            self.dt = 0
        self.lastFrame = time.time()

    def addBullet(self, entity) :
        if self.dt_weapon > self.dt_gun :
            if self.current_bullets < self.max_bullets :
                (vec, position) = self.player.shoot(Point2D(self.input.mouse[1][0], self.input.mouse[1][1]), -self.display.window_position)
                l_entityBullet = Entity(0, -vec*1000.0, Vector2D(0, 0), 0, 
                                           AdvImage([pygame.image.load('Others/Images/laser.png')],
                                                     position + vec*-50.0, _fTheta = vec.getAngle(Vector2D(1,0))))
                l_entityBullet.image.setPosition(position + vec*-50.0)
                self.bullets.append(l_entityBullet)
                self.dt_weapon = 0
                self.current_bullets += 1
            else :
                self.current_bullets = 0
                self.dt_weapon = -1

    def delBullet(self, bullet) :
        self.bullets.remove(bullet)
    
    def delTarget(self, target) :
        self.targets.remove(target)
        self.targetSound.play()
    
    def loadLevel(self) :
        images = SpriteSheet("Others/Images/sprite512.png", Point2D(42,42))
        buste = SpriteSheet("Others/Images/sprite1024.png", Point2D(84,84))
        seriesOfImages = images.loadFrames(0, 12)
        seriesOfImages2 = buste.loadFrames(0,3)
        for i in range(0, len(seriesOfImages2)):
            seriesOfImages.append(seriesOfImages2[i])
        sprites = AdvImage(seriesOfImages, Point2D(100,200))
        self.player = Skeleton(sprites,  Vector2D(0, 1), Vector2D(0, 10), 300, 1)
        self.player.scale(_fLength = 140, _bRectOnly = True)
        #self.player = Entity(200, Point2D(700, 200), Vector2D(0, 0), Vector2D(0, 10), 1, AdvImage([pygame.image.load('Others/Images/player.jpg').convert_alpha()]))
        self.player.image.scaleImage(_fLength = 140)
        self.display.background = pygame.image.load('Others/Images/background.jpg')
        #self.display.ground = AdvImage([pygame.image.load('Others/Images/ground.jpg')], Point2D(0, 700))
        #self.display.ground.scaleImage(_fLength = 20)
        #self.platforms.append(AdvImage([pygame.image.load('Others/Images/cube.jpg')], Point2D(1000, 485)))
        #self.platforms[0].scaleImage(_fLength = 280)
        #self.platforms.append(AdvImage([pygame.image.load('Others/Images/cube.jpg')], Point2D(2000, 0)))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/sol1.jpg')], Point2D(0, 429))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/sol1.jpg')], Point2D(276, 429))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/sol3.jpg')], Point2D(552, 429))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/palissade.jpg')], Point2D(1050, 200))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/batiment1.jpg')], Point2D(552, 250))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/sol.jpg')], Point2D(1050, 660))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/sol2.jpg')], Point2D(4911, 660))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/batiment2.jpg')], Point2D(1300, 460))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/batiment3.jpg')], Point2D(1510, 335))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/pont.jpg')], Point2D(2034, 350))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/batiment4.jpg')], Point2D(2450, 330))))
        
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/escalier1.jpg')], Point2D(3500, 540))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/escalier2.jpg')], Point2D(3620, 420))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/escalier3.jpg')], Point2D(3740, 300))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/escalier4.jpg')], Point2D(3860, 180))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/batiment8.jpg')], Point2D(4400, 540))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/pont1.jpg')], Point2D(4600, 540))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/batiment9.jpg')], Point2D(5000, 420))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/pont2.jpg')], Point2D(5200, 420))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/batiment10.jpg')], Point2D(6400, 360))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/batiment10.jpg')], Point2D(6400, 240))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/sol.jpg')], Point2D(6600, 660))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/batiment12.jpg')], Point2D(6400, 240))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/batiment13.jpg')], Point2D(6600, 580))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/batiment14.jpg')], Point2D(7300, 0))))
        self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/batiment15.jpg')], Point2D(6950, 420))))
        #self.platforms.append(Entity(image = AdvImage([pygame.image.load('Others/Images/end.jpg')], Point2D(7800, 150))))
        
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(300, 300)), life = 1))
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(1125, 600)), life = 1))
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(1065, 150)), life = 1))
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(1550, 290)), life = 1))
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(2250, 310)), life = 1))
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(3795, 260)), life = 1))
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(3915, 140)), life = 1))
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(5500, 80)), life = 1))
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(5600, 350)), life = 1))
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(5700, 80)), life = 1))
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(5800, 350)), life = 1))
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(5900, 80)), life = 1))
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(6000, 350)), life = 1))
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(6100, 80)), life = 1))
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(6200, 350)), life = 1))
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(7200, 80)), life = 1))        
        self.targets.append(Entity(image = AdvImage([pygame.image.load('Others/Images/target.png').convert_alpha()], Point2D(7500, 80)), life = 1))

        
        for i in range(len(self.platforms)):
            self.platforms[i].image.translateImage(Vector2D(Point2D(), self.platforms[i].image.p2DLength*0.5))
            