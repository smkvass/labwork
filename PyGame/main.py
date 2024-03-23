import pygame

pygame.init()

display = pygame.display.set_mode((800,800))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()
FPS = 50

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        display.fill((255, 255, 255))
        pygame.draw.circle(display, (0, 0,0),(400, 400), 400, 4)
        pygame.display.update()
        clock.tick(FPS)
        
game()
pygame.quit()