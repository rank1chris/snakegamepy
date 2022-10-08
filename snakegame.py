import pygame 
import random

pygame.init()

# Começo das Partes editáveis!

gameTitle = 'snakegame'
gameClock = 20
backgroundColor = 0, 0, 0
snakeColor = 255, 255, 255
foodColor = 0, 0, 255
typeofFont ='bahnschrift'
sizeofFont = 20
colorOfScore = 255, 255, 255

# Fim das partes editáveis!

width = 400
height = 400
x, y = width/2, height/2
delta_x, delta_y = 10, 0
clock = pygame.time.Clock()
food_x = random.randrange(0, width)//10*10
food_y = random.randrange(0, height)//10*10

font = pygame.font.SysFont(typeofFont, sizeofFont)

game_over = False

body_list = [(x, y)]

game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(gameTitle)

def snake():
    global x, y, delta_x, delta_y, clock, food_x, food_y, body_list, game_over
    x = (delta_x + x)%width
    y = (delta_y + y)%height
    
    if (x, y) in body_list:
        game_over = True
        return
    
    body_list.append((x, y))
    
    if (food_x == x and food_y == y):
        while ((food_x, food_y) in body_list):
            food_x = random.randrange(0, width)//10*10
            food_y = random.randrange(0, height)//10*10
    else:
        del body_list[0]        
    
    game_screen.fill(backgroundColor)
    score = font.render("Score: " + str(len(body_list) - 1), True, colorOfScore)
    game_screen.blit(score, (0, 0))
    for (i, j) in body_list:   
        pygame.draw.rect(game_screen, snakeColor, (i, j, 10, 10))
    pygame.draw.rect(game_screen, foodColor, (food_x, food_y, 10, 10))
    pygame.display.update()
    
while True:
    events = pygame.event.get()
    for event in events:
        if game_over == True:
            game_screen.fill((0, 0, 0))
            msg = font.render('Game Over!', True, (255, 0, 0))
            game_screen.blit(msg, (x, y))
            pygame.display.update()
            pygame.quit()
            quit()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delta_y = 0
                if delta_x != 10:
                    delta_x = -10
            elif event.key == pygame.K_RIGHT:
                delta_y = 0
                if delta_x != -10:
                    delta_x = 10
            elif event.key == pygame.K_UP:
                delta_x = 0
                if delta_y != 10:
                    delta_y = -10                
            elif event.key == pygame.K_DOWN:
                delta_x = 0
                if delta_y != -10:
                    delta_y = 10     
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()           
            else:
                continue
            snake()
    if (not events):
        snake()
    clock.tick(gameClock)