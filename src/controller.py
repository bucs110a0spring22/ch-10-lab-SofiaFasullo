import sys
import pygame
import random
from src import climber
from src import rockwall
#from src import holds
from src import button


class Controller:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((200, 200, 200))  # set the background to grey
        pygame.font.init()  # you have to call this at the start, if you want to use this module.
        pygame.key.set_repeat(1, 50)  # initialize a held keey to act as repeated key strikes
        self.rockwall = rockwall.Rockwall(0,0,'assets/rockwall2.png')
        self.climber = climber.Climber("Angela", 300, 200, "assets/climber.png")
        self.button1 = button.Button(random.randrange(40, 600),random.randrange(50, 300),'assets/hold.png')
        self.button2 = button.Button(random.randrange(40, 600),random.randrange(50, 300),'assets/hold.png')
        self.button3 = button.Button(random.randrange(40, 600),random.randrange(50, 300),'assets/hold.png')
        self.button4 = button.Button(random.randrange(40, 600),random.randrange(50, 300),'assets/hold.png')
        self.button5 = button.Button(random.randrange(40, 600),random.randrange(50, 300),'assets/hold.png')
        self.button6 = button.Button(random.randrange(40, 600),random.randrange(50, 300),'assets/hold.png')
        self.button7 = button.Button(random.randrange(40, 600),random.randrange(50, 300),'assets/hold.png')
        self.button8 = button.Button(random.randrange(40, 600),random.randrange(50, 300),'assets/hold.png')
        self.button9 = button.Button(random.randrange(40, 600),random.randrange(50, 300),'assets/hold.png')
        self.button10 = button.Button(random.randrange(40, 600),random.randrange(50, 300),'assets/hold.png')
        self.current_time = 0
        self.current_time = pygame.time.get_ticks()
        self.start_hold_time = 0
        self.time_holding = 0
        pygame.display.flip()
        #self.all_sprites = pygame.sprite.Group((self.climber,self.button1,self.button2,self.button3,self.button4,self.button5))# + tuple(self.holds))
        self.state = "GAME"
        
        """Load the sprites that we need"""
    '''
        self.holds = pygame.sprite.Group()
        num_holds = 5
        for i in range(num_holds):
            x = random.randrange(40, 600)
            y = random.randrange(50, 300)
            name = "button" + str(i)
            #self.hold = (holds.Hold(name, x, y, 'assets/hold.png'))
            #self.holds.add(self.hold)
            #self.holds.add(button.Button(x, y, 'assets/hold.png'))
            self.name = button.Button(x,y,'assets/hold.png')
        self.climber = climber.Climber("Angela", 300, 200, "assets/climber.png")
        #self.button = button.Button(200,100,'assets/hold.png')
    '''

    def mainLoop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
        while self.state == "GAME":
            self.screen.blit(self.rockwall.image,self.rockwall.rect)
            self.screen.blit(self.climber.image,self.climber.rect)
            self.screen.blit(self.button1.image,self.button1.rect)
            self.screen.blit(self.button2.image,self.button2.rect)
            self.screen.blit(self.button3.image,self.button3.rect)
            self.screen.blit(self.button4.image,self.button4.rect)
            self.screen.blit(self.button5.image,self.button5.rect)
            self.screen.blit(self.button6.image,self.button6.rect)
            self.screen.blit(self.button7.image,self.button7.rect)
            self.screen.blit(self.button8.image,self.button8.rect)
            self.screen.blit(self.button9.image,self.button9.rect)
            self.screen.blit(self.button10.image,self.button10.rect)
            current_time = 0
            current_time = pygame.time.get_ticks()
            start_hold_time = 0
            
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                  if(self.button1.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button1.rect.x,self.button1.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                    #time_holding = current_time - start_hold_time
                    #while time_holding > 5000: #holding more than 5 seconds
                    #  self.climber.falling()
                  elif(self.button2.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button2.rect.x,self.button2.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button3.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button3.rect.x,self.button3.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button4.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button4.rect.x,self.button4.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button5.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button5.rect.x,self.button5.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button6.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button6.rect.x,self.button6.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button7.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button7.rect.x,self.button7.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button8.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button8.rect.x,self.button8.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button9.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button9.rect.x,self.button9.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                  elif(self.button10.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button10.rect.x,self.button10.rect.y)
                    #start_hold_time = 0
                    #start_hold_time = pygame.time.get_ticks()
                if event.type == pygame.KEYDOWN:
                  self.start_hold_time = pygame.time.get_ticks()
                  self.time_holding = current_time - start_hold_time
                while self.time_holding > 5000: #holding more than 5 seconds
                  self.climber.falling()
                  #print(self.climber.fatigue())
                  

                      
            # check for collisions
            '''       
            fights = pygame.sprite.spritecollide(self.climber, self.climber, True) #bs filler, will delete
            if(fights):
                for e in fights:
                    if(self.climber.fight(e)):
                        e.kill()
                        self.background.fill((250, 250, 250))
                    else:
                        self.background.fill((250, 0, 0))
                        self.holds.add(e)

            # redraw the entire screen
            #self.holds.update()
            self.screen.blit(self.background, (0, 0))
            if(self.climber.health == 0):
                self.state = "GAMEOVER"
            self.all_sprites.draw(self.screen)
            # update the screen
            pygame.display.flip()
            '''

    def gameOver(self):
        self.climber.kill()
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0, 0, 0))
        self.screen.blit(message, (self.width / 2, self.height / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
