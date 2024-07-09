import pygame

pygame.init()

win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Einfacher Pygame Start")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

point1 = (400, 100)  
point2 = (300, 400)  
point3 = (500, 400)  
triangle_points = [point1, point2, point3]

font = pygame.font.Font(None, 32)
user_text = ""

input_rect = pygame.Rect(10, 10, 140, 32)
input_color_active = pygame.Color("azure3")
input_color_passive = pygame.Color("black")
input_color = input_color_passive

input_active = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                input_active = True
            else: 
                input_active = False
                            
        if event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[0:-1] # goes to last and deleats it
                else:
                    user_text += event.unicode

    win.fill(WHITE)
    
    if input_active:
        input_color = input_color_active
    else:
        input_color = input_color_passive
    
    pygame.draw.rect(win, input_color, input_rect, 3)
    
    text_surface = font.render(user_text, True, BLACK)
    win.blit(text_surface, (input_rect.x  + 5, input_rect.y + 5))
    
    input_rect.w = max(100, text_surface.get_width() + 10) #the biggest value is taken
    
    pygame.draw.line(win, RED, point1, point2, 5) 
    pygame.draw.line(win, GREEN, point2, point3, 5)  
    pygame.draw.line(win, BLUE, point3, point1, 5) 
    
    pygame.display.flip()

pygame.quit()
