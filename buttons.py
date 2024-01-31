"""Class to 'Automate' button rendering in Pygames:
Creates the pygame.draw.rect 
with x and y coords, text, and color changing when mouse hovers over the rectangle"""
import pygame as pg

pg.init()
pg.font.init()


font = pg.font.Font('fonts/PRISTINA.TTF', 18)


class Button:
    def __init__(self, screen, text, font, x_pos, y_pos, sizex=300, sizey=70,  enabled=True): #Class Attributes
        self.screen = screen
        self.text = text
        self.font = font
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.sizex = sizex
        self.sizey = sizey
        self.enabled = enabled
        
        #draws the button on the screen by creating a button instance (button1 = Button(screen, text, font, x, y) in another file.)
        self.draw()
        
    def draw(self):
        
        #Create the Text render and the Button Rectangle
        button_text = self.font.render(self.text, True, 'black')
        button_rect = pg.rect.Rect((self.x_pos, self.y_pos),(self.sizex, self.sizey))
        
        #Positions the text in the middle of the button
        text_x = self.x_pos + (button_rect.width - button_text.get_width()) // 2
        text_y = self.y_pos + (button_rect.height - button_text.get_height()) // 2

        #Changes the Buttons color if the button has been clicked
        #Blacks out the Button if it is DISABLED
        if self.enabled:
            if self.get_clicked():
                pg.draw.rect(self.screen, 'dark grey', button_rect, 0, 5)
            else:
                pg.draw.rect(self.screen, 'light grey', button_rect, 0, 5)
        else:
            pg.draw.rect(self.screen, 'black', button_rect, 0, 5)
    
        #Draws the Button outline and button
        pg.draw.rect(self.screen, 'black', button_rect, 2, 5)
        self.screen.blit(button_text, (text_x, text_y))
        
    def get_clicked(self):#Checks to see if user clicked button
        
        #Gathering info on the mouse position and the position of the button
        mouse_pos = pg.mouse.get_pos()
        mouse_left = pg.mouse.get_pressed()[0]
        button_rect = pg.rect.Rect((self.x_pos, self.y_pos),(self.sizex, self.sizey))
        
        #Checks if mouse and button are in the same pixel and if the button is enabled
        #Returns True for if statement to create what happens when button is pressed
        if mouse_left and button_rect.collidepoint(mouse_pos) and self.enabled:  #.collidepoint is a method of the Rect class in Pygame
            return True
        else:
            return False #If any of the above are not True the button will return False