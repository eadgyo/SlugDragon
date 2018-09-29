import pygame

class Input :
    def __init__(self) :
        self.keys = {'Left': pygame.K_q, #Remplacer par pygame.K_a si clavier en Azerty
                     'Down': pygame.K_s,
                     'Right': pygame.K_d,
                     'Run': pygame.K_LSHIFT,
                     'Jump': pygame.K_SPACE,
                     'Echap': pygame.K_ESCAPE}

        # Left / Down / Right / Run / Jump / Echap
        self.keysDown = [False, False, False, False, False, False]
        
        self.echap = False

        # Button / Pos
        self.mouse = [False, (0, 0)]
        self.mousePressed = False

    def update(self) :
        pygame.event.get()

        k = pygame.key.get_pressed()

        if k[self.keys['Left']] :
            if not k[self.keys['Right']] :
                self.keysDown[0] = True
        else :
            self.keysDown[0] = False

        if k[self.keys['Down']] :
            if not k[self.keys['Jump']] :
                self.keysDown[1] = True
        else :
            self.keysDown[1] = False

        if k[self.keys['Right']] :
            if not k[self.keys['Left']] :
                self.keysDown[2] = True
        else :
            self.keysDown[2] = False

        if k[self.keys['Run']] :
            self.keysDown[3] = True
        else :
            self.keysDown[3] = False

        if k[self.keys['Jump']] :
            self.keysDown[4] = True
        else :
            self.keysDown[4] = False

        if k[self.keys['Echap']] :
            if self.echap : 
                self.keysDown[5] = False
            else :
                self.echap = True
                self.keysDown[5] = True
        else :
            self.echap = False
            self.keysDown[5] = False

        if pygame.mouse.get_pressed()[0] :
            self.mouse[0] = True
        else :
            self.mouse[0] = False
        self.mouse[1] = pygame.mouse.get_pos()

    def get_key(self) :
        while 1 :
            event = pygame.event.poll()
            if event.type == pygame.KEYDOWN :
                return event.key

    def entityAction(self, g, entity, actions) :
        if 'Left' in actions :
            if 'Run' in actions :
                entity.velocity.x = -400
            else :
                entity.velocity.x = -200
        elif 'Right' in actions :
            if 'Run' in actions :
                entity.velocity.x = 400
            else :
                entity.velocity.x = 200
        else :
            entity.velocity.x = 0
        if 'Down' in actions :
            entity.down = True
        else :
            entity.down = False
        if 'Jump' in actions :
            if entity.velocity.y == 0 :
                g.jumpSound.play()
                entity.velocity.y = -1400
                entity.jump = True
        if 'Echap' in actions :
            g.pauseGame()
        if 'Shoot' in actions :
            g.addBullet(entity)
        return

    def player_commands(self) :
        action_list = []
        
        if self.keysDown[3] :
            action_list.append('Run')
        if self.keysDown[0] :
            action_list.append('Left')
        if self.keysDown[1] :
            action_list.append('Down')
        if self.keysDown[2] :
            action_list.append('Right')
        if self.keysDown[4] :
            action_list.append('Jump')
        if self.keysDown[5] :
            action_list.append('Echap')
        if self.mouse[0] :
            action_list.append('Shoot')
            action_list.append(self.mouse[1])

        return action_list

    ''' MENUS '''

    def updateMenu(self) :
        pygame.event.get()

        k = pygame.key.get_pressed()

        if k[self.keys['Echap']] :
            if self.echap : 
                self.keysDown[5] = False
            else :
                self.echap = True
                self.keysDown[5] = True
        else :
            self.echap = False
            self.keysDown[5] = False
        if pygame.mouse.get_pressed()[0] :
            if self.mousePressed :
                self.mouse[0] = False
            else :
                self.mousePressed = True
                self.mouse = [True, pygame.mouse.get_pos()]
        else :
            self.mousePressed = False
            self.mouse[0] = False

    def player_commands_menu(self, display) :
        if self.mouse[0] :
            (x, y) = self.mouse[1]
            if len(display.boutons) > 0 :
                if x >= display.boutons[0].left and x <= display.boutons[0].right :
                    for i in range(len(display.boutons)) :
                        if y >= display.boutons[i].top and y <= display.boutons[i].bottom :
                            return display.boutons_text[i]
        return 0

    def commands_menu(self, com, g) :
        if com != 0 :
            
            main = g.display.boutons_main
            pause = g.display.boutons_pause
            end = g.display.boutons_end
                
            if com == main[0] or com == pause[1] or com == end[0] :
                g.startGame()
            elif com == main[1] or com == end[1] :
                g.display.showHighScoresMenu(g)
            elif com == main[2] or com == pause[3] :
                g.display.showSettingsMenu()
            elif com == main[3] or com == pause[4] or com == end[3] :
                g.endGame()
            elif com == pause[2] or com == end[2] :
                g.display.showMainMenu()
            elif com == pause[0] :
                g.pauseGame()
                
        if g.input.keysDown[5] :
            if g.display.setting :
                g.display.hideSettingsMenu()
            elif g.display.highscore :
                g.display.hideHighScoresMenu()
            elif g.display.state == 'pause' :
                g.pauseGame()
            elif g.display.state == 'end' :
                g.display.showMenu()

    def input_box(self, display) :
        message = 'Name : '
        text = ''
        while 1 :
            display.clean()
            display.showText(message+text)
            display.show()

            k = self.get_key()

            if k == pygame.K_SPACE and len(text) > 0 :
                text = text + chr(k)
            elif k == pygame.K_BACKSPACE and text != '' :
                text = text[0:-1]
            elif k == pygame.K_RETURN and len(text) > 2 :
                break
            elif k <= 127 and len(text) < 15 :
                text = text + chr(k)

        return text