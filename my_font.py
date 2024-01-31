"""Class for rendering fonts in pygames"""

import pygame as pg

class MyFont:
    def __init__(self, size):
        self.size = size
        
    def font_A(self):
        self.A = pg.font.Font('fonts/1942.ttf', self.size)
        return self.A
    
    def font_B(self):
        self.B = pg.font.Font('fonts/OldNewspaperTypes.ttf', self.size)
        return self.B
    
    def font_C(self):
        self.C = pg.font.Font('fonts/ITCBLKAD.TTF', self.size)
        return self.C
    
    def font_D(self):
        self.D = pg.font.Font('fonts/PAPYRUS.TTF', self.size)
        return self.D
    
    def font_E(self):
        self.E = pg.font.Font('fonts/PARCHM.TTF', self.size)
        return self.E
    
    def font_F(self):
        self.F = pg.font.Font('fonts/PRISTINA.TTF', self.size)
        return self.F
    
    def font_G(self):
        self.G = pg.font.Font('fonts/consola.ttf', self.size)
        return self.G
    
    def font_H(self):
        self.H = pg.font.Font('fonts\VINERITC.TTF', self.size)
        return self.H
    
    def font_I(self):
        self.I = pg.font.Font('fonts/CHILLER.TTF', self.size)
        return self.I