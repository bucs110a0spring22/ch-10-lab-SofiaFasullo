import pygame
import random
#model
class Climber(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name
        self.speed = 3
        self.health = 3
        self.shielded = False
    
    #make new method for shielded
    def shieldmode(self):
        self.image = pygame.image.load("assets/shieldturtle.png").convert_alpha()
        self.shielded = True

    #methods to make moving our hero easier
    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed

    def grab_hold(self,x,y):
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        self.rect.x = 200
        self.rect.y = 200
      

    def fight(self, opponent):
        print("successful attack")
        return True

