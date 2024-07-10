import pygame
import math

pygame.init()

win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Einfacher Pygame Start")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

a_length = 390.51
b_length = 390.51
c_length = 500

point1 = (450, 100)  
point3 = (700, 400)  
point2 = (200, 400)  

font_height = 32
font = pygame.font.Font(None, font_height)

a_text = "a  "
b_text = "b  "
c_text = "c  "
a_user_text = ""
b_user_text = ""
c_user_text = ""

a_input_rect = pygame.Rect(10, 10, 140, 32)
b_input_rect = pygame.Rect(10, 50, 140, 32)
c_input_rect = pygame.Rect(10, 90, 140, 32)

input_color_active = pygame.Color("azure3")
input_color_passive = pygame.Color("black")

a_input_color = input_color_passive
b_input_color = input_color_passive
c_input_color = input_color_passive

input_active = None  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if a_input_rect.collidepoint(event.pos):
                input_active = 'a'
            elif b_input_rect.collidepoint(event.pos):
                input_active = 'b'
            elif c_input_rect.collidepoint(event.pos):
                input_active = 'c'
            else: 
                input_active = None

        if event.type == pygame.KEYDOWN:
            if input_active == 'a':
                if event.key == pygame.K_BACKSPACE:
                    a_user_text = a_user_text[0:-1]
                else:
                    a_user_text += event.unicode
            elif input_active == 'b':
                if event.key == pygame.K_BACKSPACE:
                    b_user_text = b_user_text[0:-1]
                else:
                    b_user_text += event.unicode
            elif input_active == 'c':
                if event.key == pygame.K_BACKSPACE:
                    c_user_text = c_user_text[0:-1]
                else:
                    c_user_text += event.unicode

    win.fill(WHITE) 
    
    #get the longest line 
    longest_line = max(a_length, b_length, c_length)    

       
    # Get the midlle of a line for a 
    length_a_x = max(point3[0], point1[0]) - min(point3[0], point1[0]) #Takes the higher num - lower num
    half_length_a_x = length_a_x // 2
    
    length_a_y = max(point3[1], point1[1]) - min(point3[1], point1[1])
    half_length_a_y = length_a_y // 2
    # Add that to the smaller cord 
    middle_a_x = half_length_a_x + point1[0]
    middle_a_y = half_length_a_y + point1[1]
    
    ###B###
    length_b_x = max(point1[0], point2[0]) - min(point1[0], point2[0])
    half_length_b_x = length_b_x // 2

    length_b_y = max(point1[1], point2[1]) - min(point1[1], point2[1])
    half_length_b_y = length_b_y // 2
    
    middle_b_x = half_length_b_x + point2[0]
    middle_b_y = half_length_b_y + point1[1]
    
    ###C###
    length_c_x = max(point3[0], point2[0]) - min(point3[0], point2[0])
    half_length_c_x = length_c_x // 2

    length_c_y = max(point3[1], point2[1]) - min(point3[1], point2[1])
    half_length_c_y = length_c_y // 2

    middle_c_x = half_length_c_x + point2[0]
    middle_c_y = half_length_c_y + point2[1]
    

    win.blit(font.render("a", True, BLACK), (middle_a_x, middle_a_y))
    win.blit(font.render("b", True, BLACK), (middle_b_x, middle_b_y))
    win.blit(font.render("c", True, BLACK), (middle_c_x, middle_c_y))
    
    pygame.draw.line(win, RED, point1, point2, 5)
    pygame.draw.line(win, GREEN, point2, point3, 5)
    pygame.draw.line(win, BLUE, point3, point1, 5)
    
    a_input_color = input_color_active if input_active == 'a' else input_color_passive
    b_input_color = input_color_active if input_active == 'b' else input_color_passive
    c_input_color = input_color_active if input_active == 'c' else input_color_passive
    
    pygame.draw.rect(win, a_input_color, a_input_rect, 3)
    pygame.draw.rect(win, b_input_color, b_input_rect, 3)
    pygame.draw.rect(win, c_input_color, c_input_rect, 3)
    
    a_text_surface = font.render(a_text + a_user_text, True, BLACK)
    b_text_surface = font.render(b_text + b_user_text, True, BLACK)
    c_text_surface = font.render(c_text + c_user_text, True, BLACK)
    
    win.blit(a_text_surface, (a_input_rect.x + 5, a_input_rect.y + 5))
    win.blit(b_text_surface, (b_input_rect.x + 5, b_input_rect.y + 5))
    win.blit(c_text_surface, (c_input_rect.x + 5, c_input_rect.y + 5))
    
    a_input_rect.w = max(100, a_text_surface.get_width() + 10)
    b_input_rect.w = max(100, b_text_surface.get_width() + 10)
    c_input_rect.w = max(100, c_text_surface.get_width() + 10)

    pygame.display.flip()

pygame.quit()
