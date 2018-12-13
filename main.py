import pygame
from pygame.locals import *
from Classes.Snake import *
from Classes.Food import *
from Classes.Block import *



RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


#all_sprite_list = pygame.sprite.Group()


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
        
        # Create Initial Food
        self.initFood = Food(RED, 10, 10)
        self._display_surf.blit(self.initFood.image, self.initFood.rect)
        
        # display the initial Snake array
        for i in range(len(self.snake)):
            self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
        pygame.display.update()
        


    """
    Helper Method that will run the events that are clicked on by the user
    """
    def on_event(self):
        if pygame.sprite.collide_rect(self.snake[0], self.initFood):
            # Erases the current screen
            self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
            self._display_surf.fill(BLACK)
            
            # Create a new Food at random location and display it
            self.initFood = Food(RED, 10, 10)
            

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
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == pygame.KEYDOWN:
                
                # Adds a block to the end of the snake. This will replace when snake eats a Food
                # HAS BEEN IMPLEMENTED - FOLLOWING CAN BE REMOVED
                if event.key == pygame.K_SPACE:
                    print("SPACE")
                    
                    # Erases the current screen
                    self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
                    self._display_surf.fill(BLACK)
                    
                    # add Food
                    self._display_surf.blit(self.initFood.image, self.initFood.rect)
                    
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
                        

                    # displays all snake Blocks
                    for i in range(len(self.snake)):
                        self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
                    
                if event.key == pygame.K_LEFT:
                    print("LEFT")

                    # Erases the current screen
                    self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
                    self._display_surf.fill(BLACK)
                    
                    # Add Food
                    self._display_surf.blit(self.initFood.image, self.initFood.rect)

                    # Store the length of the snake
                    currentLength = len(self.snake)

                    # Loop that adds the shifted Snake blocks to self.snake array
                    for i in range(len(self.snake)):
                        player = self.snake[i].image
    
                        # Shift the current snake right 10 units
                        newSnake = self.snake[i].moveLeft()
    
                        # append new Snake into list instead of old
                        self.snake.append(newSnake)

                    # removes old snake blocks
                    for i in range(currentLength):
                        self.snake.pop(0)

                    # displays the shifted snake Blocks
                    for i in range(len(self.snake)):
                        self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
                        
                if event.key == pygame.K_RIGHT:
                    print("RIGHT")
                    
                    # Erases the current screen
                    self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
                    self._display_surf.fill(BLACK)
                    
                    # Add Food
                    self._display_surf.blit(self.initFood.image, self.initFood.rect)
                    
                    # Store the length of the snake
                    currentLength = len(self.snake)
                    
                    # Loop that adds the shifted Snake blocks to self.snake array
                    for i in range(len(self.snake)):
                        player = self.snake[i].image

                        # Shift the current snake right 10 units
                        newSnake = self.snake[i].moveRight()
                        
                        # append new Snake into list instead of old
                        self.snake.append(newSnake)
                    
                    # removes old snake blocks
                    for i in range(currentLength):
                        self.snake.pop(0)
                    
                    # displays the shifted snake Blocks
                    for i in range(len(self.snake)):
                        self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
            
            
                if event.key == pygame.K_UP:
                    
                    # Erases the current screen
                    self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
                    self._display_surf.fill(BLACK)
                    
                    # Add Food
                    self._display_surf.blit(self.initFood.image, self.initFood.rect)

                    # Store the length of the snake
                    currentLength = len(self.snake)

                    # Loop that adds the shifted Snake blocks to self.snake array
                    for i in range(len(self.snake)):
                        player = self.snake[i].image
    
                        # Shift the current snake right 10 units
                        newSnake = self.snake[i].moveUp()
    
                        # append new Snake into list instead of old
                        self.snake.append(newSnake)

                    # removes old snake blocks
                    for i in range(currentLength):
                        self.snake.pop(0)

                    # displays the shifted snake Blocks
                    for i in range(len(self.snake)):
                        self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
                        
                if event.key == pygame.K_DOWN:
                    
                    # Erases the current screen
                    self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
                    self._display_surf.fill(BLACK)
                    
                    # Add Food
                    self._display_surf.blit(self.initFood.image, self.initFood.rect)

                    # Store the length of the snake
                    currentLength = len(self.snake)

                    # Loop that adds the shifted Snake blocks to self.snake array
                    for i in range(currentLength):
                        player = self.snake[i].image
    
                        # Shift the current snake right 10 units
                        newSnake = self.snake[i].moveDown()
    
                        # append new Snake into list instead of old
                        self.snake.append(newSnake)

                    # removes old snake blocks
                    for i in range(currentLength):
                        self.snake.pop(0)

                    # displays the shifted snake Blocks
                    for i in range(len(self.snake)):
                        self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
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
    
        while (self._running):
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()
        
    


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()