import sys
import pygame
import random
from src import climber
from src import holds
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
        self.climber = climber.Climber("Angela", 300, 200, "assets/climber.png")
        self.screen.blit(self.climber.image,self.climber.rect)
        self.button1 = button.Button(random.randrange(40, 600),random.randrange(50, 300),'assets/hold.png')
        self.button2 = button.Button(random.randrange(40, 600),random.randrange(50, 300),'assets/hold.png')
        #self.screen.blit(self.button2.image,self.button2.rect)
        self.button3 = button.Button(random.randrange(40, 600),random.randrange(50, 300),'assets/hold.png')
        #self.screen.blit(self.button3.image,self.button3.rect)
        self.button4 = button.Button(random.randrange(40, 600),random.randrange(50, 300),'assets/hold.png')
        #self.screen.blit(self.button4.image,self.button4.rect)
        self.button5 = button.Button(random.randrange(40, 600),random.randrange(50, 300),'assets/hold.png')
        #self.screen.blit(self.button5.image,self.button5.rect)
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
            self.screen.blit(self.button1.image,self.button1.rect)
            self.screen.blit(self.button2.image,self.button2.rect)
            self.screen.blit(self.button3.image,self.button3.rect)
            self.screen.blit(self.button4.image,self.button4.rect)
            self.screen.blit(self.button5.image,self.button5.rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                  if(self.button1.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button1.rect.x,self.button1.rect.y)
                  elif(self.button2.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button1.rect.x,self.button1.rect.y)
                  elif(self.button3.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button3.rect.x,self.button3.rect.y)
                  elif(self.button4.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button4.rect.x,self.button4.rect.y)
                  elif(self.button5.rect.collidepoint(event.pos)):
                    self.climber.grab_hold(self.button5.rect.x,self.button5.rect.y)
                if event.type == pygame.KEYDOWN:
                    if(event.type == pygame.K_s):
                      self.background.fill((0, 250, 250))
                      self.screen.blit(self.background, (0, 0)) 
                      self.shield_sprites.draw(self.screen)
                    if(event.key == pygame.K_UP):
                        self.climber.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.climber.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.climber.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.climber.move_right()
                    elif(event.key == pygame.K_SPACE):
                        self.climber.shieldmode()

                      
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
