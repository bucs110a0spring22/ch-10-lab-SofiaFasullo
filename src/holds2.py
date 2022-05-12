import pygame
import random
#model
class Hold2(pygame.sprite.Sprite):
    def __init__(self, x1,x2, y1,y2, img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(x1,x2)
        self.rect.y = random.randrange(y1,y2)
        #set other attributes
        #self.name = name + str(id(self))
        #self.speed = 2