import pygame

class Button(pygame.sprite.Sprite):
  def __init__(self,pos,fn):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(fn)
    self.rect = self.image.get_rect()
    self.rect.y = pos[0]
    self.rect.y = pos[0]