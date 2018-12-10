import pygame
from pygame.locals import *


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
       
       
class Snake:
    # TODO: Make Snake a chain of Blocks
    
    snake = None
    
    """
    Method the will change the direction of the Snake towards the left
    """
    def moveLeft(self):
        return 0
    
    """
    Method that will change the direction of the Snake toward the right
    """
    def moveRight(self):
        return 0
    
    """
    Method that will change the direction of the Snake to go upward
    """
    def moveUp(self):
        return 0
    
    
    """
    Method that will change the direction of the Snake to go downward
    """
    def moveDown(self):
        return 0
    
    


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 400, 400
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
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
                    print("LEFT")
                if event.key == pygame.K_RIGHT:
                    # TODO: make Snake move to the right
                    print("RIGHT")
                if event.key == pygame.K_UP:
                    # TODO: make Snake move up
                    print("UP")
                if event.key == pygame.K_DOWN:
                    # TODO: make Snake move down
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
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()