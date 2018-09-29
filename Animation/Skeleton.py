from Maths.Point2D import Point2D
from Animation.Bone import Bone
from Animation.KeyFrames import KeyFrames
from Maths.Vector2D import Vector2D
from GamesFiles.Entity import Entity
from Animation.AdvImage import AdvImage

"""Skeleton correspond au squelette humain"""
class Skeleton(Entity):
    def __init__(self, _advImage, _velocity = Vector2D(), _accelerat = Vector2D(),  _mass = 0.0, _life = 0.0, _iVersion = 0):
        Entity.__init__(self, _mass, _velocity, _accelerat, _life, _advImage)
        self.iVersion = _iVersion
        self.bone = None
        self.AnimationFrames = []
        self.create()
        self.updateRectangle()
        self.actualAnim = 0
        self.bCanAim = True
        self.bSword = False
        
        
    def create(self):
        self.createSkeleton()
        self.createAnimation()
    
    """Creer la structure du squelette, voici a quoi il ressemble"""
    """
    ###############################################################
    ##########################oooooo###############################
    ##########################o####o###############################
    ##########################oooooo###############################
    ############################*##################################
    #########################********##############################
    #########################*##++##*##############################
    #########################*##++##*##############################
    #########################*##++##*##############################
    #########################***++***##############################
    #########################/##++#/###############################
    #########################/##++#/###############################
    #########################/#####/###############################
    ##########################/####/###############################
    ###########################/###/###############################
    ###########################/###/###############################
    ##########################/####//##############################
    ##########################////////#############################
    ###############################################################
    """
    
    def createSkeleton(self):
        """ Le buste: * """
        self.bone = Bone(AdvImage([self.image[12]], Point2D(140,180), Point2D(140,250), Point2D(100,150)))
        
        """ La tete: o """
        if(self.iVersion == 0):
            self.bone.addBone(AdvImage([self.image[11]], Point2D(150,85), Point2D(150,106), Point2D(65,80)))
        elif(self.iVersion == 1):
            self.bone.addBone(AdvImage([self.image[3]], Point2D(150,85), Point2D(150,106), Point2D(65,80)))
        
        """ Bras Droit: + """
        self.bone.addBone(AdvImage([self.image[2]], Point2D(130,180), Point2D(130,150), Point2D(60,90)))
        self.bone.bone[1].addBone(AdvImage([self.image[1]], Point2D(130,250), Point2D(130,222), Point2D(40,90)))
        self.bone.bone[1].bone[0].addBone(AdvImage([self.image[8]], Point2D(130,250), Point2D(135,275), Point2D(40,90)))
        self.bone.bone[1].bone[0].bone[0].addBone(AdvImage([self.image[10]], Point2D(145,300), Point2D(165,330), Point2D(50,100)))
        
        """ Bras Gauche: + """
        self.bone.addBone(AdvImage([self.image[2]], Point2D(130,180), Point2D(130,150), Point2D(60,90)))
        self.bone.bone[2].addBone(AdvImage([self.image[0]], Point2D(130,250), Point2D(130,222), Point2D(40,90)))
        self.bone.bone[2].bone[0].addBone(AdvImage([self.image[8]], Point2D(130,250), Point2D(135,275), Point2D(40,90)))
        if(self.iVersion == 0):
            self.bone.bone[2].bone[0].bone[0].addBone(AdvImage([self.image[14]], Point2D(190,275), Point2D(190,275), Point2D(180,60)))
        
        """ Jambe Droite: / """
        self.bone.addBone(AdvImage([self.image[5]], Point2D(135,280), Point2D(135,240), Point2D(60,120)))
        self.bone.bone[3].addBone(AdvImage([self.image[4]], Point2D(155,380), Point2D(150,330), Point2D(50,120)))
        self.bone.bone[3].bone[0].addBone(AdvImage([self.image[9]], Point2D(160,445), Point2D(150,430), Point2D(65,50)))
        
        """ Jambe Gauche: / """
        self.bone.addBone(AdvImage([self.image[6]], Point2D(135,280), Point2D(135,240), Point2D(60,120)))
        self.bone.bone[4].addBone(AdvImage([self.image[4]], Point2D(155,380), Point2D(150,330), Point2D(50,120)))
        self.bone.bone[4].bone[0].addBone(AdvImage([self.image[9]], Point2D(160,445), Point2D(150,430), Point2D(65,50)))
        
        if(self.iVersion == 0):
            self.bone.addBone(AdvImage([self.image[13]], Point2D(85,190), Point2D(150,106), Point2D(65,80)))
        
        """On initialise la taille, rotation, position"""
        self.bone.scaleBone(1.0)
        self.bone.setThetaBone(0, Vector2D(Point2D(), Point2D(1,0)))
        self.translate(Vector2D(100,0))
        
    """On creer des cles pour plusieurs animations"""
    def createAnimation(self):
        bFrame = 0.1
        bFrameN = 0.1
        bFrameW = 0.2
        bFrameR = 0.1
        bFrameJ = 0.1
        bFrameF = 0.1
        bFrameD = 0.1
        bFrameDW = 0.4
        bFrameDR = 0.2

        # NOTHING / WALK / RUN / JUMP / FALL / DOWN / DOWN_WALK / DOWN_RUN
        self.AnimationFrames = [KeyFrames([bFrameN], [0.0]),
                                KeyFrames([bFrameW], [0.0]),
                                KeyFrames([bFrameR], [-15.0]),
                                KeyFrames([bFrameJ], [0.0]),
                                KeyFrames([bFrameF], [0.0]),
                                KeyFrames([bFrameD], [-30.0]),
                                KeyFrames([bFrameDW], [-30.0]),
                                KeyFrames([bFrameDR], [-30.0])]

        # NOTHING
        self.AnimationFrames[0].addKeyFrames() #Tete
        self.AnimationFrames[0].addKeyFrames([bFrame], [0.0]) #BradD
        self.AnimationFrames[0].aKeyFrames[1].addKeyFrames([bFrame], [0.0]) #BradD
        self.AnimationFrames[0].addKeyFrames([bFrame], [0.0]) #BradG
        self.AnimationFrames[0].aKeyFrames[2].addKeyFrames([bFrame],[0.0]) #BradG

        self.AnimationFrames[0].addKeyFrames([bFrame], [0.0]) #JambeD
        self.AnimationFrames[0].aKeyFrames[3].addKeyFrames([bFrame], [0.0]) #jambeD
        self.AnimationFrames[0].aKeyFrames[3].aKeyFrames[0].addKeyFrames([bFrame], [0.0]) #JambeD
        self.AnimationFrames[0].addKeyFrames([bFrame], [0.0]) #JambeG
        self.AnimationFrames[0].aKeyFrames[4].addKeyFrames([bFrame], [0.0]) #JambeG
        self.AnimationFrames[0].aKeyFrames[4].aKeyFrames[0].addKeyFrames([bFrame], [0.0]) #JambeG

        #WALK
        self.AnimationFrames[1].addKeyFrames() #Tete
        self.AnimationFrames[1].addKeyFrames([bFrame, bFrame, bFrame, bFrame, bFrame, bFrame], [20.0, 10.0, 0.0, -10.0, 0.0, 10.0]) #BradD
        self.AnimationFrames[1].aKeyFrames[1].addKeyFrames([bFrame, bFrame, bFrame, bFrame, bFrame, bFrame], [20.0, 10.0, 0.0, 0.0, 0.0, 0.0]) #BradD
        self.AnimationFrames[1].addKeyFrames([bFrame, bFrame, bFrame, bFrame, bFrame, bFrame], [-10.0, 0.0, 10.0, 20.0, 10.0, 0.0]) #BradG
        self.AnimationFrames[1].aKeyFrames[2].addKeyFrames([bFrame, bFrame, bFrame, bFrame, bFrame, bFrame], [0.0, 0.0, 0.0, 20.0, 10.0, 0.0]) #BradG

        self.AnimationFrames[1].addKeyFrames([bFrame, bFrame, bFrame, bFrame, bFrame, bFrame], [-20.0, -10.0, 10.0, 20.0, 0.0, -10.0]) #JambeD
        self.AnimationFrames[1].aKeyFrames[3].addKeyFrames([bFrame, bFrame, bFrame, bFrame, bFrame, bFrame], [0.0, -20.0, -20.0, 0.0, 0.0, 0.0]) #JambeD
        self.AnimationFrames[1].aKeyFrames[3].aKeyFrames[0].addKeyFrames([bFrame, bFrame, bFrame, bFrame, bFrame, bFrame], [20.0, 0.0, 0.0, 0.0, 0.0, 10.0]) #JambeD
        self.AnimationFrames[1].addKeyFrames([bFrame, bFrame, bFrame, bFrame, bFrame, bFrame], [20.0, 0.0, -10.0, -20.0, -10.0, 10.0]) #JambeG
        self.AnimationFrames[1].aKeyFrames[4].addKeyFrames([bFrame, bFrame, bFrame, bFrame, bFrame, bFrame], [0.0, 0.0, 0.0, 0.0, -20.0, -20.0]) #JambeG
        self.AnimationFrames[1].aKeyFrames[4].aKeyFrames[0].addKeyFrames([bFrame, bFrame, bFrame, bFrame, bFrame, bFrame], [0.0, 0.0, 20.0, 10.0, 0.0, 0.0]) #JambeG

        #RUN
        self.AnimationFrames[2].addKeyFrames() #Tete
        self.AnimationFrames[2].addKeyFrames([bFrameR, bFrameR, bFrameR, bFrameR, bFrameR, bFrameR], [40.0, 20.0, 0.0, -20.0, 0.0, 20.0]) #BradD
        self.AnimationFrames[2].aKeyFrames[1].addKeyFrames([bFrameR, bFrameR, bFrameR, bFrameR, bFrameR, bFrameR], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0]) #BradD
        self.AnimationFrames[2].addKeyFrames([bFrameR, bFrameR, bFrameR, bFrameR, bFrameR, bFrameR], [-20.0, 0.0, 20.0, 40.0, 20.0, 0.0]) #BradG
        self.AnimationFrames[2].aKeyFrames[2].addKeyFrames([bFrameR, bFrameR, bFrameR, bFrameR, bFrameR, bFrameR], [100.0, 100.0, 100.0, 100.0, 100.0, 100.0]) #BradG

        self.AnimationFrames[2].addKeyFrames([bFrameR, bFrameR, bFrameR, bFrameR, bFrameR, bFrameR], [-15.0, -10.0, 45.0, 85.0, 35.0, 45.0]) #JambeD
        self.AnimationFrames[2].aKeyFrames[3].addKeyFrames([bFrameR, bFrameR, bFrameR, bFrameR, bFrameR, bFrameR], [0.0, -85.0, -100.0, -85.0, 0.0, -60.0]) #JambeD
        self.AnimationFrames[2].aKeyFrames[3].aKeyFrames[0].addKeyFrames([bFrameR, bFrameR, bFrameR, bFrameR, bFrameR, bFrameR], [30.0, 0.0, 0.0, 10.0, -20.0, 30.0]) #JambeD
        self.AnimationFrames[2].addKeyFrames([bFrameR, bFrameR, bFrameR, bFrameR, bFrameR, bFrameR], [85.0, 35.0, 45.0, -15.0, -10.0, 45.0]) #JambeG
        self.AnimationFrames[2].aKeyFrames[4].addKeyFrames([bFrameR, bFrameR, bFrameR, bFrameR, bFrameR, bFrameR], [-85.0, 0.0, -60.0, 0.0, -85.0, -100.0]) #JambeG
        self.AnimationFrames[2].aKeyFrames[4].aKeyFrames[0].addKeyFrames([bFrameR, bFrameR, bFrameR, bFrameR, bFrameR, bFrameR], [10.0, -20.0, 30.0, 30.0, 0.0, 0.0]) #JambeG

        # JUMP
        self.AnimationFrames[3].addKeyFrames() #Tete
        self.AnimationFrames[3].addKeyFrames([bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #BradD
        self.AnimationFrames[3].aKeyFrames[1].addKeyFrames([bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #BradD
        self.AnimationFrames[3].addKeyFrames([bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ], [0.0, 00.0, 0.0, 0.0, 0.0, 0.0]) #BradG
        self.AnimationFrames[3].aKeyFrames[2].addKeyFrames([bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #BradG

        self.AnimationFrames[3].addKeyFrames([bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #JambeD
        self.AnimationFrames[3].aKeyFrames[3].addKeyFrames([bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #JambeD
        self.AnimationFrames[3].aKeyFrames[3].aKeyFrames[0].addKeyFrames([bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #JambeD
        self.AnimationFrames[3].addKeyFrames([bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #JambeG
        self.AnimationFrames[3].aKeyFrames[4].addKeyFrames([bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #JambeG
        self.AnimationFrames[3].aKeyFrames[4].aKeyFrames[0].addKeyFrames([bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ, bFrameJ], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #JambeG

        # FALL
        self.AnimationFrames[4].addKeyFrames() #Tete
        self.AnimationFrames[4].addKeyFrames([bFrameF, bFrameF, bFrameF, bFrameF, bFrameF, bFrameF], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #BradD
        self.AnimationFrames[4].aKeyFrames[1].addKeyFrames([bFrameF, bFrameF, bFrameF, bFrameF, bFrameF, bFrameF], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #BradD
        self.AnimationFrames[4].addKeyFrames([bFrameF, bFrameF, bFrameF, bFrameF, bFrameF, bFrameF], [0.0, 00.0, 0.0, 0.0, 0.0, 0.0]) #BradG
        self.AnimationFrames[4].aKeyFrames[2].addKeyFrames([bFrameF, bFrameF, bFrameF, bFrameF, bFrameF, bFrameF], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #BradG

        self.AnimationFrames[4].addKeyFrames([bFrameF, bFrameF, bFrameF, bFrameF, bFrameF, bFrameF], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #JambeD
        self.AnimationFrames[4].aKeyFrames[3].addKeyFrames([bFrameF, bFrameF, bFrameF, bFrameF, bFrameF, bFrameF], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #JambeD
        self.AnimationFrames[4].aKeyFrames[3].aKeyFrames[0].addKeyFrames([bFrameF, bFrameF, bFrameF, bFrameF, bFrameF, bFrameF], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #JambeD
        self.AnimationFrames[4].addKeyFrames([bFrameF, bFrameF, bFrameF, bFrameF, bFrameF, bFrameF], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #JambeG
        self.AnimationFrames[4].aKeyFrames[4].addKeyFrames([bFrameF, bFrameF, bFrameF, bFrameF, bFrameF, bFrameF], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #JambeG
        self.AnimationFrames[4].aKeyFrames[4].aKeyFrames[0].addKeyFrames([bFrameF, bFrameF, bFrameF, bFrameF, bFrameF, bFrameF], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]) #JambeG

        # DOWN
        self.AnimationFrames[5].addKeyFrames() #Tete
        self.AnimationFrames[5].addKeyFrames([bFrameD], [0.0]) #BradD
        self.AnimationFrames[5].aKeyFrames[1].addKeyFrames([bFrameD], [50.0]) #BradD
        self.AnimationFrames[5].addKeyFrames([bFrameD], [0.0]) #BradG
        self.AnimationFrames[5].aKeyFrames[2].addKeyFrames([bFrameD], [0.0]) #BradG

        self.AnimationFrames[5].addKeyFrames([bFrameD], [30.0]) #JambeD
        self.AnimationFrames[5].aKeyFrames[3].addKeyFrames([bFrameD], [-100.0]) #JambeD
        self.AnimationFrames[5].aKeyFrames[3].aKeyFrames[0].addKeyFrames([bFrameD], [10.0]) #JambeD
        self.AnimationFrames[5].addKeyFrames([bFrameD], [120.0]) #JambeG
        self.AnimationFrames[5].aKeyFrames[4].addKeyFrames([bFrameD], [-90.0]) #JambeG
        self.AnimationFrames[5].aKeyFrames[4].aKeyFrames[0].addKeyFrames([bFrameD], [0.0]) #JambeG

        # DOWN_WALK
        self.AnimationFrames[6].addKeyFrames() #Tete
        self.AnimationFrames[6].addKeyFrames([bFrameDW, bFrameDW], [0.0, 0.0]) #BradD
        self.AnimationFrames[6].aKeyFrames[1].addKeyFrames([bFrameDW, bFrameDW], [50.0, 50.0]) #BradD
        self.AnimationFrames[6].addKeyFrames([bFrameDW, bFrameDW], [0.0, 0.0]) #BradG
        self.AnimationFrames[6].aKeyFrames[2].addKeyFrames([bFrameDW, bFrameDW], [0.0, 0.0]) #BradG

        self.AnimationFrames[6].addKeyFrames([bFrameDW, bFrameDW], [30.0, 120]) #JambeD
        self.AnimationFrames[6].aKeyFrames[3].addKeyFrames([bFrameDW, bFrameDW], [-100.0, -90.0]) #JambeD
        self.AnimationFrames[6].aKeyFrames[3].aKeyFrames[0].addKeyFrames([bFrameDW, bFrameDW], [10., 0.0]) #JambeD
        self.AnimationFrames[6].addKeyFrames([bFrameDW, bFrameDW], [120.0, 30.0]) #JambeG
        self.AnimationFrames[6].aKeyFrames[4].addKeyFrames([bFrameDW, bFrameDW], [-90.0, -100.0]) #JambeG
        self.AnimationFrames[6].aKeyFrames[4].aKeyFrames[0].addKeyFrames([bFrameDW, bFrameDW], [0.0, 10.0]) #JambeG

        # DOWN_RUN
        self.AnimationFrames[7].addKeyFrames() #Tete
        self.AnimationFrames[7].addKeyFrames([bFrameDR, bFrameDR], [0.0, 0.0]) #BradD
        self.AnimationFrames[7].aKeyFrames[1].addKeyFrames([bFrameDR, bFrameDR], [50.0, 50.0]) #BradD
        self.AnimationFrames[7].addKeyFrames([bFrameDR, bFrameDR], [0.0, 0.0]) #BradG
        self.AnimationFrames[7].aKeyFrames[2].addKeyFrames([bFrameDR, bFrameDR], [0.0, 0.0]) #BradG

        self.AnimationFrames[7].addKeyFrames([bFrameDR, bFrameDR], [30.0, 120]) #JambeD
        self.AnimationFrames[7].aKeyFrames[3].addKeyFrames([bFrameDR, bFrameDR], [-100.0, -90.0]) #JambeD
        self.AnimationFrames[7].aKeyFrames[3].aKeyFrames[0].addKeyFrames([bFrameDR, bFrameDR], [10., 0.0]) #JambeD
        self.AnimationFrames[7].addKeyFrames([bFrameDR, bFrameDR], [120.0, 30.0]) #JambeG
        self.AnimationFrames[7].aKeyFrames[4].addKeyFrames([bFrameDR, bFrameDR], [-90.0, -100.0]) #JambeG
        self.AnimationFrames[7].aKeyFrames[4].aKeyFrames[0].addKeyFrames([bFrameDR, bFrameDR], [0.0, 10.0]) #JambeG

        """On lance une animation, celle ci est en boucle"""
        #self.bone.setKeyFrames(self.AnimationFrames[1])
    
    """Translation relative a la derniere position"""
    def translate(self, _vec):
        self.bone.translateBone(_vec)
        
    def setPosition(self, _p2DPos):
        l_vec = Vector2D(self.bone.getCenter(), _p2DPos)
        self.bone.translateBone(l_vec)
    
    def scale(self, _fFactor = 1.0, _fLength = None, _bRectOnly = False):
        self.updateRectangle()
        l_fFactor = _fFactor
        if(_fLength != None):
            l_fFactor = _fLength/float(self.image.p2DLength.y)
        self.bone.scaleBone(l_fFactor, _bRectOnly = _bRectOnly)
    
    def clearAnimation(self):
        if(self.bone.advImage.bFlipX):
            self.bone.clearAnimation(Vector2D(Point2D(), Point2D(-1,0)))
        else:
            self.bone.clearAnimation(Vector2D(Point2D(), Point2D(1,0)))
    
    def flipX(self):
        self.bone.flipX(self.bone.getCenter())
        self.clearAnimation()
        self.bone.setKeyFrames(self.AnimationFrames[self.actualAnim])
       
    """On peut afficher rapidement le squelette sans ordre, ou avec un ordre precis pour avoir un effet "realiste"""
    """Le mode rapide correspond au mode debug, on peut voir les rectangles de collisions"""
    def display(self, _screen, _vec, _bImage = True, _bRec = False, _bLast = False):
        
        if(_bRec):
            self.bone.display(_screen, _vec, _bImage, _bRec, _bLast)
        else:
            if(self.bSword):
                """On n affiche l epee dans la main"""
                self.bone.bone[2].display(_screen, _vec)#bras D
            else:
                self.bone.bone[5].display(_screen, _vec)
                self.bone.bone[2].bone[0].bone[0].display(_screen, _vec, _bFirst = True)#bras D
                self.bone.bone[2].bone[0].display(_screen, _vec, _bFirst = True)#bras D
                self.bone.bone[2].display(_screen, _vec, _bFirst = True)#bras D
            self.bone.bone[0].display(_screen, _vec)#Tete
            self.bone.bone[4].display(_screen, _vec)#jambe G
            self.bone.bone[3].display(_screen, _vec)#jambe D
            self.bone.display(_screen ,_vec, _bFirst = True)
            self.bone.bone[1].display(_screen, _vec)#bras G

                
    """On met a jour le squelette, animation, agrandissement..."""
    def update(self, dt):
        self.setPosition(self.image.p2DCenter)
        Entity.update(self, dt)
        self.updateAnim()
        if(self.bone.advImage.bFlipX):
            self.bone.update(dt, Vector2D(Point2D(), Point2D(-1,0)))
        else:
            self.bone.update(dt, Vector2D(Point2D(), Point2D(1,0)))
        self.updateRectangle()
    
    def updateRectangle(self):
        l_fLower1 = self.bone.bone[3].bone[0].bone[0].getLowerY()
        l_fLower2 = self.bone.bone[4].bone[0].bone[0].getLowerY()
        l_fLower = l_fLower1
        if(l_fLower2 > l_fLower1):
            l_fLower = l_fLower2
        
        l_fHigher = self.bone.bone[0].getHigherY()
        l_p2DCenter = Point2D(self.image.p2DCenter.x, l_fLower/2 + l_fHigher/2)
        
        l_p2DDist = Point2D(self.image.p2DLength.x, l_fLower - l_fHigher)
        
        self.image.define(self.image.p2DCenter, l_p2DDist, _fTheta = self.image.fTheta)
        
        self.bone.translateBone(Vector2D(l_p2DCenter, self.image.p2DCenter))

    def updateAnim(self) :
        if self.down :
            if abs(self.velocity.x) == 200 :
                if self.actualAnim != 6 :
                    self.bone.setKeyFrames(self.AnimationFrames[6])
                    self.bCanAim = True
                    self.actualAnim = 6
                    return
            elif abs(self.velocity.x) == 400 :
                if self.actualAnim != 7 :
                    self.bone.setKeyFrames(self.AnimationFrames[7])
                    self.bCanAim = True
                    self.actualAnim = 7
                    return
            else :
                if self.actualAnim != 5 :
                    self.bone.setKeyFrames(self.AnimationFrames[5])
                    self.bCanAim = True
                    self.actualAnim = 5
                return
        elif self.jump :
            if self.actualAnim != 3 :
                self.bone.setKeyFrames(self.AnimationFrames[3])
                self.bCanAim = True
                self.actualAnim = 3
                return
        elif abs(self.velocity.x) == 200 :
            if self.actualAnim != 1 :
                self.bone.setKeyFrames(self.AnimationFrames[1])
                self.bCanAim = True
                self.actualAnim = 1
                return
        elif abs(self.velocity.x) == 400 :
            if self.actualAnim != 2 :
                self.bone.setKeyFrames(self.AnimationFrames[2])
                self.bCanAim = True
                self.actualAnim = 2
                return
        elif self.velocity.y < 0 :
            if self.actualAnim != 4 :
                self.bone.setKeyFrames(self.AnimationFrames[4])
                self.bCanAim = True
                self.actualAnim = 4
                return
        else :
            if self.actualAnim != 0 :
                self.bone.setKeyFrames(self.AnimationFrames[0])
                self.bCanAim = True
                self.actualAnim = 0
    
    
    def aim(self, _p2DMouse, _vec):
        if(self.bCanAim):
            l_vecCenterImage = Vector2D(_p2DMouse + _vec, self.image.p2DCenter)
            l_scalarProduct = l_vecCenterImage.scalarProduct(Vector2D(1,0))
            if(self.bone.advImage.bFlipX):
                if(l_scalarProduct < 0):
                    self.flipX()
            else:
                if(l_scalarProduct > 0):
                    self.flipX()
            if(self.down):
                if(self.bone.advImage.bFlipX):
                    add = 45
                else:
                    add = 25
            else:
                if(self.bone.advImage.bFlipX):
                    add = 85
                else:
                    add = 93
               
            l_vecRotGun = Vector2D(_p2DMouse + _vec, self.bone.bone[1].advImage.p2DRotation)
            if(self.bone.advImage.bFlipX):
                l_vecRotGun = - l_vecRotGun
            l_fTheta = l_vecRotGun.getAngle(Vector2D(1,0)) + self.bone.advImage.fTheta - add
            
            l_vec2 = self.bone.getVec()
            self.bone.bone[1].setThetaBone(l_fTheta, l_vec2)
            l_vec2 = self.bone.bone[1].getVec()
            self.bone.bone[1].bone[0].setThetaBone(0, l_vec2)
            l_vec2 = self.bone.bone[1].bone[0].getVec()
            self.bone.bone[1].bone[0].bone[0].setThetaBone(0, l_vec2)
        
    def shoot(self, _p2DMouse, _vec):
        l_p2DRotGun = self.bone.bone[1].bone[0].bone[0].bone[0].advImage.p2DRotation.copy()
        l_p2DCent = self.bone.bone[1].bone[0].bone[0].bone[0].advImage.aPoints[3]*0.82 + self.bone.bone[1].bone[0].bone[0].bone[0].advImage.aPoints[0]*0.18
        l_vecMousGun = Vector2D(l_p2DCent,
                            l_p2DRotGun)
        l_vecMousGun.normalize()
        return (-l_vecMousGun, l_p2DRotGun)