import pygame
import random
#model

#the purpose of this addition is to introduce a shield to the game, but I wasn't sure how to keep the shield attached to the hero during the game so I just made a new identical hero with a shield (excuse my poor art skills) and decided to swap this hero in but pretend I was just adding a shield

class ShieldTurtle(pygame.sprite.Sprite):
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

    #methods to make moving our hero easier
    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed

  #with a shield, our hero is defended so they don't lose health 
    def fight(self, opponent):
      print("successful attack")
      return True
