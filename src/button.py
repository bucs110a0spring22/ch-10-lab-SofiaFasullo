import pygame

class Button(pygame.sprite.Sprite):
  def __init__(self,x,y,fn):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(fn)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y