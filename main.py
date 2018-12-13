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
        self.snake = [Snake(WHITE, 10, 10, 50, 50), Snake(WHITE, 10, 10, 40, 50), Snake(WHITE, 10, 10, 30, 50)]

        
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(BLACK)
        self._running = True
        xInit = 100
        yInit = 100
        for i in range(len(self.snake)):
            self._display_surf.blit(self.snake[i].image, self.snake[i].rect)
            # player = self.snake[i].image
            # position = player.get_rect()
            # position.x = xInit
            # position.y = yInit
            # self._display_surf.blit(self.snake[i].image, position)
            # xInit -= 10
            # self.snake.append(Snake(WHITE, 10, 10, position.x, position.y))
        pygame.display.update()
        
        # for i in range(len(self.snake)):
        #     player = self.snake[i].image
        #     position = player.get_rect()
        #     for x in range(100):
        #         self._display_surf.fill(BLACK)
        #         position = position.move(10,0)
        #         self._display_surf.blit(player, position)
        #         pygame.display.update()


    """
    Helper Method that will run the events that are clicked on by the user
    """
    def on_event(self):
        # movement = {pygame.K_UP: (0, -1),
        #             pygame.K_DOWN: (0, 1),
        #             pygame.K_LEFT: (-1, 0),
        #             pygame.K_RIGHT: (1, 0)}
        move = (0,0)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # self.body.pop()
                    # self.body.append(self.snake.moveLeft())
                    print("LEFT")

                    # Erases the current screen
                    self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
                    self._display_surf.fill(BLACK)

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
                    # TODO: make Snake move to the right
                    print("RIGHT")
                    
                    # Erases the current screen
                    self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
                    self._display_surf.fill(BLACK)
                    
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
                    # TODO: make Snake move up
                    
                    # Erases the current screen
                    self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
                    self._display_surf.fill(BLACK)

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
                    # TODO: make Snake move down
                    # Erases the current screen
                    self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
                    self._display_surf.fill(BLACK)
                    
                    downwardSnake = []

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
        # self.snake.rect.move_ip(move)
        # self._display_surf.fill(pygame.color.Color('Black'))
        # pygame.draw.rect(self._display_surf, pygame.color.Color('White'), self.snake.rect)
        # pygame.display.update()
        # pygame.draw.rect(self._display_surf, WHITE, self.snake.rect)
            # all_sprite_list.empty()
            # all_sprite_list.add(self.body)
            # all_sprite_list.draw(self._display_surf)
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