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
        """Load the sprites that we need"""

        self.holds = pygame.sprite.Group()
        num_holds = 20
        for i in range(num_holds):
            x = random.randrange(40, 600)
            y = random.randrange(50, 300)
            name = "hold" + str(i)
            self.hold = (holds.Hold(name, x, y, 'assets/hold.png'))
            self.holds.add(self.hold)
            #self.holds.add(button.Button(x, y, 'assets/hold.png'))
        self.climber = climber.Climber("Angela", 300, 200, "assets/climber.png")
        #self.button = button.Button((250,250),'assets/button.png')
        self.all_sprites = pygame.sprite.Group((self.climber,self.holds) + tuple(self.holds))
        
        self.state = "GAME"

    def mainLoop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                  if(self.holds.rect.collidepoit(event.pos)):
                    self.climber.grab_hold(200,200)
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
            fights = pygame.sprite.spritecollide(self.climber, self.holds, True)
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
