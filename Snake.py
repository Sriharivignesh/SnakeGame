import pygame
import time
import random
import os

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,200,0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_FPS = 30

pygame.init()

#Display initialisation
game_canvas = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#Display title 
pygame.display.set_caption('SNAKE - RECREATION')

# Game Loop driver
game_continue = True

# Set the initial key status
key_continue = pygame.K_DOWN

#Set text font for in game messages
game_font = pygame.font.SysFont(None,25)

#Function that will blit in game messages on the screen
def message_to_screen(message,color):
    screen_text = game_font.render(message,True,color)
    game_canvas.blit(screen_text,[SCREEN_WIDTH/2,SCREEN_HEIGHT/2])

#Set green background and update the display
game_canvas.fill(GREEN)
pygame.display.update()

#Get clock object to make game run at a particular FPS rate
game_clock = pygame.time.Clock()

#Set starting points of snake and other snake and apple parameters
snake_x = 10
snake_y = 10
snake_length = 1
snake_block_length = 10
apple_x = random.randrange(0,SCREEN_WIDTH,10)
apple_y = random.randrange(0,SCREEN_HEIGHT,10)
snake_body = []

while game_continue:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            game_continue = False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_UP and key_continue != pygame.K_DOWN):
                key_continue = pygame.K_UP
            elif(event.key == pygame.K_DOWN and key_continue != pygame.K_UP):
                key_continue = pygame.K_DOWN
            elif(event.key == pygame.K_LEFT and key_continue != pygame.K_RIGHT):
                key_continue = pygame.K_LEFT
            elif(event.key == pygame.K_RIGHT and key_continue != pygame.K_LEFT):
                key_continue = pygame.K_RIGHT
    if(key_continue == pygame.K_DOWN):
        snake_y += 10
    if(key_continue == pygame.K_UP):
        snake_y -= 10
    if(key_continue == pygame.K_LEFT):
        snake_x -= 10
    if(key_continue == pygame.K_RIGHT):
        snake_x += 10
    if(snake_x < 0):
        snake_x = 790
    elif(snake_x > 790):
        snake_x = 0
    if(snake_y < 0):
        snake_y = 590
    elif(snake_y > 590):
        snake_y = 0
    if(snake_x == apple_x and snake_y == apple_y):
        apple_x = random.randrange(0,SCREEN_WIDTH,10)
        apple_y = random.randrange(0,SCREEN_HEIGHT,10)
        snake_length += 1

    snake_body.append([snake_x,snake_y])

    #Doing this makes the snake bend when the length if sufficiently large
    if len(snake_body) > snake_length:
        del snake_body[0] 
    
    #Exit if snake head coordinates are found twice in the snake body list since it will mean that collision has occurred
    if snake_body.count(snake_body[0]) > 1:
        game_continue = False


    game_canvas.fill(GREEN)
    game_canvas.fill(RED,rect = [apple_x,apple_y,10,10])
    pygame.display.update()


    for XnY in snake_body:
        game_canvas.fill(BLACK,rect = [XnY[0],XnY[1],10,snake_block_length])


    pygame.display.update()
    game_clock.tick(GAME_FPS)


#Game over messages
message_to_screen("See You Next Time!", BLACK)
pygame.display.update()
time.sleep(2)
pygame.quit()

quit()