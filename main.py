import pygame
from pygame.locals import *
from Classes.Snake import *
from Classes.Food import *
import random

# Global Color Variables
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0,255, 255)

allMoves = ['right', 'left', 'up', 'down']

keys = {275: 'right', 274: 'down', 276: 'left', 273: 'up'}

# Set the speed of the Snake --> lower = faster
timeDelaySpeed = 0


populationSize = 2

population = []


    
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 600, 700
        
        # create the boarder
        self.boarder = self.generateBoard()
        
        # Initial Snake array with 3 Snake Blocks starting at (50, 50) and going left
        # self.snake = [Snake(WHITE, 10, 10, 200, 260), Snake(WHITE, 10, 10, 190, 260), Snake(WHITE, 10, 10, 180, 260), Snake(WHITE, 10, 10, 170, 260), Snake(WHITE, 10, 10, 160, 260), Snake(WHITE, 10, 10, 150, 260), Snake(WHITE, 10, 10, 140, 260), Snake(WHITE, 10, 10, 130, 260)]
        self.snake = [Snake(WHITE, 10, 10, 150, 260), Snake(WHITE, 10, 10, 140, 260), Snake(WHITE, 10, 10, 130, 260)]
    
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(BLACK)
        self._running = True
        
        self.i = 0
        
        self.child = []
        
        self.population = {}
        
        self.fitness = 0
        
        self.stepsWithNoChange = 0
        
        # Create Score Board
        self.score = 0
        self.displayScore(self.score, 45)
        
        # Generate Generation Count
        self.generationCount = 0
        
        # Create Initial Food
        self.initFood = Food(RED, 10, 10)
        self._display_surf.blit(self.initFood.image, self.initFood.rect)
        
        # display the initial Snake array
        for i in range(len(self.snake)):
            self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
        
        # display the board
        for i in range(len(self.boarder)):
            self._display_surf.blit(self.boarder[i].image, self.boarder[i].rect)
            
        pygame.display.update()


    """
    Helper Method that will run the events that are clicked on by the user
    """
    def on_event(self):
        # print(self.openDirections())
        # Checks if Snake crashes with itself - LOSE
        for i in range(1, len(self.snake)):
            if pygame.sprite.collide_rect(self.snake[0], self.snake[i]):
                self.spaceToRestartText(20)
                self.gameRestart()
                break
    
        # Check if Snake hits the boarder - LOSE
        for i in range(len(self.boarder)):
            if pygame.sprite.collide_rect(self.snake[0], self.boarder[i]):
                self.spaceToRestartText(20)
                self.gameRestart()
            
        # Checks if Snake eats Food 
        if pygame.sprite.collide_rect(self.snake[0], self.initFood):
            self.eatFood()
            
        # set the direction based of key that is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.move == 'right':
                        self.move = 'right'
                    elif self.move == '':
                        self.move = ''
                    else:
                        self.move = 'left'
                        
                if event.key == pygame.K_RIGHT:
                    if self.move == 'left':
                        self.move == 'left'
                    else:
                        self.move = 'right'
            
                if event.key == pygame.K_UP:
                    if self.move == 'down':
                        self.move == 'down'
                    else:
                        self.move = 'up'
                        
                if event.key == pygame.K_DOWN:
                    if self.move == 'up':
                        self.move == 'up'
                    else:
                        self.move = 'down'
         
        # if stored current direction is right           
        if self.move == 'right':
            # Reset the Board
            self.boardReset()

            # Store the current head of the snake
            snakeHead = self.snake[0]
            
            # remove the last block of the snake
            self.snake.pop()
            
            # create a new head for the snake that is shifted toward the right
            newHead = snakeHead.moveRight()
            
            # add the newly created head to the front of the list - make head
            self.snake.insert(0, newHead)

            # displays moved snake
            for i in range(len(self.snake)):
                self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
            pygame.display.update()
            
            pygame.time.delay(timeDelaySpeed)

        # if stored current direction is left
        if self.move == 'left':
            # Reset the Board
            self.boardReset()
    
            # Store the current head of the snake
            snakeHead = self.snake[0]
    
            # remove the last block of the snake
            self.snake.pop()
    
            # create a new head for the snake that is shifted toward the right
            newHead = snakeHead.moveLeft()
    
            # add the newly created head to the front of the list - make head
            self.snake.insert(0, newHead)
    
            # displays moved snake
            for i in range(len(self.snake)):
                self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
            pygame.display.update()
    
            pygame.time.delay(timeDelaySpeed)

        # if stored current direction is up
        if self.move == 'up':
            # Reset the Board
            self.boardReset()
    
            # Store the current head of the snake
            snakeHead = self.snake[0]
    
            # remove the last block of the snake
            self.snake.pop()
    
            # create a new head for the snake that is shifted toward the right
            newHead = snakeHead.moveUp()
    
            # add the newly created head to the front of the list - make head
            self.snake.insert(0, newHead)
    
            # displays moved snake
            for i in range(len(self.snake)):
                self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
            pygame.display.update()

            pygame.time.delay(timeDelaySpeed)
                
        # if stored current direction is down
        if self.move == 'down':
            # Reset the Board
            self.boardReset()

            # Store the current head of the snake
            snakeHead = self.snake[0]

            # remove the last block of the snake
            self.snake.pop()

            # create a new head for the snake that is shifted toward the right
            newHead = snakeHead.moveDown()

            # add the newly created head to the front of the list - make head
            self.snake.insert(0, newHead)

            # displays moved snake
            for i in range(len(self.snake)):
                self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
            pygame.display.update()

            pygame.time.delay(timeDelaySpeed)

        
    """
    Helper method that displays the current score on the screen.
    """
    def displayScore(self, score, size):
        font = pygame.font.SysFont("Comic Sans MS", size)
        ScoreBoard = font.render("SCORE: {}".format(score), False, (WHITE))
        self._display_surf.blit(ScoreBoard, [90, 100])
        pygame.display.update()
        
        
    def displayGeneration(self, genCount, size):
        font = pygame.font.SysFont("Comic Sans MS", size)
        ScoreBoard = font.render("GENERATION: {}".format(genCount), False, (WHITE))
        self._display_surf.blit(ScoreBoard, [275, 100])
        pygame.display.update()
        
        
    def displayPopNumber(self):
        pass
        
        
    """
    Helper method that will reset the screen:
    
    Make screen Black
    Add the current Food block
    Add the current Score
    """
    def boardReset(self):
        # Erases the current screen
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(BLACK)
    
        # Create Score Board
        self.displayScore(self.score, 45)
        
        # Display generation Number
        self.displayGeneration(self.generationCount, 45)
    
        # Add Food
        self._display_surf.blit(self.initFood.image, self.initFood.rect)
        
        # Add Boarder
        for i in range(len(self.boarder)):
            self._display_surf.blit(self.boarder[i].image, self.boarder[i].rect)
    
    
    """
    Eating food helper method
    """
    def eatFood(self):
        # Create a new Food at random location and display it
        self.initFood = Food(RED, 10, 10)
        self._display_surf.blit(self.initFood.image, self.initFood.rect)
    
        # Create Score Board
        self.score += 1
        self.displayScore(self.score, 45)
        
        # Display generation number
        self.displayGeneration(self.generationCount, 45)
    
        
        lastSnakeBlock = self.snake[-1]
        secondToLastBlock = self.snake[-2]
    
        # if the last two blocks are on the same horizontal line and the last block is to the left of the
        # second to last block, add a block to the left side of the last block
        if lastSnakeBlock.rect.y == secondToLastBlock.rect.y and lastSnakeBlock.rect.x < secondToLastBlock.rect.x:
            newX = lastSnakeBlock.rect.x - 10
            newSnakeBlock = Snake(lastSnakeBlock.color, lastSnakeBlock.width, lastSnakeBlock.height, newX,
                                  lastSnakeBlock.rect.y)
            self.snake.append(newSnakeBlock)
    
        # if the last two blocks are on the same horizontal line and the last block is to the right of the
        # second to last block, add a block to the right side of the last block
        if lastSnakeBlock.rect.y == secondToLastBlock.rect.y and lastSnakeBlock.rect.x > secondToLastBlock.rect.x:
            newX = lastSnakeBlock.rect.x + 10
            newSnakeBlock = Snake(lastSnakeBlock.color, lastSnakeBlock.width, lastSnakeBlock.height, newX,
                                  lastSnakeBlock.rect.y)
            self.snake.append(newSnakeBlock)
    
        # if the last two blocks are on the same vertical line and the last block is above the
        # second to last block, add a block above the last block
        if lastSnakeBlock.rect.x == secondToLastBlock.rect.x and lastSnakeBlock.rect.y < secondToLastBlock.rect.y:
            newY = lastSnakeBlock.rect.y - 10
            newSnakeBlock = Snake(lastSnakeBlock.color, lastSnakeBlock.width, lastSnakeBlock.height,
                                  lastSnakeBlock.rect.x, newY)
            self.snake.append(newSnakeBlock)
    
        # if the last two blocks are on the same vertical line and the last block is below the
        # second to last block, add a block below the last block
        if lastSnakeBlock.rect.x == secondToLastBlock.rect.x and lastSnakeBlock.rect.y > secondToLastBlock.rect.y:
            newY = lastSnakeBlock.rect.y + 10
            newSnakeBlock = Snake(lastSnakeBlock.color, lastSnakeBlock.width, lastSnakeBlock.height,
                                  lastSnakeBlock.rect.x, newY)
            self.snake.append(newSnakeBlock)
    
        for i in range(len(self.snake)):
            self._display_surf.blit(self.snake[i].image, self.snake[i].rect)


    """
    Takes the player back to initial start state
    """
    def gameRestart(self):
        # Erase the Board
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(BLACK)
        self._running = True
        
        self.i = 0
        
        self.child = []
        self.stepsWithNoChange = 0

        self.fitness = 0
        
        # Recreate the Snake
        self.snake = [Snake(WHITE, 10, 10, 150, 260), Snake(WHITE, 10, 10, 140, 260), Snake(WHITE, 10, 10, 130, 260)]
    
        # Create Score Board
        self.score = 0
        self.displayScore(self.score, 45)
        
        # Display generation number
        self.displayGeneration(self.generationCount, 45)
    
        # Create Initial Food
        self.initFood = Food(RED, 10, 10)
        self._display_surf.blit(self.initFood.image, self.initFood.rect)
    
        # set current move to nothing
        self.move = ''
    
        # draw in the boarder
        for i in range(len(self.boarder)):
            self._display_surf.blit(self.boarder[i].image, self.boarder[i].rect)
    
        # display the initial Snake array
        for i in range(len(self.snake)):
            self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
        pygame.display.update()


    """
    Creates a List of Blocks that outline the Boarder of the snake game
    """
    def generateBoard(self):
        boardCorners = []
        boardTop = []
        boardSide1 = []
        boardSide2 = []
        boardBottom = []
    
        # Makes (0,0) of board = (100, 210)
        # top left corner
        boardCorners.append(Snake(CYAN, 10, 10, 90, 200))
    
        # top right corner
        boardCorners.append(Snake(CYAN, 10, 10, 500, 200))
    
        # bottom left corner
        boardCorners.append(Snake(CYAN, 10, 10, 90, 610))
    
        # bottom right corner
        boardCorners.append(Snake(CYAN, 10, 10, 500, 610))
    
        # top and bottom sides
        topCoord = 100
        for i in range(40):
            boardTop.append(Snake(CYAN, 10, 10, topCoord, 200))
            boardBottom.append(Snake(CYAN, 10, 10, topCoord, 610))
            topCoord += 10
    
        # sides of board
        sideCoord = 210
        for i in range(40):
            boardSide1.append(Snake(CYAN, 10, 10, 90, sideCoord))
            boardSide2.append(Snake(CYAN, 10, 10, 500, sideCoord))
            sideCoord += 10
    
        # combine all parts
        allBoarder = boardCorners + boardTop + boardSide1 + boardSide2 + boardBottom
    
        # return list of blocks
        return allBoarder


    """
    Allows player to restart a game by pressing space bar - displays losing screen
    """
    def spaceToRestartText(self, size):
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(BLACK)
        self.youLoseText(50)
        self.yourScoreText(25)
        font = pygame.font.SysFont("Comic Sans MS", size)
        text_surface = font.render("Press space bar to play again", True, WHITE)
        text_rect = text_surface.get_rect(center=(self.weight / 2, self.height / 2))
        self._display_surf.blit(text_surface, text_rect)
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        done = True


    """
    Helper function that prints 'YOU LOSE!'
    """
    def youLoseText(self, size):
        font = pygame.font.SysFont("Comic Sans MS", size)
        text_surface = font.render("YOU LOSE!", True, WHITE)
        # Shift height up so no collision with space bar text
        text_rect = text_surface.get_rect(center=(self.weight / 2, (self.height / 2) - 75))
        self._display_surf.blit(text_surface, text_rect)
        pygame.display.flip()
    
    
    """
    Helper function that prints your score at loss
    """
    def yourScoreText(self, size):
        font = pygame.font.SysFont("Comic Sans MS", size)
        text_surface = font.render("Your Score was: " + str(self.score), True, WHITE)
        # Shift height up so no collision with space bar text
        text_rect = text_surface.get_rect(center=(self.weight / 2, (self.height / 2) - 35))
        self._display_surf.blit(text_surface, text_rect)
        pygame.display.flip()


    def openDirections(self):
        
        foodCoord = (self.initFood.rect.x, self.initFood.rect.y)
        
        openDirections = []
        
        if self.move == '':
            openDirections = ['right', 'up', 'down']

            checkRight = self.snake[0].moveRight()
            checkUp = self.snake[0].moveUp()
            checkDown = self.snake[0].moveDown()

            checkRightCoord = (checkRight.rect.x, checkRight.rect.y)
            checkUpCoord = (checkUp.rect.x, checkUp.rect.y)
            checkDownCoord = (checkDown.rect.x, checkDown.rect.y)

            if checkRightCoord == foodCoord:
                openDirections = ['right']
                return openDirections
            elif checkUpCoord == foodCoord:
                openDirections = ['up']
                return openDirections
            elif checkDownCoord == foodCoord:
                openDirections = ['down']
                return openDirections
            
        if self.move == 'left':
            openDirections = ['left', 'up', 'down']
            checkLeft = self.snake[0].moveLeft()
            checkUp = self.snake[0].moveUp()
            checkDown = self.snake[0].moveDown()
            
            checkLeftCoord = (checkLeft.rect.x, checkLeft.rect.y)
            checkUpCoord = (checkUp.rect.x, checkUp.rect.y)
            checkDownCoord = (checkDown.rect.x, checkDown.rect.y)
            
            if checkLeftCoord == foodCoord:
                openDirections = ['left']
                return openDirections
            elif checkUpCoord == foodCoord:
                openDirections = ['up']
                return openDirections
            elif checkDownCoord == foodCoord:
                openDirections = ['down']
                return openDirections
                
            for i in range(len(self.boarder)):
                if pygame.sprite.collide_rect(checkLeft, self.boarder[i]):
                    index = openDirections.index("left")
                    openDirections.pop(index)
                if pygame.sprite.collide_rect(checkUp, self.boarder[i]):
                    index = openDirections.index("up")
                    openDirections.pop(index)
                if pygame.sprite.collide_rect(checkDown, self.boarder[i]):
                    index = openDirections.index("down")
                    openDirections.pop(index)
        
            for i in range(1, len(self.snake)):
                if pygame.sprite.collide_rect(checkLeft, self.snake[i]):
                    index = openDirections.index("left")
                    openDirections.pop(index)
                if pygame.sprite.collide_rect(checkUp, self.snake[i]):
                    index = openDirections.index("up")
                    openDirections.pop(index)
                if pygame.sprite.collide_rect(checkDown, self.snake[i]):
                    index = openDirections.index("down")
                    openDirections.pop(index)
    
        if self.move == 'right':
            openDirections = ['right', 'up', 'down']
            checkRight = self.snake[0].moveRight()
            checkUp = self.snake[0].moveUp()
            checkDown = self.snake[0].moveDown()

            checkRightCoord = (checkRight.rect.x, checkRight.rect.y)
            checkUpCoord = (checkUp.rect.x, checkUp.rect.y)
            checkDownCoord = (checkDown.rect.x, checkDown.rect.y)

            if checkRightCoord == foodCoord:
                openDirections = ['right']
                return openDirections
            elif checkUpCoord == foodCoord:
                openDirections = ['up']
                return openDirections
            elif checkDownCoord == foodCoord:
                openDirections = ['down']
                return openDirections
            
            for i in range(len(self.boarder)):
                if pygame.sprite.collide_rect(checkRight, self.boarder[i]):
                    index = openDirections.index('right')
                    openDirections.pop(index)
                if pygame.sprite.collide_rect(checkUp, self.boarder[i]):
                    index = openDirections.index('up')
                    openDirections.pop(index)
                if pygame.sprite.collide_rect(checkDown, self.boarder[i]):
                    index = openDirections.index('down')
                    openDirections.pop(index)
        
            for i in range(1, len(self.snake)):
                if pygame.sprite.collide_rect(checkRight, self.snake[i]):
                    index = openDirections.index("right")
                    openDirections.pop(index)
                if pygame.sprite.collide_rect(checkUp, self.snake[i]):
                    index = openDirections.index("up")
                    openDirections.pop(index)
                if pygame.sprite.collide_rect(checkDown, self.snake[i]):
                    index = openDirections.index("down")
                    openDirections.pop(index)
    
        if self.move == 'up':
            openDirections = ['up', 'left', 'right']
            checkUp = self.snake[0].moveUp()
            checkLeft = self.snake[0].moveLeft()
            checkRight = self.snake[0].moveRight()

            checkUpCoord = (checkUp.rect.x, checkUp.rect.y)
            checkLeftCoord = (checkLeft.rect.x, checkLeft.rect.y)
            checkRightCoord = (checkRight.rect.x, checkRight.rect.y)
            
            if checkUpCoord == foodCoord:
                openDirections = ['up']
                return openDirections
            elif checkLeftCoord == foodCoord:
                openDirections = ['left']
                return openDirections
            elif checkRightCoord == foodCoord:
                openDirections = ['right']
                return openDirections
                
                
            for i in range(len(self.boarder)):
                if pygame.sprite.collide_rect(checkUp, self.boarder[i]):
                    index = openDirections.index("up")
                    openDirections.pop(index)
                if pygame.sprite.collide_rect(checkLeft, self.boarder[i]):
                    index = openDirections.index("left")
                    openDirections.pop(index)
                if pygame.sprite.collide_rect(checkRight, self.boarder[i]):
                    index = openDirections.index("right")
                    openDirections.pop(index)
        
            for i in range(1, len(self.snake)):
                if pygame.sprite.collide_rect(checkUp, self.snake[i]):
                    index = openDirections.index("up")
                    openDirections.pop(index)
                if pygame.sprite.collide_rect(checkLeft, self.snake[i]):
                    index = openDirections.index("left")
                    openDirections.pop(index)
                if pygame.sprite.collide_rect(checkRight, self.snake[i]):
                    index = openDirections.index("right")
                    openDirections.pop(index)
    
        if self.move == 'down':
            openDirections = ['down', 'left', 'right']
            checkDown = self.snake[0].moveDown()
            checkLeft = self.snake[0].moveLeft()
            checkRight = self.snake[0].moveRight()

            checkDownCoord = (checkDown.rect.x, checkDown.rect.y)
            checkLeftCoord = (checkLeft.rect.x, checkLeft.rect.y)
            checkRightCoord = (checkRight.rect.x, checkRight.rect.y)

            if checkDownCoord == foodCoord:
                openDirections = ['down']
                return openDirections
            elif checkLeftCoord == foodCoord:
                openDirections = ['left']
                return openDirections
            elif checkRightCoord == foodCoord:
                openDirections = ['right']
                return openDirections
                
            for i in range(len(self.boarder)):
                if pygame.sprite.collide_rect(checkDown, self.boarder[i]):
                    index = openDirections.index("down")
                    openDirections.pop(index)
                if pygame.sprite.collide_rect(checkLeft, self.boarder[i]):
                    index = openDirections.index("left")
                    openDirections.pop(index)
                if pygame.sprite.collide_rect(checkRight, self.boarder[i]):
                    index = openDirections.index("right")
                    openDirections.pop(index)
        
            for i in range(1, len(self.snake)):
                if pygame.sprite.collide_rect(checkDown, self.snake[i]):
                    index = openDirections.index("down")
                    openDirections.pop(index)
                if pygame.sprite.collide_rect(checkLeft, self.snake[i]):
                    index = openDirections.index("left")
                    openDirections.pop(index)
                if pygame.sprite.collide_rect(checkRight, self.snake[i]):
                    index = openDirections.index("right")
                    openDirections.pop(index)
    
        return openDirections
    
    
    def locationOfFoodToHead(self):
        foodCoordx = self.initFood.rect.x
        foodCoordy = self.initFood.rect.y
        headCoordx = self.snake[0].rect.x
        headCoordy = self.snake[0].rect.y

        if not pygame.sprite.collide_rect(self.snake[0], self.initFood):
            if headCoordx == foodCoordx and headCoordy < foodCoordy:
                goodDirection = ['down']
            if headCoordx == foodCoordx and headCoordy > foodCoordy:
                goodDirection = ['up']
            if headCoordy == foodCoordy and headCoordx < foodCoordx:
                goodDirection = ['right']
            if headCoordy == foodCoordy and headCoordx > foodCoordx:
                goodDirection = ['left']
                
            if headCoordx < foodCoordx and headCoordy > foodCoordy:
                goodDirection = ['up', 'right']
            if headCoordx > foodCoordx and headCoordy > foodCoordy:
                goodDirection = ['up', 'left']
            if headCoordx < foodCoordx and headCoordy < foodCoordy:
                goodDirection = ['down', 'right']
            if headCoordx > foodCoordx and headCoordy < foodCoordy:
                goodDirection = ['down', 'left']
        else:
            goodDirection = []
            
        return goodDirection
    
    
    def topNchildren(self, dic, n):
        keys = list(dic)
        keys.sort(reverse = True)
        top = []
        for i in range(n):
            nth = keys[i]
            val = dic.get(nth)
            top.append(val)
        return top


    def breed(self, child1, child2):
        len1 = len(child1)
        len2 = len(child2)
        if len1 < len2:
            randIdx = random.randint(0, len1-1)
        else:
            randIdx = random.randint(0, len2-1)
        
        for i in range(randIdx):
            temp = child1[i]
            child1[i] = child2[i]
            child2[i] = temp
        return child1, child2
    
    
    """
    Given a list of move lists, this function will create a dictionary mapping each list
    to a fitness score.
    """
    def createFitnessDictionary(self, lstOfMoveLsts):
        pass

        
    def on_event_AI(self):
        if len(self.population) > populationSize - 1:
            population.append(self.population)
            fittest, secFittest = self.topNchildren(self.population, 2)[0], self.topNchildren(self.population, 2)[1]
            breeded = self.breed(fittest, secFittest)
            self.population = {}
            self.generationCount += 1

        self.stepsWithNoChange += 1
    
        if self.move in self.locationOfFoodToHead():
            self.fitness += 1
        else:
            self.fitness -= 1.5
        
        #self.fitness = self.fitness()
    
        # Checks if Snake eats Food
        if pygame.sprite.collide_rect(self.snake[0], self.initFood):
            self.eatFood()
            self.stepsWithNoChange = 0
            self.fitness += 10
            
        possibleDirections = self.openDirections()
        
        if self.stepsWithNoChange > 300:
            possibleDirections = []
        
        if possibleDirections == []:
            print()
            print('lost')
            print('final score: ', self.score)
            self.population[self.fitness] = self.child
            print('pop: ', self.population)
            print('pop len: ', len(self.population))
            print('fit', self.population.keys())
            self.gameRestart()
        elif self.generationCount == 0:
            randomMoveIndex = random.randint(0, len(possibleDirections) - 1)
            self.move = possibleDirections[randomMoveIndex]
        else:
            movesList = ['', 'up', 'left', 'down', 'left', 'left', 'up', 'left', 'down', 'right', 'right', 'down', 'left', 'up', 'left', 'down', 'down', 'right', 'down', 'down', 'right', 'down', 'right', 'right', 'right', 'right', 'down', 'right', 'up', 'left', 'down', 'right', 'down', 'down', 'down', 'right', 'down', 'right', 'right', 'up', 'right']
            self.move = movesList[self.i]
            self.i += 1
            
        self.child.append(self.move)
        
        # if stored current direction is right
        if self.move == 'right':
            # Reset the Board
            self.boardReset()
            
            # Store the current head of the snake
            snakeHead = self.snake[0]

            # remove the last block of the snake
            self.snake.pop()

            # create a new head for the snake that is shifted toward the right
            newHead = snakeHead.moveRight()

            # add the newly created head to the front of the list - make head
            self.snake.insert(0, newHead)

            # displays moved snake
            for i in range(len(self.snake)):
                self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
            pygame.display.update()

            pygame.time.delay(timeDelaySpeed)

        # if stored current direction is left
        if self.move == 'left':
            # Reset the Board
            self.boardReset()

            # Store the current head of the snake
            snakeHead = self.snake[0]

            # remove the last block of the snake
            self.snake.pop()

            # create a new head for the snake that is shifted toward the right
            newHead = snakeHead.moveLeft()

            # add the newly created head to the front of the list - make head
            self.snake.insert(0, newHead)

            # displays moved snake
            for i in range(len(self.snake)):
                self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
            pygame.display.update()

            pygame.time.delay(timeDelaySpeed)

        # if stored current direction is up
        if self.move == 'up':
            # Reset the Board
            self.boardReset()

            # Store the current head of the snake
            snakeHead = self.snake[0]

            # remove the last block of the snake
            self.snake.pop()

            # create a new head for the snake that is shifted toward the right
            newHead = snakeHead.moveUp()

            # add the newly created head to the front of the list - make head
            self.snake.insert(0, newHead)

            # displays moved snake
            for i in range(len(self.snake)):
                self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
            pygame.display.update()

            pygame.time.delay(timeDelaySpeed)

        # if stored current direction is down
        if self.move == 'down':
                # Reset the Board
                self.boardReset()
    
                # Store the current head of the snake
                snakeHead = self.snake[0]
    
                # remove the last block of the snake
                self.snake.pop()
    
                # create a new head for the snake that is shifted toward the right
                newHead = snakeHead.moveDown()
    
                # add the newly created head to the front of the list - make head
                self.snake.insert(0, newHead)
    
                # displays moved snake
                for i in range(len(self.snake)):
                    self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
                pygame.display.update()
    
                pygame.time.delay(timeDelaySpeed)
            


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
    
        self.move = ''
        while (self._running):
            self.on_event_AI()
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
    


""""

Every time snake eats food, create a new graph where the snake could go.
No edge between nodes from empty block to snake block. No edge between nodes from empty block to border.
All edges must be between empty blocks.
Get Node of Food.
Get Node of Snake Head
Find the shortest distance between Food and Snake Head.
Take that route
Eat Food and Repeat.


"""
