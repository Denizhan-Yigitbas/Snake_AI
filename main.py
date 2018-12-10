import pygame
from pygame.locals import *
import random

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


all_sprite_list = pygame.sprite.Group()

class Block(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       
       
class Snake(pygame.sprite.Sprite):
    # TODO: Make Snake a chain of Blocks
    def __init__(self, color, width, height, x, y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        # self.rect = self.image.get_rect()
        self.rect = pygame.draw.rect(self.image, color, (x, y, width, height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def setX(self, x):
        self.x += x
        return self
        
    
    
    """
    Method the will change the direction of the Snake towards the left
    """
    def moveLeft(self):
        self.x -= self.width
        all_sprite_list.add(Snake(WHITE, self.width, self.height, self.x, self.y;))
        return Snake(WHITE, self.width, self.height, self.x, self.y)
    
    """
    Method that will change the direction of the Snake toward the right
    """
    def moveRight(self):
        self.x += self.width
        all_sprite_list.add(Snake(WHITE, self.width, self.height, self.x, self.y))
        return Snake(WHITE, self.width, self.height, self.x, self.y)

    
    """
    Method that will change the direction of the Snake to go upward
    """
    def moveUp(self):
        self.y -= self.width
        all_sprite_list.add(Snake(WHITE, self.width, self.height, self.x, self.y))
        return Snake(WHITE, self.width, self.height, self.x, self.y)
    
    
    """
    Method that will change the direction of the Snake to go downward
    """
    def moveDown(self):
        self.y += self.width
        all_sprite_list.add(Snake(WHITE, self.width, self.height, self.x, self.y))
        return Snake(WHITE, self.width, self.height, self.x, self.y)
    
    
class Food(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = pygame.draw.rect(self.image, color, (random.randint(0,399), random.randint(0,399), width, height))
        
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        #self.rect = self.image.get_rect()

    
    """
    UNNEEDED - ??
    returns a random coordinate in tuple form within a given width and height
    """
    def getNewLocation(self, width, height):
        return pygame.draw.rect(self.image,color, (random.randint(0,399), random.randint(0,399), width, height))
        
        

class App:
    
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 400, 400
        self.snake = Snake(WHITE, 10, 10, 100, 100)
        all_sprite_list.add(self.snake)
        
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(BLACK)
        self.initFood = Food(RED, 10, 10)
        all_sprite_list.add(self.initFood)
        self._running = True

    """
    Helper Method that will run the events that are clicked on by the user
    """
    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # TODO: move Snake move to the left
                    self.snake.moveLeft()
                    print("LEFT")
                if event.key == pygame.K_RIGHT:
                    # TODO: make Snake move to the right
                    self.snake.moveRight()
                    print("RIGHT")
                if event.key == pygame.K_UP:
                    # TODO: make Snake move up
                    self.snake.moveUp()
                    print("UP")
                if event.key == pygame.K_DOWN:
                    # TODO: make Snake move down
                    self.snake.moveDown()
                    print("DOWN")
                    
    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    """
    Game Loop
    """
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
    
        while (self._running):
            self.on_event()
            self.on_loop()
            self.on_render()
            all_sprite_list.draw(self._display_surf)
            pygame.display.update()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()