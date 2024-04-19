import pygame
pygame.init()

fps = 60 #частота пөр секонд 
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_size = 0
active_color = 'white'
active_figure = 0
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('PAINT')
painting = []

    
def draw_menu(size, color, figures):
    pygame.draw.rect(screen, 'gray', [0,0,WIDTH, 70])
    pygame.draw.line(screen, 'black', (0,70), (WIDTH, 70) ,3)
    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    l_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (95, 35), 15)
    m_brush = pygame.draw.rect(screen, 'black', [130, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (155, 35), 10)
    s_brush = pygame.draw.rect(screen, 'black', [190, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (215, 35), 5)
    brush_list=[xl_brush, l_brush, m_brush,s_brush]
    #КВАДРАТТЫ БАСҚАНДА ЖАСЫЛ БОРДЕР БОЛАДЫ
    if size == 20:
        pygame.draw.rect(screen, 'green', [10,10,50,50],3)
    elif size == 15:
        pygame.draw.rect(screen, 'green', [70,10,50,50],3)
    elif size == 10:
        pygame.draw.rect(screen, 'green', [130,10,50,50],3)
    elif size == 5:
        pygame.draw.rect(screen, 'green', [190,10,50,50],3)  
    
    #ТАҢДАҒАН ЦВЕТ ТҮСІ ШЕҢБЕР ІШІНДЕ       
    draw_circle = pygame.draw.circle(screen, color, (400, 35), 30)
    draw_rect = pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)
    
    
    blue = pygame.draw.rect(screen, (0,0,255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255,0,0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0,255,0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255,255,0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0,255,255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255,0,255), [WIDTH - 85, 35, 25, 25])
    white = pygame.draw.rect(screen, (255,255,255), [WIDTH - 110, 10, 25, 25])
    black = pygame.draw.rect(screen, (0,0,0), [WIDTH - 110, 35, 25, 25]) 
    
    #фигура чтобы выбрать
    pygame.draw.circle(screen, (255,255,255), (480, 25), 15)
    circle = pygame.draw.circle(screen, 'black', (480,25),15, 2)
    
    pygame.draw.rect(screen, (255,255,255), [WIDTH - 290, 10, 22,30])
    rect = pygame.draw.rect(screen, 'black', [WIDTH - 290, 10, 22,30], 2)
    #теңбүйірлі үшбұрыш
    pygame.draw.polygon(screen, 'white', ((550,35), (560,8), (570,35)))
    eq_triangle = pygame.draw.polygon(screen, 'black', ((550,35), (560,8), (570,35)), 2)
    
    pygame.draw.polygon(screen, 'white',((480,60), (500,40), (520, 60)) )
    right_triangle = pygame.draw.polygon(screen, 'black',((480,60), (500,40), (520, 60)),2 )
    #rhombus 
    pygame.draw.polygon(screen, 'white',((535,50), (545,40), (555, 50),(545,65)))
    rhombus = pygame.draw.polygon(screen, 'black',((535,50), (545,40), (555, 50),(545,65)), 2)
    
    figures = [circle, rect, eq_triangle, right_triangle, rhombus]
    color_rect = [blue, red, green, yellow, teal, purple, white, black]
    rgb_list = [(0,0,255), (255,0,0), (0,255,0), (255,255,0),(0,255,255), (255,0,255),(255,255,255),(0,0,0)]
    return brush_list, color_rect, rgb_list, figures
    
def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(screen, paints[i][0],paints[i][1], paints[i][2])
    
run = True
while run:
    timer.tick(fps)# кол-во кадров в секунду 
    screen.fill((255,255,255))
    mouse = pygame.mouse.get_pos() #get the coordinates of the mouse
    left_click = pygame.mouse.get_pressed()[0] #нажата ли левая сторона мыши именно первый элемент
    
    
    if left_click and mouse[1] > 0: #not over the menu
        painting.append((active_color, mouse, active_size, active_figure))
    draw_painting(painting)
    
    if mouse[1] > 0:
        pygame.draw.circle(screen, active_color, mouse, active_size, active_figure)
    brushes, colors, rgbs, figures = draw_menu(active_size, active_color, active_figure)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)): # все кисти в списке
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)
                    
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]
                    

    pygame.display.flip()
pygame.quit()