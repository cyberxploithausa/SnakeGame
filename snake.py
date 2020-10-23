############################################################
#####                   CYBERXPLOIT                    #####
##### PROJECT NAME: SNAKE                              #####
##### PROJECT ID: CYBX002                              #####
#####                                                  #####
############################################################

#Importing the pygame module and random module
import pygame
from random import randint

pygame.init()

width = 750
height = 600

win = pygame.display.set_mode((width, height))

pygame.display.set_caption('Snake Game')

#Colours to be used in the entire development of the game
red = (255, 0, 0)
green = (0, 255, 0)
purple = (255, 0, 255)
black = (0, 0, 0)

#Game Objects "Snake, Food, Bomb"
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([25, 25])
        self.image.fill(black)
        self.rect = self.image.get_rect() 
        self.score = 0
        self.highscore = 0
        self.speed = 10
        self.dx = 0
        self.dy = 0 

class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(red)
        self.rect = self.image.get_rect()
    def move(self):
        food.rect.x = randint(50, width - 50)
        food.rect.y = randint(50, height - 50)

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([25, 25])
        self.image.fill(purple)
        self.rect = self.image.get_rect()

#where to draw game objects

snake = Snake()
snake.rect.x = width // 2
snake.rect.y = height // 2

food = Food()
food.rect.x = randint(50, width - 50)
food.rect.y = randint(50, height - 50)

#Sprites Group
sprites_group = pygame.sprite.Group()
sprites_group.add(snake)
sprites_group.add(food) 

bomb_group = pygame.sprite.Group()

#Redraw Function

def redraw():
    if playing:
        win.fill( green)

        #Score
        font = pygame.font.SysFont('Time New Roman', 24)
        score = font.render('SCORE: ' + str(snake.score), False, black)
        scoreRect = score.get_rect()
        scoreRect.center = (width // 2, 50) 
        win.blit(score, scoreRect)
        
        
        #Draw Sprite Groups
        sprites_group.update()
        sprites_group.draw(win)
        bomb_group.update()
        bomb_group.draw(win)
    else:
        win.fill(black)
        font = pygame.font.SysFont('Arial black', 60)

        #Title
        title = font.render('SNAKE', False, green)
        titleRect = title.get_rect()
        titleRect.center = (width // 2, 100)
        win.blit(title, titleRect)

        #High score
        high = font.render('High Score: ' + str(snake.highscore),  False, purple)
        highRect = high.get_rect()
        highRect.center = (width // 2, height // 2)
        win.blit(high, highRect)

        #Start
        start = font.render('Press Space to start',  False, (randint(0, 255), randint(0, 255), randint(0, 255)))
        startRect = start.get_rect()
        startRect.center = (width // 2, height - 100)
        win.blit(start, startRect)



    pygame.display.update()

#Main loop
run = True
playing = False


while run:

    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    if playing:
        #Snake movement
        snake.rect.x += snake.dx
        snake.rect.y += snake.dy

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            snake.dx = -snake.speed
            snake.dy = 0
        if key[pygame.K_RIGHT]:
            snake.dx = snake.speed
            snake.dy = 0
        if key[pygame.K_UP]:
            snake.dy = -snake.speed
            snake.dx = 0
        if key[pygame.K_DOWN]:
            snake.dy = snake.speed   
            snake.dx = 0

        #Collision
        if snake.rect.colliderect(food.rect):
            food.move()
            bomb = Bomb()
            bomb.rect.x = snake.rect.x + 50 
            bomb.rect.y = snake.rect.y + 50 
            bomb_group.add(bomb)
            snake.score += 1

        for bomb in bomb_group:
            if bomb.rect.colliderect(snake.rect):
                if snake.score > snake.highscore:
                    snake.highscore = snake.score
                playing  = False
    else:
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            playing = True
            snake.rect.x = width // 2
            snake.rect.y = height // 2
            snake.score = 0
            bomb_group.empty()


    redraw()

pygame.quit()







