import pygame
from Maths.Vector2D import Vector2D
import time

class Display :
    def __init__(self) :
        self.width = 1280
        self.height = 720
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window_position = Vector2D(0, 0)

        ''' DECORS '''
        
        self.background = None
        self.ground = None
        self.platforms = []

        ''' MENUS '''

        self.boutons = []
        self.boutons_text = []
        self.boutons_main = ['Start', 'HighScore', 'Settings', 'Quit']
        self.boutons_pause = ['Resume', 'Restart', 'Menu', 'Settings', 'Quit']
        self.boutons_end = ['Restart', 'HighScore', 'Menu', 'Quit']
        self.boutons_settings = ['Soon']
        self.boutons_scores = ['No Score']
        self.bouton_width = 200
        self.bouton_height = 80
        self.bouton_score_w = 300
        self.bouton_score_h = 50
        self.state = 'main'
        self.setting = False
        self.highscore = False
        
        self.myFont = pygame.font.Font('Others/Fonts/myFont.ttf', 36)

    def init(self) :
        self.window_position = Vector2D(0, 0)

    def update(self, g) :
        self.showBackground()
        for target in g.targets:
            if(target.life != 0) :
                target.image.display(self.window, self.window_position*-1)
        
        g.player.display(self.window, self.window_position*-1)
        #g.player.image.drawRectangle(self.window, self.window_position*-1)
        for platform in g.platforms :
            platform.image.display(self.window, self.window_position*-1)
            platform.image.drawRectangle(self.window, self.window_position*-1)
        
            
        for enemy in g.enemies :
            self.showEntity(enemy)
        for bullet in g.bullets :
            self.showEntity(bullet)
        self.showScore(g.score)
        self.show()

    def updatePosition(self, player) :
        if player.image.p2DCenter.x < self.width/3 :
            self.window_position.x = 0
        elif player.image.p2DCenter.x - self.width*2/3 > 8200 - self.width:
            self.window_position.x = 8200 - self.width
        else:
            if player.image.p2DCenter.x - self.window_position.x - self.width/3 < 0 :
                self.window_position.x = (player.image.p2DCenter.x - self.width/3)
            elif - player.image.p2DCenter.x + self.window_position.x + self.width*2/3 < 0 :
                self.window_position.x = (player.image.p2DCenter.x - self.width*2/3)

    def clean(self) :
        self.window.fill((255, 153, 0))

    def showBackground(self) :
        self.window.blit(self.background, (0, 0))

    def showEntity(self, entity) :
        entity.image.display(self.window, self.window_position*-1)

    def show(self) :
        pygame.display.flip()

    def showScore(self, score) :
        contenu = self.myFont.render(str(round(time.time() - score, 1)), 1, (255, 255, 255))
        self.window.blit(contenu, (0, 0))

    ''' MENUS '''

    def showMenu(self) :
        self.clean()
        if not self.setting and not self.highscore :
            if self.state == 'main' :
                self.showBoutons(self.boutons_main, self.bouton_width, self.bouton_height)
            elif self.state == 'pause' :
                self.showBoutons(self.boutons_pause, self.bouton_width, self.bouton_height)
            elif self.state == 'end' :
                self.showBoutons(self.boutons_end, self.bouton_width, self.bouton_height)
        else :
            if self.setting :
                self.showBoutons(self.boutons_settings, self.bouton_width, self.bouton_height)
            elif self.highscore :
                self.showBoutons(self.boutons_scores, self.bouton_score_w, self.bouton_score_h)
        self.show()

    def showSettingsMenu(self) :
        self.setting = True
        
    def hideSettingsMenu(self) :
        self.setting = False
        
    def showHighScoresMenu(self, g) :
        self.highscore = True
        scores_list = g.files.readFile('Others/Saves/scores.slug')
        pseudos = []
        scores = []
        top10 = []

        i = 1
        while i < len(scores_list) :
            pseudos.append(scores_list[i].split(' ')[0])
            scores.append(int(scores_list[i].split(' ')[1]))
            i += 1

        while len(pseudos) > 0 and len(top10) < 10 :
            rang = scores.index(min(scores))
            pseudo = pseudos[rang]
            score = scores[rang]
            top10.append(pseudo + ' : ' + str(score))
            pseudos.remove(pseudo)
            scores.remove(score)

        self.boutons_scores = top10

    def hideHighScoresMenu(self) :
        self.highscore = False

    def showMainMenu(self) :
        self.state = 'main'

    def showPauseMenu(self) :
        self.state = 'pause'

    def showEndMenu(self) :
        self.state = 'end'

    def showBoutons(self, text, w, h) :
        self.boutons = []
        self.boutons_text = text
        n = len(text)
        x = self.width/2 - w/2
        y = self.height/(n+1)
        bouton = pygame.Rect(x, 0, w, h)
        i = 0
        while i < n :
            bouton_i = bouton.move(0, y*(i+1) - h/2)
            self.boutons.append(bouton_i)
            contenu = self.myFont.render(text[i], 1, (255, 255, 255))
            contenu_rect = contenu.get_rect()
            pygame.draw.rect(self.window, (255, 0, 0), bouton_i, 0)
            self.window.blit(contenu,(bouton_i.centerx - contenu_rect.width/2, bouton_i.centery - contenu_rect.height/2))
            i += 1

    def showText(self, text) :
        x = self.width/2 - 400/2
        y = self.height/(2)
        box = pygame.Rect(x, y - 80/2, 400, 80)
        contenu = self.myFont.render(text, 1, (255, 255, 255))
        contenu_rect = contenu.get_rect()
        pygame.draw.rect(self.window, (0, 102, 255), box, 0)
        self.window.blit(contenu,(box.left + 20, box.centery - contenu_rect.height/2))