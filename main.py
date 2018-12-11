import pygame
from pygame.locals import *
from Classes import Snake
from Classes import Food
from Classes import Block


RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


all_sprite_list = pygame.sprite.Group()


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 400, 400
        self.snake = Snake(WHITE, 10, 10, 20, 20)
        self.body = []
        self.body.append(self.snake)

        
    
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
        movement = {pygame.K_UP: (0, -1),
                    pygame.K_DOWN: (0, 1),
                    pygame.K_LEFT: (-1, 0),
                    pygame.K_RIGHT: (1, 0)}
        move = (0,0)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == pygame.KEYDOWN:
        #         if event.type == pygame.KEYDOWN:
        #             move = movement.get(event.key, move)
        # multipliedMove = map(lambda x: x*10, move)
        # self.snake.rect.move_ip(tuple(multipliedMove))
        # self._display_surf.fill(pygame.color.Color('Black'))
        # pygame.draw.rect(self._display_surf, pygame.color.Color('White'), self.snake.rect)
        # pygame.display.update()
        
                if event.key == pygame.K_LEFT:
                    # TODO: move Snake move to the left
                    move = self.snake.moveLeft()
                    # self.body.pop()
                    # self.body.append(self.snake.moveLeft())
                    print("LEFT")
                if event.key == pygame.K_RIGHT:
                    # TODO: make Snake move to the right
                    move = self.snake.moveRight()
                    print("RIGHT")
                if event.key == pygame.K_UP:
                    # TODO: make Snake move up
                    move = self.snake.moveUp()
                    # self.body.pop()
                    # self.body.append(self.snake.moveUp())
                    print("UP")
                if event.key == pygame.K_DOWN:
                    # TODO: make Snake move down
                    move = self.snake.moveDown()
                    # self.body.pop()
                    # self.body.append(self.snake.moveDown())
                    print("DOWN")
        self.snake.rect.move_ip(move)
        self._display_surf.fill(pygame.color.Color('Black'))
        pygame.draw.rect(self._display_surf, pygame.color.Color('White'), self.snake.rect)
        pygame.display.update()
        pygame.draw.rect(self._display_surf, WHITE, self.snake.rect)
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