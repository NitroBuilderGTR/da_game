# Essential / Required Imports
import pygame
import stats

# -------------------------------------------------------
# Basic Game Variables (Time, App Running Status, etc...)
run = True
pygame.init()
clock = pygame.time.Clock()
# -------------------------------------------------------
# Window Controls (Border, and Resizeable App Borders)
screen = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
# set title
pygame.display.set_caption('DA GAME')
# -------------------------------------------------------
# Login / Main Menu Text Logic
def show_text(text, colour, x, y):
      font = pygame.font.Font('freesansbold.ttf', 13)
      text_obj=font.render(text,True,colour)
      screen.blit(text_obj, (x, y))      
# -------------------------------------------------------
# The Error - Protection    
if run == True:
    print("DA GAME is [STATUS: ONLINE]")
else:
    print("DA GAME is [STATUS : OFFLINE :( ]")
# -------------------------------------------------------
# Floor Texture File Handler
floor = pygame.image.load("Wooden_floor.png")
class wood(pygame.sprite.Sprite):
      def __init__(self, width, height, x, y, group, img):
            self._layer = 1
            pygame.sprite.Sprite.__init__(self, group)
            
            self.image = pygame.Surface([width, height])
            img = pygame.transform.scale(img, (width, height))
            self.image.blit(img, (0, 0))
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = self.x
            self.rect.y = self.y
      def update(self):
            self.rect.x = self.x
            self.rect.y = self.y
# -------------------------------------------------------
#wall class ---------------------------------------------
class wall(pygame.sprite.Sprite):
      def __init__(self, width, height, x, y, group, img):
            self._layer = 2
            pygame.sprite.Sprite.__init__(self, group)
            
            self.image = pygame.Surface([width, height])
            img = pygame.transform.scale(img, (width, height))
            self.image.blit(img, (0, 0))
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = self.x
            self.rect.y = self.y
      def update(self):
            self.rect.x = self.x
            self.rect.y = self.y
#-------------------------------------------------------
def show_text():
      Green=(0,255,0)
      font = pygame.font.Font('freesansbold.ttf', 10)
      text_obj=font.render("This is Text",True,Green)
      screen.blit(text_obj, (0, 0)) 
# Flooring Logic
flooring = pygame.sprite.LayeredUpdates()
x = wood(50, 50, 100, 100, flooring, floor)
while run:
      screen.fill((0, 0, 0))
      fps = clock.tick(60)
      for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                  if event.type == pygame.QUIT:
                        run = False
      main_map(main_map)
      flooring.draw(screen)
      flooring.update()
      show_text(f'fps:{fps}', stats.red, 0, 0)

      pygame.display.update()
# -------------------------------------------------------
