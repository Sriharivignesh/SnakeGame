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
GAME_FPS = 16

pygame.init()
game_canvas = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('SNAKE - RECREATION')

# Decides whether the game loop will continue
game_continue = True

# Set the initial key status
key_continue = pygame.K_DOWN

game_font = pygame.font.SysFont(None,25)

def message_to_screen(message,color):
    screen_text = game_font.render(message,True,color)
    game_canvas.blit(screen_text,[SCREEN_WIDTH/2,SCREEN_HEIGHT/2])

game_canvas.fill(GREEN)
pygame.display.update()
game_clock = pygame.time.Clock()

snake_x = 10
snake_y = 10
snake_length = 1
snake_block_length = 10
apple_x = random.randrange(0,SCREEN_WIDTH,10)
apple_y = random.randrange(0,SCREEN_HEIGHT,10)
snake_body = []
#snake_body.append([snake_x, snake_y])

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
    if len(snake_body) > snake_length:
        del snake_body[0] 
    

        
    game_canvas.fill(GREEN)
    game_canvas.fill(RED,rect = [apple_x,apple_y,10,10])
    pygame.display.update()
    for XnY in snake_body:
        game_canvas.fill(BLACK,rect = [XnY[0],XnY[1],10,snake_block_length])
        #pygame.draw.rect(game_canvas, BLACK, [XnY[0],XnY[1],snake_block_length,snake_block_length])


    pygame.display.update()
    game_clock.tick(GAME_FPS)

message_to_screen("See You Next Time!", BLACK)
pygame.display.update()
time.sleep(2)
pygame.quit()

quit()