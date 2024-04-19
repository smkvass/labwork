import pygame
import random #generating random numbers

pygame.init()#Initializes all Pygame modules

WIDTH = 700
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE GAME")
clock = pygame.time.Clock() #control the frame rate of the game
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
background = white

snake_block = 10 #размер блока змеи
snake_speed = 15

font_style = pygame.font.SysFont(None, 35)

def our_snake(snake_block, snake_list): #координаты и размеры прямоугольника
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

def message(txt, color):
    text = font_style.render(txt, True, color)
    screen.blit(text, (100,30)) #отображает изобрж тектста,

def show_score(number):
    score = font_style.render("Your score: " + str(number), True, black)
    screen.blit(score, [280, 40])


def gameSnake():

    game_over = False
    game_close = False
    #начальные координаты головы змеи по центру экрана
    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0
    #список координат блоков змеи
    snake_List = []
    #басында денесі бір блоктан тұрады
    length_of_snake = 1

    food_width = random.randint(10,15) #предел (10,15)
    food_height = random.randint(10,15)
    food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
    food_time = 5000 #5 секунд 
    last_food = pygame.time.get_ticks() #уақыт миллисекундта
    
    while not game_over:

        while game_close:
            screen.fill(white)
            message("PRESS r - repeat, c - close. Your score is: " + str(length_of_snake - 1), red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameSnake()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
          
        x1 += x1_change
        y1 += y1_change
        screen.fill(white) #бірінші очистка жасайды кейін экран ақ болады
        
        
        if pygame.time.get_ticks() - last_food > food_time:
            food_x = round(random.randrange(0, WIDTH - food_width) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - food_height) / 10.0) * 10.0
            food_width = random.randint(5, 15)
            food_height = random.randint(5, 15)
            last_food = pygame.time.get_ticks()
      
        #еда на экране
        pygame.draw.rect(screen, red, [food_x, food_y, food_width, food_height])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]

        our_snake(snake_block, snake_List) #змеяны экранда көрсету
        show_score(length_of_snake - 1)
        
        #жыланның басы тамақтың координатасына сәйкес келеме
        if x1 >= food_x and x1 <= food_x + food_width and y1 >= food_y and y1 <= food_y + food_height:
            food_x = round(random.randrange(0, WIDTH - food_width) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - food_height) / 10.0) * 10.0
            food_width = random.randint(10, 15)
            food_height = random.randint(10, 15)

            length_of_snake += 1 #тамақ жегенде блок өседі
            last_food = pygame.time.get_ticks()

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameSnake()