import pygame
from snake import Snake
from food import Food
from jugador import Player 


class Game:
    def __init__(self):
        self.snake=Snake()
        self.food=Food()
        self.player=Player()
        self.ancho=200
        self.largo=200
        self.screen=pygame.display.set_mode((self.ancho,self.largo))
        self.clock=pygame.time.Clock()
        self.fps=60
    
    def checkKeys(self):
        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]: self.snake.direction="UP"
        elif keys[pygame.K_DOWN]: self.snake.direction="DOWN"
        elif keys[pygame.K_RIGHT]: self.snake.direction="RIGHT"
        elif keys[pygame.K_LEFT]: self.snake.direction="LEFT"


    def checkEat(self):
        self.foodRect=pygame.Rect(self.food.x, self.food.y, self.food.size, self.food.size)
        self.snakeHeadRect=pygame.Rect(self.snake.body[0][0], self.snake.body[0][1], 10, 10)
        if pygame.Rect.colliderect(self.foodRect, self.snakeHeadRect):
            self.food.status = "eaten"
            self.snake.eat()
        
           
            
            
    def run (self):
        pygame.init()
        while True:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()

            self.screen.fill((255,255,255))
            for celda in self.snake.body:
                pygame.draw.rect(self.screen, self.snake.color, (celda[0],celda[1],10,10))
                
            pygame.draw.circle(self.screen, self.food.color, (self.food.x,self.food.y),5)
            
            if self.food.status == "eaten":
                self.food.putfood(200,200)
                self.food.status = "inactive"
            

            
            self.checkKeys()
            self.checkEat()
            self.snake.move()
            
            pygame.display.flip()
            

mygame=Game()
mygame.run()