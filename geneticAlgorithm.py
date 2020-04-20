from Classes.Snake import *
from Classes.Food import *
import random

""""

- fitness function
- breeding function
- mutation function
- child maker


"""



"""
Given a snake and food, calculates a fitness function
"""
def fitness(snake, food, boarder):
    fitness = 0
    
    if pygame.sprite.collide_rect(snake[0], food):
        fitness += 5000
    for i in range(len(boarder)):
        if pygame.sprite.collide_rect(snake[0], boarder[i]):
            fitness -= 150
    for i in range(1, len(snake)):
        if pygame.sprite.collide_rect(snake[0], snake[1]):
            fitness -= 150
        if pygame.sprite.collide_rect(snake[0], snake[i]):
            fitness -= 150
    return fitness


def generateSingleChild():
    pass

def generatePopulation(populationSize):
    pass

def breed(child1, child2):
    pass
    


    
        