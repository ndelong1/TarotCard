"""tarot_card.py
A class object to select the tarot cards
Shuffle the tarot cards
"""

import pygame as pg
import os

'''
Load card images (78 different cards)
'''

class TarotCard:
    def __init__(self, screen, card, right, left, rotation=90, scale_x=800, scale_y=400): #sets up class attributes and PYGAME instance
        self.screen = screen
        self.card = card
        self.right = right #X coord
        self.left = left #Y coord
        self.rotation = rotation
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.image_lst = []
        
        pg.init() #calling the init to be able to use the pygame module       
        
        #Load each image from Assests folder
        img_file_path = "C:\\CSC_FINAL\\Cards"
        img_file_ls = [f for f in os.listdir(img_file_path) if f.endswith('.png')]
        
        #Appends each card file into a list [0-77]
        for file in img_file_ls:
            img_path = os.path.join(img_file_path, file)
            img = pg.image.load(img_path)
            self.image_lst.append(img)
            #print("Loaded file", file)   
            
             
        #print(self.image_lst) 
        
    def draw_card(self):# draws the card onto the screen when called
        #Scales and rotates the image of the card that is being drawn 
        scaled = pg.transform.scale(self.image_lst[self.card], (self.scale_x, self.scale_y))
        rotated = pg.transform.rotate(scaled, self.rotation)
        
        #Draws the card in this code snippet
        self.screen.blit(rotated, (self.right, self.left))
        

if __name__ == '__main__':
    app = TarotCard(None, None, None, None, None)
    