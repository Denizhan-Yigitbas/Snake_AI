import pygame
import random

"""
Class to create a Food at a random coordinate
"""

class Food(pygame.sprite.Sprite):
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
        
        # set the position of the Food
        # TODO: change values in randint to use the input width and height
        randX = random.randint(10,49) * 10
        randY = random.randint(21,60) * 10
        self.rect.x = randX
        self.rect.y = randY
    
