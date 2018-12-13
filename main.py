import pygame
from pygame.locals import *
from Classes.Snake import *
from Classes.Food import *
from Classes.Block import *



RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



    
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 400, 400
        
        # Initial Snake array with 3 Snake Blocks starting at (50, 50) and going left
        self.snake = [Snake(WHITE, 10, 10, 50, 50), Snake(WHITE, 10, 10, 40, 50), Snake(WHITE, 10, 10, 30, 50)]
        
        
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(BLACK)
        self._running = True
        
        # Create Score Board
        self.score = 0
        self.displayScore(self.score, 30)
        
        # Create Initial Food
        self.initFood = Food(RED, 10, 10)
        self._display_surf.blit(self.initFood.image, self.initFood.rect)
        
        # display the initial Snake array
        for i in range(len(self.snake)):
            self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
        pygame.display.update()
        
        self.moves = []


    """
    Helper Method that will run the events that are clicked on by the user
    """
    def on_event(self):
        
        # Checks if Snake crashes with itself - LOSE
        for i in range(1, len(self.snake)):
            if pygame.sprite.collide_rect(self.snake[0], self.snake[i]):
                pygame.quit()
        
        # Checks if Snake goes off the board
        if self.snake[0].rect.x == -10 or self.snake[0].rect.x == 400:
            self.message_display("LOSE")
            #pygame.quit()
        if self.snake[0].rect.y == -10 or self.snake[0].rect.y == 400:
            pygame.quit()
            
        # Checks if Snake eats Food - LOSE
        if pygame.sprite.collide_rect(self.snake[0], self.initFood):
            self.eatFood()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.oldMove = self.move
                    self.move = 'left'
                        
                if event.key == pygame.K_RIGHT:
                    self.oldMove = self.move
                    self.move = 'right'
                    self.moves.append((self.snake[0].rect.x, self.snake[0].rect.y))
            
                if event.key == pygame.K_UP:
                    self.oldMove = self.move
                    self.move = 'up'
                        
                if event.key == pygame.K_DOWN:
                    self.oldMove = self.move
                    self.move = 'down'
                    self.moves.append((self.snake[0].rect.x,self.snake[0].rect.y))
                    
                    
        print(self.moves)
        if self.move == 'right':
            print("RIGHT")
    
            # get the coordinates of the head of the Snake
            xCoord = self.snake[0].rect.x
            yCoord = self.snake[0].rect.y
            
    
            # Reset the Board
            self.boardReset()
    
            # Store the length of the snake
            currentLength = len(self.snake)
    
            # Loop to make points follow the head
            for i in range(len(self.snake)):
                if self.snake[i].rect.x == xCoord and self.snake[i].rect.y == yCoord:
                    newSnake = self.snake[i].moveRight()
            
                    # append new Snake into list instead of old
                    self.snake.append(newSnake)
                else:
                    # append snake into it
                    self.snake.append(self.snake[i].moveRight())
            # removes old snake blocks
            for i in range(currentLength):
                self.snake.pop(0)
    
            # displays the shifted snake Blocks
            for i in range(len(self.snake)):
                self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
            pygame.display.update()
            
            pygame.time.delay(150)

        if self.move == 'left':
    
            print("LEFT")
    
            xCoord = self.snake[0].rect.x
            yCoord = self.snake[0].rect.y
    
            # Reset the Board
            self.boardReset()
    
            # Store the length of the snake
            currentLength = len(self.snake)
    
            # Loop to make points follow the head
            for i in range(len(self.snake)):
                if self.snake[i].rect.x == xCoord and self.snake[i].rect.y == yCoord:
                    newSnake = self.snake[i].moveLeft()
            
                    # append new Snake into list instead of old
                    self.snake.append(newSnake)
                else:
                    if self.oldMove == 'right':
                        self.snake.append(self.snake[i].moveRight())
                    if self.oldMove == 'left':
                        self.snake.append(self.snake[i].moveLeft())
                    if self.oldMove == 'up':
                        self.snake.append(self.snake[i].moveUp())
                    if self.oldMove == 'down':
                        self.snake.append(self.snake[i].moveDown())
    
            # removes old snake blocks
            for i in range(currentLength):
                self.snake.pop(0)
    
            # displays the shifted snake Blocks
            for i in range(len(self.snake)):
                self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
            pygame.display.update()
    
            pygame.time.delay(150)

        if self.move == 'up':
            print("UP")
            # get the coordinates of the head of the Snake
            xCoord = self.snake[0].rect.x
            yCoord = self.snake[0].rect.y

            # Reset the board
            self.boardReset()

            # Store the length of the snake
            currentLength = len(self.snake)

            # Loop to make points follow the head
            for i in range(len(self.snake)):
                if self.snake[i].rect.x == xCoord and self.snake[i].rect.y == yCoord:
                    newSnake = self.snake[i].moveUp()
        
                    # append new Snake into list instead of old
                    self.snake.append(newSnake)
                else:
                    if self.oldMove == 'right':
                        self.snake.append(self.snake[i].moveRight())
                    if self.oldMove == 'left':
                        self.snake.append(self.snake[i].moveLeft())
                    if self.oldMove == 'up':
                        self.snake.append(self.snake[i].moveUp())
                    if self.oldMove == 'down':
                        self.snake.append(self.snake[i].moveDown())

            # removes old snake blocks
            for i in range(currentLength):
                self.snake.pop(0)

            # displays the shifted snake Blocks
            for i in range(len(self.snake)):
                self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
                
            pygame.time.delay(150)
            pygame.display.update()
                
        if self.move == 'down':
            print("DOWN")
            # get the coordinates of the head of the Snake
            xCoord = self.snake[0].rect.x
            yCoord = self.snake[0].rect.y

            
            # Reset the Board
            self.boardReset()
    
            # Store the length of the snake
            currentLength = len(self.snake)
    
            # Loop to make points follow the head
            for i in range(len(self.snake)):
                if self.snake[i].rect.x == xCoord and self.snake[i].rect.y == yCoord:
                    newSnake = self.snake[i].moveDown()
            
                    # append new Snake into list instead of old
                    self.snake.append(newSnake)
                else:
                    if self.oldMove == 'right':
                        self.snake.append(self.snake[i].moveRight())
                    if self.oldMove == 'left':
                        self.snake.append(self.snake[i].moveLeft())
                    if self.oldMove == 'up':
                        self.snake.append(self.snake[i].moveUp())
                    if self.oldMove == 'down':
                        self.snake.append(self.snake[i].moveDown())
    
            # removes old snake blocks
            for i in range(currentLength):
                self.snake.pop(0)
    
            # displays the shifted snake Blocks
            for i in range(len(self.snake)):
                self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
            pygame.display.update()
            
            pygame.time.delay(150)
        
        
        pygame.display.update()
    
    
    """
    Helper method that displays the current score on the screen.
    """
    def displayScore(self, score, size):
        font = pygame.font.SysFont("Comic Sans MS", size)
        ScoreBoard = font.render("SCORE: {}".format(score), False, (WHITE))
        self._display_surf.blit(ScoreBoard, [0, 0])
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
        self.displayScore(self.score, 30)
    
        # Add Food
        self._display_surf.blit(self.initFood.image, self.initFood.rect)
    
    """
    Eating food helper method
    """
    def eatFood(self):
        # Erases the current screen
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(BLACK)
    
        # Create a new Food at random location and display it
        self.initFood = Food(RED, 10, 10)
    
        # Create Score Board
        self.score += 1
        self.displayScore(self.score, 30)
    
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
        

    def text_objects(self, text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()

    def message_display(self, text):
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf = largeText.render(text, True, BLACK)
        TextRect = TextSurf.get_rect()
        #TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((self.weight / 2), (self.height / 2))
        self._display_surf.blit(TextSurf, TextRect)
        pygame.display.update()
                    
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
    
        self.move = 'none'
        self.oldMove = 'none'
        while (self._running):
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()
        
    


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()