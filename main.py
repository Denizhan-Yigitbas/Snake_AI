import pygame
from pygame.locals import *
from Classes.Snake import *
from Classes.Food import *
from Classes.Block import *


# Global Color Variables
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0,255, 255)

# Set the speed of the Snake --> lower = faster
timeDelaySpeed = 1
    
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 600, 700
        
        # create the boarder
        self.boarder = self.generateBoard()
        
        # Initial Snake array with 3 Snake Blocks starting at (50, 50) and going left
        self.snake = [Snake(WHITE, 10, 10, 150, 260), Snake(WHITE, 10, 10, 140, 260), Snake(WHITE, 10, 10, 130, 260)]
    
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(BLACK)
        self._running = True
        
        # Create Score Board
        self.score = 0
        self.displayScore(self.score, 45)
        
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
        # Checks if Snake crashes with itself - LOSE
        for i in range(1, len(self.snake)-1):
            if pygame.sprite.collide_rect(self.snake[0], self.snake[1]):
                self.spaceToRestartText(20)
                self.gameRestart()
            if pygame.sprite.collide_rect(self.snake[0], self.snake[i]):
                self.spaceToRestartText(20)
                self.gameRestart()
    
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
                    self.move = 'left'
                        
                if event.key == pygame.K_RIGHT:
                    self.move = 'right'
            
                if event.key == pygame.K_UP:
                    self.move = 'up'
                        
                if event.key == pygame.K_DOWN:
                    self.move = 'down'
         
        # if stored current direction is right           
        if self.move == 'right':
            print("RIGHT")
            
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
            print("LEFT")
    
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
            print("UP")
    
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
            print("DOWN")

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
    
        # for i in range(len(self.snake)):
        #     self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
        #
        # Store the last and second to last blocks of the snake
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
        
        # Recreate the Snake
        self.snake = [Snake(WHITE, 10, 10, 150, 260), Snake(WHITE, 10, 10, 140, 260), Snake(WHITE, 10, 10, 130, 260)]
    
        # Create Score Board
        self.score = 0
        self.displayScore(self.score, 45)
    
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
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()