import pygame
from pygame.locals import *

def draw():
    screen.fill((255, 255, 255))  # Set background color to white

    # Blue color
    blue = (54, 60, 146)
    
    # White color
    white = (255, 255, 255)
    
    # Red color
    red = (221, 0, 39)
    
    # Draw first mountain
    pygame.draw.polygon(screen, blue, [(680, 414), (295, 776), (1067, 776)])
    
    # Draw second mountain
    pygame.draw.polygon(screen, blue, [(928, 564), (563, 834), (1292, 834)])
    
    # Draw snow on first mountain
    pygame.draw.polygon(screen, white, [(680, 432), (590, 522), (770, 522)])
    
    # Draw front of second mountain
    pygame.draw.polygon(screen, white, [(928, 599), (630, 843), (1226, 843)])
    
    # Draw stupa border
    pygame.draw.circle(screen, blue, (418, 1024), 437, width=50)
    
    # Draw face border
    pygame.draw.rect(screen, blue, (291, 439, 203, 172))
    
    # Draw shrine
    pygame.draw.polygon(screen, blue, [(393, -17), (296, 441), (489, 441)])
    
    # Draw stupa front
    pygame.draw.circle(screen, white, (419, 1024), 402)
    
    # Draw face front
    pygame.draw.rect(screen, white, (307, 461, 167, 138))
    
    # Draw head top
    pygame.draw.polygon(screen, red, [(393, 370), (337, 441), (449, 441)])
    
    # Draw head top light
    pygame.draw.polygon(screen, white, [(393, 389), (353, 441), (433, 441)])
    
    # Draw head hat
    pygame.draw.rect(screen, red, (281, 439, 223, 27))
    
    # Draw mask
    pygame.draw.rect(screen, white, (0, 539, 433, 485))
    
    # Draw bottom beam
    pygame.draw.rect(screen, red, (22, 783, 472, 31))
    
    # Draw bottom layer
    pygame.draw.polygon(screen, blue, [(252, 609), (27, 776), (477, 776)])
    
    # Draw gap
    pygame.draw.rect(screen, white, (137, 633, 229, 32))
    
    # Draw top beam
    pygame.draw.rect(screen, red, (92, 607, 314, 26))
    
    # Draw top layer
    pygame.draw.polygon(screen, blue, [(247, 461), (98, 598), (395, 598)])
    
    # Draw gap
    pygame.draw.polygon(screen, white, [(247, 461), (190, 511), (303, 511)])
    
    # Draw gap in shrine
    for i in range(72, 356, 31):
        pygame.draw.rect(screen, white, (306, i, 178, 14))
    
    # Draw shrine
    pygame.draw.polygon(screen, blue, [(246, 466), (228, 499), (263, 499)])
    
    # Draw text rectangles
    pygame.draw.rect(screen, white, (19, 874, 45, 150))
    pygame.draw.rect(screen, white, (167, 874, 45, 150))
    pygame.draw.rect(screen, white, (370, 874, 49, 150))
    pygame.draw.rect(screen, white, (300, 874, 189, 37))
    pygame.draw.rect(screen, white, (579, 874, 48, 150))
    pygame.draw.rect(screen, white, (709, 874, 46, 150))
    pygame.draw.rect(screen, white, (579, 930, 176, 37))
    pygame.draw.rect(screen, white, (579, 977, 176, 37))
    pygame.draw.rect(screen, white, (579, 874, 176, 37))
    
    # Draw text triangles
    pygame.draw.polygon(screen, white, [(62.5, 875.5), (170.5, 963.5), (173.5, 1022.5)])
    pygame.draw.polygon(screen, white, [(62.5, 875.5), (62.5, 940.5), (173.5, 1022.5)])
    
 
    
    # Load font
    font = pygame.font.Font(None, 200)  # Load a font with size 100

    # Render text
    text_surface = font.render("N  T  B", True, (54, 60, 146))  # Render "NTB" with black color

    # Blit the text onto the screen at the bottom left corner of the logo
    screen.blit(text_surface, (70, 850))
    pygame.display.flip()

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    global screen
    screen = pygame.display.set_mode((1024, 1024))  # Set screen size
    pygame.display.set_caption("Mountain Scene")    # Set window title

    clock = pygame.time.Clock()  # Create a Clock object to control frame rate
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Exit the loop when the user closes the window

        # Fill the screen with white
        screen.fill((255, 255, 255))

        draw()  # Call the draw function to draw the logo with "NTB" integrated

        pygame.display.flip()  # Update the display
        clock.tick(60)         # Cap the frame rate at 60 FPS

    pygame.quit()  # Clean up and quit Pygame when the loop exits

if __name__ == "__main__":
    main()