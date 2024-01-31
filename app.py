"""app.py 

Tarot Reading app
CSC221 Final Project
Kota DeLong

“When you drop the idea of predicting the future, you start to experience the cards as a mirror of the psyche. That`s when playing with the tarot becomes a path to wisdom.”
― Philippe St Genoux 
"""
"""------------------------------------***Importing Python modules***-------------------------------------"""
import pygame as pg
import random
import csv


"""--------------------------------------***Importing My modules***---------------------------------------"""
from tarot_card import TarotCard
from horoscope import Horoscope, render_textrect
from BirthDate import BirthDate
from buttons import Button
from my_font import MyFont


class TarotApp:
    def __init__(self): #Class setup, PYGAME init, Screen setup
        pg.init()
        pg.font.init()

        #create Pygame Screen
        flags = pg.RESIZABLE | pg.DOUBLEBUF
        self.SCREEN_X = 1320
        self.SCREEN_Y = 780
        self.ROOT = pg.display.set_mode(((self.SCREEN_X), (self.SCREEN_Y)), flags=flags)
        pg.display.set_caption("Tarot Readings")
        self.CLOCK = pg.time.Clock()
        
        #Loading the back of the card image and scaling it down.     
        self.BACKCARD = pg.image.load("Assests\\card_backing.png")
        self.BACKCARD_SCALED = pg.transform.scale(self.BACKCARD, (800, 400))
        self.BACKCARD_ROTATED = pg.transform.rotate(self.BACKCARD_SCALED, 90)
        
        #Variables to effect button logic:
        self.my_triple_int = 0
        self.my_triple_bool = False
        self.my_single_bool = False
        self.my_single_int = 0
        
    """----------------------------------------***Class Methods***----------------------------------------"""  
    """------------------***StartUp and Background Methods***-----------------"""  
    def title_page(self): #Start Page
        
        #Used to display the Title Page before going into the main menu
        bg_img = pg.image.load('Assests/TitlePage3.png')
        bg_img_scale = pg.transform.scale(bg_img, (self.SCREEN_X, self.SCREEN_Y))
        
        #Time delay for text and buttons
        title_delay = 500
        subtitle_delay = 1000
        sub2_delay = 2000
        start_delay = 4000
        start_time = pg.time.get_ticks()
        start_button = None #Placeholder for the Button
        
        #Sets the Fonts used and the font size
        font_manager = MyFont(32)
        font_F = font_manager.font_F()
        font_G = font_manager.font_G()
        font_manager1 = MyFont(60)
        font_H = font_manager1.font_H()
        font_manager2 = MyFont(178)
        font_E = font_manager2.font_E()

        title_text = font_E.render("Tarot Readings", False, 'red')
        title_rect = title_text.get_rect(center=((self.SCREEN_X/2), 80))
        
        sub_text1 = font_H.render("KotaKatTech", False, 'red')
        sub_rect1 = sub_text1.get_rect(center=((self.SCREEN_X/2), 580))
        sub_text2 = font_G.render("    by:\nKota DeLong", False, 'red')
        sub_rect2 = sub_text2.get_rect(center=((self.SCREEN_X/2), 640))

        running = True
    
        while running:
            
            self.ROOT.blit(bg_img_scale, (0,0))
        
            for event in pg.event.get(): 
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                    
            current_time = pg.time.get_ticks()
            
            #Logic for when each text and button appear on screen
            if current_time - start_time >= title_delay:
                self.ROOT.blit(title_text, title_rect)
                
            if current_time - start_time >= subtitle_delay:
                self.ROOT.blit(sub_text1, sub_rect1)
                
            if current_time - start_time >= sub2_delay:
                self.ROOT.blit(sub_text2, sub_rect2)
            
            if current_time - start_time >= start_delay:
                start_button = Button(self.ROOT, "START", font_F, ((self.SCREEN_X/2) - 150), ((self.SCREEN_Y/2) - 35))
            
            if start_button and start_button.get_clicked():
                running = False
                self.main_menu()
                
            pg.display.update()
    
    def main_menu(self): #Main Menu Screen
        """Function to create the 'Main' screen of the app.
    On the [MAIN MENU] screen you will see buttons for [New Tarot Reading], [Previous Tarot Reading], [Daily Horoscope], [Tarot Info]"""    
    
        bg_img_2 = pg.image.load('Assests/TitlePage3.png')
        bg_img_2_scale = pg.transform.scale(bg_img_2, (self.SCREEN_X, self.SCREEN_Y))
    
        font_manager = MyFont(24)
        font_A = font_manager.font_A()
        font_manager2 = MyFont(178)
        font_E = font_manager2.font_E()

        title_text = font_E.render("Tarot Readings", False, 'red')
        title_rect = title_text.get_rect(center=((self.SCREEN_X/2), 80))
        
        running = True

        while running:
    
            self.ROOT.blit(bg_img_2_scale, (0,0))
            self.ROOT.blit(title_text, title_rect)
            
            for event in pg.event.get(): 
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()                
                """-----------------------------***Key inputs***-----------------------"""
                keys = pg.key.get_pressed()   
                if keys[pg.K_ESCAPE]:
                    running = False
        
            """------------------------------***Buttons***-------------------------"""        
            tarotreading = Button(self.ROOT, "New Reading", font_A, x_pos=300, y_pos=300)
            previoustarot = Button(self.ROOT, "Previous Reading", font_A, x_pos=300, y_pos=400)
            dailyhoroscope = Button(self.ROOT, "Horoscope", font_A, x_pos=700, y_pos=300)
            tarotinfo = Button(self.ROOT, "Tarot Info", font_A, x_pos=700, y_pos=400)
            quit_button = Button(self.ROOT, "Quit", font_A, x_pos=510, y_pos=580)
        
            """---------------------------***Button Logic***-----------------------"""
            
            if tarotreading.get_clicked():
                print('New Reading Button clicked')
                running = False
                pg.time.delay(300)
                self.tarot_reading()
                
            if previoustarot.get_clicked():
                running = False
                pg.time.delay(300)
                self.previous_reading() 
            
            if dailyhoroscope.get_clicked():
                running = False
                pg.time.delay(300)
                self.horoscope_screen()
                
            if tarotinfo.get_clicked():
                running = False
                pg.time.delay(300)
                self.tarot_info()
            
            if quit_button.get_clicked():
                running = False
                pg.time.delay(300)
                pg.quit()
        
            pg.display.update()
            
    def cvs_reading(self, rowx, my_rot): #One Method to Rule the CSV

        """This module exist to create one place to handle CSV events. Gathering data from TarotCard.csv
        rowx = the row in which the data is to be found in column 0 = ID
        The columns needed are the Card Name, Information Upright, and Information Reversed
        """
        
        with open('TarotCards.csv') as tarot:
            file_read = csv.DictReader(tarot)
            for row in file_read:
                if int(row['ID#']) == int(rowx):
                    if my_rot == (-90):
                        self.card_name = row['Card Name']
                        self.cardinfo = row['Information Upright']
                    elif my_rot == (90):
                        self.card_name = row['Card Name']
                        self.cardinfo = row['Information Reversed']
                    else:
                        self.card_name = "ERROR!"
                        self.cardinfo = "404"
            
            return self.card_name, self.cardinfo
        
    """------------------------***Tarot Card Reading***-----------------------"""       
    def tarot_reading(self): #To be or not to be that is the question
    
        pg.display.set_caption("Select Tarot Reading Style")
        
        font_manager = MyFont(18)
        font_A = font_manager.font_A()
        font_manager2 = MyFont(256)
        font_E = font_manager2.font_E()
        
        title_text = font_E.render("New Readings", False, 'red')
        title_rect = title_text.get_rect(center=((self.SCREEN_X/2), (self.SCREEN_Y/2 - 250)))
        
        self.my_int = 1
    
        running = True

        while running:
            self.ROOT.fill('black')
            self.ROOT.blit(title_text, title_rect)
    
            singleread = Button(self.ROOT, "Single Card", font_A, x_pos=250, y_pos=390)
            tripleread = Button(self.ROOT, "Triple Card", font_A, x_pos=750, y_pos=390)
            home_button = Button(self.ROOT, "Home", font_A, x_pos=510, y_pos=580)
        
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            if singleread.get_clicked():
                print('Single Reading is clicked')
                running = False
                pg.time.delay(300)
                self.reading_screen()
                    
            if tripleread.get_clicked():
                running = False
                pg.time.delay(300)
                self.trip_read()
                
            if home_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.main_menu()
            
            pg.display.update()
    
    """------------***SINGLE CARD***------------"""
    def reading_screen(self): #Start of Single Card Reading // Shows Single Card backing
    
        pg.display.set_caption("New Reading")
        
        bg_img_2 = pg.image.load('Assests/TitlePage3.png')
        bg_img_2_scale = pg.transform.scale(bg_img_2, (self.SCREEN_X, self.SCREEN_Y))
        font_manager = MyFont(24)
        font_A = font_manager.font_A()
        
        self.my_single_int = 1        
    
        running = True
        
        while running:
            
            self.ROOT.fill('black')
            self.ROOT.blit(bg_img_2_scale, (0,0))
            card_button = Button(self.ROOT, 'card_flip', font_A, (self.SCREEN_X//2 - 100), (self.SCREEN_Y//2 - 200), 200, 400)
            self.ROOT.blit(self.BACKCARD_ROTATED, (((self.SCREEN_X/2) - 200), ((self.SCREEN_Y/2) - 400)))
            home_button = Button(self.ROOT, 'Home', font_A, (self.SCREEN_X/2 - 150), 700)
            text4 = font_A.render("Click on the card", True, "black", "white")
            text4_rect = text4.get_rect(center=(((self.SCREEN_X/2)), ((self.SCREEN_Y/2) - 340)))
            self.ROOT.blit(text4, text4_rect)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            if card_button.get_clicked():
                running = False
                print("Card is clicked!")
                pg.time.delay(300)
                self.flip_card()
                
            if home_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.main_menu()
            
            
            pg.display.update()
            
    def flip_card(self): #Shows the face in a single card reading
        
        pg.display.set_caption('Reading')
        
        bg_img_2 = pg.image.load('Assests/TitlePage3.png')
        bg_img_2_scale = pg.transform.scale(bg_img_2, (self.SCREEN_X, self.SCREEN_Y))
        font_manager = MyFont(24)
        font_A = font_manager.font_A()
        self.num_list = []
        pos_x = ((self.SCREEN_X/2) - 200)
        pos_y = ((self.SCREEN_Y/2) - 400)
        
        for x in range(78):
            self.num_list.append(x)
        
        #print(self.num_list) #used for testing the list
        
        self.card0 = random.choice(self.num_list)
        print(self.card0)
        rotate_list = [-90, 90]
        self.rotate = random.choice(rotate_list)
        print("Rotate is ", self.rotate)
        
        self.card0_save = self.card0
        self.rotate_save = self.rotate
        
    
        self.choosen_card = TarotCard(self.ROOT, self.card0, pos_x, pos_y, self.rotate)
        
        running = True
        
        while running:
            self.ROOT.fill('black')
            self.ROOT.blit(bg_img_2_scale, (0,0))
            self.CLOCK.tick(60)
            home_button = Button(self.ROOT, 'Home', font_A, (self.SCREEN_X/2 + 50), 700)
            info_button = Button(self.ROOT, 'Card Info', font_A, ((self.SCREEN_X/2) - 350), 700)
            self.choosen_card.draw_card()
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            if home_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.main_menu()
                
            if info_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.card_info()
                
            
            pg.display.update()
            
    def card_info(self): #Displays single card information 
        
        pg.display.set_caption('Card Information')
        
        bg_img_2 = pg.image.load('Assests/TitlePage3.png')
        bg_img_2_scale = pg.transform.scale(bg_img_2, (self.SCREEN_X, self.SCREEN_Y))
        font_manager = MyFont(24)
        font_A = font_manager.font_A()
        font_manager2 = MyFont(32)
        font_G = font_manager2.font_G() 
        
        running = True
        
        while running:
            self.ROOT.fill('black')
            self.ROOT.blit(bg_img_2_scale, (0,0))
            self.CLOCK.tick(60)
            home_button = Button(self.ROOT, 'Home', font_A, (self.SCREEN_X/2 - 150), 700)
            
            csv_text = self.cvs_reading(self.card0, self.rotate)
            
            #print("Rotate still: ", self.rotate) #Testing the saved rotate variable
            
            text = font_G.render(str(csv_text), False, 'white', 'black', wraplength=500)
            text_rect = text.get_rect(center=(self.SCREEN_X//2+300, self.SCREEN_Y//2))
                
            self.ROOT.blit(text, text_rect)
            
            self.choosen_card.draw_card()
            if self.choosen_card.right >= 175:
                self.choosen_card.right -= 10  
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            if home_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.main_menu()
                
            pg.display.update()
    
    """------------***TRIPLE CARD***------------"""    
    def trip_read(self): #Start of 3 Card Reading // Shows 3 Card backings
        pg.display.set_caption("New Reading")
        
        bg_img_2 = pg.image.load('Assests/TitlePage3.png')
        bg_img_2_scale = pg.transform.scale(bg_img_2, (self.SCREEN_X, self.SCREEN_Y))
        font_manager = MyFont(24)
        font_A = font_manager.font_A()
        
        self.my_triple_int = 1
    
        running = True
        
        while running:
            
            self.ROOT.fill('black')
            self.ROOT.blit(bg_img_2_scale, (0,0))
            card_button = Button(self.ROOT, 'card_flip', font_A, (self.SCREEN_X//2 - 75), (self.SCREEN_Y//2 - 100), 150, 200)
            self.ROOT.blit(self.BACKCARD_ROTATED, (((self.SCREEN_X/2) - 600), ((self.SCREEN_Y/2) - 400)))
            self.ROOT.blit(self.BACKCARD_ROTATED, (((self.SCREEN_X/2) - 200), ((self.SCREEN_Y/2) - 400)))
            self.ROOT.blit(self.BACKCARD_ROTATED, (((self.SCREEN_X/2) + 200), ((self.SCREEN_Y/2) - 400)))
            home_button = Button(self.ROOT, 'Home', font_A, (self.SCREEN_X/2 - 150), 700)
            
            text1 = font_A.render("PAST", False, 'black', 'dark grey')
            text1_rect = text1.get_rect(center=(((self.SCREEN_X/2) - 400), ((self.SCREEN_Y/2) - 300)))
            self.ROOT.blit(text1, text1_rect)
            text2 = font_A.render("PRESENT", False, 'black', 'dark grey')
            text2_rect = text2.get_rect(center=(((self.SCREEN_X/2)), ((self.SCREEN_Y/2) - 300)))
            self.ROOT.blit(text2, text2_rect)
            text3 = font_A.render("FUTURE", False, 'black', 'dark grey')
            text3_rect = text3.get_rect(center=(((self.SCREEN_X/2) + 400), ((self.SCREEN_Y/2) - 300)))
            self.ROOT.blit(text3, text3_rect)
            
            text4 = font_A.render("Click the middle card", True, "black", "white")
            text4_rect = text4.get_rect(center=(((self.SCREEN_X/2)), ((self.SCREEN_Y/2) - 340)))
            self.ROOT.blit(text4, text4_rect)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            if card_button.get_clicked():
                running = False
                print("Card is clicked!")
                pg.time.delay(300)
                self.flip_card_trip()
                
            if home_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.main_menu()
            
            
            pg.display.update()
            
    def flip_card_trip(self): #Shows the Faces in 3 Card Reading
        
        pg.display.set_caption('Reading')
        
        bg_img_2 = pg.image.load('Assests/TitlePage3.png')
        bg_img_2_scale = pg.transform.scale(bg_img_2, (self.SCREEN_X, self.SCREEN_Y))
        font_manager = MyFont(24)
        font_A = font_manager.font_A()
        self.num_list = []
        
        for x in range(78):
            self.num_list.append(x)
        
        print(self.num_list)
        
        self.card1 = random.choice(self.num_list)
        self.num_list.remove(self.card1)
        self.card2 = random.choice(self.num_list)
        self.num_list.remove(self.card2)
        self.card3 = random.choice(self.num_list)
        self.num_list.remove(self.card3)
        print(self.card1)
        print(self.card2)
        print(self.card3)
        
        rotate_list = [-90, 90]
        self.rotate1 = random.choice(rotate_list)
        self.rotate2 = random.choice(rotate_list)
        self.rotate3 = random.choice(rotate_list)
        
        self.scalx = 800
        self.scaly = 400
        
        self.card1_save = self.card1
        self.card2_save = self.card2
        self.card3_save = self.card3
        
        self.rot1_save = self.rotate1
        self.rot2_save = self.rotate2
        self.rot3_save = self.rotate3
    
        self.past = TarotCard(self.ROOT, self.card1, ((self.SCREEN_X/2) - 600), ((self.SCREEN_Y/2) - 400), self.rotate1, scale_x=self.scalx, scale_y=self.scaly)
        self.present = TarotCard(self.ROOT, self.card2, ((self.SCREEN_X/2) - 200), ((self.SCREEN_Y/2) - 400), self.rotate2, scale_x=self.scalx, scale_y=self.scaly)
        self.future = TarotCard(self.ROOT, self.card3, ((self.SCREEN_X/2) + 200), ((self.SCREEN_Y/2) - 400), self.rotate3, scale_x=self.scalx, scale_y=self.scaly)
        
        running = True
        
        while running:
            self.ROOT.fill('black')
            self.ROOT.blit(bg_img_2_scale, (0,0))
            self.CLOCK.tick(60)
            home_button = Button(self.ROOT, 'Home', font_A, (self.SCREEN_X/2), 700)
            info_button = Button(self.ROOT, 'Card Info', font_A, ((self.SCREEN_X/2) - 350), 700)
            self.past.draw_card()
            self.present.draw_card()
            self.future.draw_card()
            
            text1 = font_A.render("PAST", False, 'black', 'dark grey')
            text1_rect = text1.get_rect(center=(((self.SCREEN_X/2) - 400), ((self.SCREEN_Y/2) - 300)))
            self.ROOT.blit(text1, text1_rect)
            text2 = font_A.render("PRESENT", False, 'black', 'dark grey')
            text2_rect = text2.get_rect(center=(((self.SCREEN_X/2)), ((self.SCREEN_Y/2) - 300)))
            self.ROOT.blit(text2, text2_rect)
            text3 = font_A.render("FUTURE", False, 'black', 'dark grey')
            text3_rect = text3.get_rect(center=(((self.SCREEN_X/2) + 400), ((self.SCREEN_Y/2) - 300)))
            self.ROOT.blit(text3, text3_rect)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            if home_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.main_menu()
                
            if info_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.card_info_trip()
                
            pg.display.update()            
            
    def card_info_trip(self): #Displays 3 Card information
        
        pg.display.set_caption('Card Information')
        
        bg_img_2 = pg.image.load('Assests/TitlePage3.png')
        bg_img_2_scale = pg.transform.scale(bg_img_2, (self.SCREEN_X, self.SCREEN_Y))
        font_manager = MyFont(24)
        font_A = font_manager.font_A()
        font_manager2 = MyFont(32)
        font_G = font_manager2.font_G() 
        
        running = True
        
        while running:
            self.ROOT.fill('black')
            self.ROOT.blit(bg_img_2_scale, (0,0))
            self.CLOCK.tick(60)
            home_button = Button(self.ROOT, 'Home', font_A, (self.SCREEN_X/2 - 150), 700)
            
            csv_text1 = self.cvs_reading(self.card1, self.rotate1)
            csv_text2 = self.cvs_reading(self.card2, self.rotate2)
            csv_text3 = self.cvs_reading(self.card3, self.rotate3)
            
            text_info1 = font_G.render(str(csv_text1), False, 'white', 'black', 500)
            text_info1_rect = text_info1.get_rect(center=(self.SCREEN_X//2 + 100, self.SCREEN_Y//2 - 220))
            self.ROOT.blit(text_info1, text_info1_rect)
            
            text_info2 = font_G.render(str(csv_text2), False, 'white', 'black', 500)
            text_info2_rect = text_info2.get_rect(center=(self.SCREEN_X//2 + 100, self.SCREEN_Y//2 - 20))
            self.ROOT.blit(text_info2, text_info2_rect)
            
            text_info3 = font_G.render(str(csv_text3), False, 'white', 'black', 500)
            text_info3_rect = text_info3.get_rect(center=(self.SCREEN_X//2 + 100, self.SCREEN_Y//2 + 200))
            self.ROOT.blit(text_info3, text_info3_rect)
            
            text1 = font_A.render("PAST", False, 'black', 'dark grey')
            text1_rect = text1.get_rect(center=(200, ((self.SCREEN_Y/2) - 220)))
            self.ROOT.blit(text1, text1_rect)
            
            text2 = font_A.render("PRESENT", False, 'black', 'dark grey')
            text2_rect = text2.get_rect(center=(200, ((self.SCREEN_Y/2) - 20)))
            self.ROOT.blit(text2, text2_rect)
            
            text3 = font_A.render("FUTURE", False, 'black', 'dark grey')
            text3_rect = text3.get_rect(center=(200, ((self.SCREEN_Y/2) + 200)))
            self.ROOT.blit(text3, text3_rect)
            
            #Changing the X scale of each card
            if self.past.scale_x == 800:
                self.past.scale_x = 300
            if self.present.scale_x == 800:
                self.present.scale_x = 300
            if self.future.scale_x == 800:
                self.future.scale_x = 300
            
            #Changing the Y scale of each card
            if self.past.scale_y == 400:
                self.past.scale_y = 150
            if self.present.scale_y == 400:
                self.present.scale_y = 150
            if self.future.scale_y == 400:
                self.future.scale_y = 150
                
                
            self.past.draw_card()
            self.present.draw_card()
            self.future.draw_card()
            
            #Change the position of each card on screen
            '''---------------***PAST***---------------'''
            if self.past.right != 300:
                self.past.right += 10
            if self.past.left != 10:
                self.past.left += 10
            
            '''------------***PRESENT***---------------'''
            if self.present.right != 300:
                self.present.right -= 10  
            if self.present.left  != 230:
                self.present.left += 10
              
            '''-------------***FUTURE***---------------'''  
            if self.future.right != 300:
                self.future.right -= 10
            if self.future.left != 450:
                self.future.left += 10
            
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            if home_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.main_menu()
                
            pg.display.update() 
    
    """---------***PREVIOUS  READING***---------"""
    def previous_reading(self): #Select Single or Triple Previous Reading
        pg.display.set_caption("Select Previous Reading Style")
        
        font_manager = MyFont(18)
        font_A = font_manager.font_A()
        font_manager1 = MyFont(24)
        font_G = font_manager1.font_G()
        font_manager2 = MyFont(256)
        font_E = font_manager2.font_E()
        
        title_text = font_E.render("Previous Readings", False, 'red')
        title_rect = title_text.get_rect(center=((self.SCREEN_X/2), (self.SCREEN_Y/2 - 250)))
        
        error_text = font_G.render("There are no Previous Readings available:\n            Try Again Later", False, 'red')
        error_rect = error_text.get_rect(center=((self.SCREEN_X/2), (self.SCREEN_Y/2)))
        
        
    
        running = True

        while running:
            self.ROOT.fill('black')
            
            """----------------------------***More Buttons***-----------------------"""
    
            singleread = Button(self.ROOT, "Single Card", font_A, x_pos=250, y_pos=390, enabled=self.my_single_bool)
            tripleread = Button(self.ROOT, "Triple Card", font_A, x_pos=750, y_pos=390, enabled=self.my_triple_bool)
            home_button = Button(self.ROOT, "Home", font_A, x_pos=510, y_pos=580)
            self.ROOT.blit(title_text, title_rect)
        
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    
            if self.my_single_int == 0 and self.my_triple_int == 0:
                self.ROOT.blit(error_text, error_rect)
            
            if self.my_single_int == 1:
                self.my_single_bool = True
            else:
                self.my_single_bool = False
            
            if self.my_triple_int == 1:
                self.my_triple_bool = True
            else:
                self.my_triple_bool = False
                
            if singleread.get_clicked():
                print('Single Reading is clicked')
                running = False
                pg.time.delay(300)
                self.saved_single()
                    
            if tripleread.get_clicked():
                running = False
                pg.time.delay(300)
                self.saved_triple()
                
            if home_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.main_menu()
            
            pg.display.update()

    def saved_single(self): #Recalls the last Single Card Reading
        
        pg.display.set_caption('Previous Single Card Reading')
        
        bg_img_2 = pg.image.load('Assests/TitlePage3.png')
        bg_img_2_scale = pg.transform.scale(bg_img_2, (self.SCREEN_X, self.SCREEN_Y))
        font_manager = MyFont(24)
        font_A = font_manager.font_A()
        font_manager2 = MyFont(32)
        font_G = font_manager2.font_G()
        
        pos_x = 165
        pos_y = ((self.SCREEN_Y/2) - 400)
        
        previous_single_card = TarotCard(self.ROOT, self.card0_save, pos_x, pos_y, self.rotate_save)
        
        card_info = self.cvs_reading(self.card0_save, self.rotate_save)
        
        title = font_G.render("Previous Single Card Reading", False, 'red')
        title_rect = title.get_rect(center=(self.SCREEN_X//2, self.SCREEN_Y//2 - 300))
        
        text = font_G.render(str(card_info), False, "white", "black", 500)
        text_rect = text.get_rect(center=(self.SCREEN_X//2+300, self.SCREEN_Y//2))
        
        running = True
        
        while running:
            self.ROOT.fill('black')
            self.ROOT.blit(bg_img_2_scale, (0,0))
            self.CLOCK.tick(60)
            home_button = Button(self.ROOT, 'Home', font_A, (self.SCREEN_X/2), 700)
            self.ROOT.blit(title, title_rect)
            previous_single_card.draw_card()
            self.ROOT.blit(text, text_rect)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            if home_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.main_menu()
            
            pg.display.update()
    
    def saved_triple(self): #Recalls the last Triple Card Reading
        
        pg.display.set_caption('Previous Single Card Reading')
        
        bg_img_2 = pg.image.load('Assests/TitlePage3.png')
        bg_img_2_scale = pg.transform.scale(bg_img_2, (self.SCREEN_X, self.SCREEN_Y))
        font_manager = MyFont(24)
        font_A = font_manager.font_A()
        font_manager2 = MyFont(32)
        font_G = font_manager2.font_G()
        
        previous_card1 = TarotCard(self.ROOT, self.card1_save, 300, 10, self.rot1_save, scale_x=300, scale_y=150)
        previous_card2 = TarotCard(self.ROOT, self.card2_save, 300, 230, self.rot2_save, scale_x=300, scale_y=150)
        previous_card3 = TarotCard(self.ROOT, self.card3_save, 300, 450, self.rot3_save, scale_x=300, scale_y=150)
        
        card1_info = self.cvs_reading(self.card1_save, self.rot1_save)
        card2_info = self.cvs_reading(self.card2_save, self.rot2_save)
        card3_info = self.cvs_reading(self.card3_save, self.rot3_save)
        
        title = font_G.render("Previous Triple Card Reading", False, 'red')
        title_rect = title.get_rect(center=(self.SCREEN_X//2 + 100, self.SCREEN_Y//2 - 320))
            
        text_info1 = font_G.render(str(card1_info), False, 'white', 'black', 500)
        text_info1_rect = text_info1.get_rect(center=(self.SCREEN_X//2 + 100, self.SCREEN_Y//2 - 220))
            
        text_info2 = font_G.render(str(card2_info), False, 'white', 'black', 500)
        text_info2_rect = text_info2.get_rect(center=(self.SCREEN_X//2 + 100, self.SCREEN_Y//2 - 20))
            
        text_info3 = font_G.render(str(card3_info), False, 'white', 'black', 500)
        text_info3_rect = text_info3.get_rect(center=(self.SCREEN_X//2 + 100, self.SCREEN_Y//2 + 200))
            
        text1 = font_A.render("PAST", False, 'black', 'dark grey')
        text1_rect = text1.get_rect(center=(200, ((self.SCREEN_Y/2) - 220)))
            
        text2 = font_A.render("PRESENT", False, 'black', 'dark grey')
        text2_rect = text2.get_rect(center=(200, ((self.SCREEN_Y/2) - 20)))
            
        text3 = font_A.render("FUTURE", False, 'black', 'dark grey')
        text3_rect = text3.get_rect(center=(200, ((self.SCREEN_Y/2) + 200)))
        
        running = True
        
        while running:
            self.ROOT.fill('black')
            self.ROOT.blit(bg_img_2_scale, (0,0))
            self.CLOCK.tick(60)
            home_button = Button(self.ROOT, 'Home', font_A, (self.SCREEN_X/2), 700)
            self.ROOT.blit(title, title_rect)
            previous_card1.draw_card()
            previous_card2.draw_card()
            previous_card3.draw_card()
            self.ROOT.blit(text_info1, text_info1_rect)
            self.ROOT.blit(text_info2, text_info2_rect)
            self.ROOT.blit(text_info3, text_info3_rect)
            self.ROOT.blit(text1, text1_rect)
            self.ROOT.blit(text2, text2_rect)
            self.ROOT.blit(text3, text3_rect)
            
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            if home_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.main_menu()
            
            pg.display.update()
    
    """--------------------------***ABOUT  PAGE***--------------------------"""
    def tarot_info(self): #An about page and Tarot information
        #Displays text on screen
        font_manager = MyFont(20)
        font = font_manager.font_G()
        font_manager2 = MyFont(24)
        font_A = font_manager2.font_A()
        
        about_text = font.render("About the Creator:", False, 'red')
        about1_text = font.render("Kota is a Computer Science Major at New River Community College. Their goals as a Computer Science Major is to transfere to a 4 year school focused in gaming and animation. They became interested in Tarot Cards back in 2015 after seeing their Aunt doing Tarot Readings at a family reunion. Noticing that there are not many Tarot Card apps on the market that help educate new readers, they decided to create their own as a class project.", False, 'white', wraplength=800)
        about_text_rect = about_text.get_rect(center=(400, 100))
        about1_rect = about1_text.get_rect(center=(660, 200))
        
        quote_text = font.render('“When you drop the idea of predicting the future, you start to experience the cards as a mirror of the psyche. That`s when playing with the tarot becomes a path to wisdom.” ― Philippe St Genoux', False, 'red', wraplength=800)
        quote_text_rect = quote_text.get_rect(center=(660, 390))
        
        tarot_text = font.render("How to read Tarot Cards:", False, 'red')
        tarot1_text = font.render("Each Tarot card has a representation based on its layout: Upright or Reversed. For example: The Fool represents New Beginnings and Adventure when upright and Recklessnes and Risk when reversed.", False, 'white', wraplength= 800)
        tarot_rect = tarot_text.get_rect(center=((self.SCREEN_X//2 - 220), 500))
        tarot1_rect = tarot1_text.get_rect(center=((self.SCREEN_X//2), 550))      
        
        running = True
        
        while running:
            self.ROOT.fill('black')
            self.ROOT.blit(about_text, about_text_rect)
            self.ROOT.blit(about1_text, about1_rect)
            self.ROOT.blit(quote_text, quote_text_rect)
            self.ROOT.blit(tarot_text, tarot_rect)
            self.ROOT.blit(tarot1_text, tarot1_rect)
            
            home_button = Button(self.ROOT, 'Home', font_A, (self.SCREEN_X/2 + 50), 700)
            more_button = Button(self.ROOT, "More Info", font_A, (self.SCREEN_X/2 - 350), 700)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            if more_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.more_info()

            if home_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.main_menu()
            
            
            pg.display.update()
            
    def more_info(self): #Displays more information on Tarot Cards
        
        font_manager = MyFont(20)
        font = font_manager.font_G()
        font_manager2 = MyFont(24)
        font_A = font_manager2.font_A()
        
        tarot_text = font.render("What is Tarot?", False, 'red')
        tarot1_text = font.render("    Tarot is often viewed as a tool for for telling the future used by witches. That is not true. Tarot cards are used as a tool but to help clear a foggy mind.", False, 'white', wraplength=800)
        tarot2_text = font.render("  Do you need to be a Psychic to give readings?", False, 'red')
        tarot3_text = font.render("     No. It does takes some time to study and practice the cards to fully understand a Tarot deck however.", False, 'white', wraplength=800)
        tarot_rect = tarot_text.get_rect(center=((self.SCREEN_X/2), (self.SCREEN_Y/2 - 300)))
        tarot1_rect = tarot1_text.get_rect(center=((self.SCREEN_X/2), (self.SCREEN_Y/2 - 250)))
        tarot2_rect = tarot2_text.get_rect(center=((self.SCREEN_X/2), (self.SCREEN_Y/2 - 150)))
        tarot3_rect = tarot3_text.get_rect(center=((self.SCREEN_X/2), (self.SCREEN_Y/2 - 100)))
        
        history_text = font.render("The History of Tarot:", False, 'red')
        history1_text = font.render("The earliest evidence of Tarot Cards date back to the 1400's in Italy as a card game. In which each deck had four suites: Cups, Pentagrams, Wands, and Swords. The 'Fool' is thought to be a wild card. As time went on the Major Arcana (the 'Court' cards numbered 0-21) were added. Tarot as a source of divination did not appear until the 18th century according to Wikipedia.", False, 'white', wraplength=800)
        history_rect = history_text.get_rect(center=((self.SCREEN_X/2), (self.SCREEN_Y/2)))
        history1_rect = history1_text.get_rect(center=((self.SCREEN_X/2), (self.SCREEN_Y/2 + 100)))
        
        running = True
        
        while running:
            
            self.ROOT.fill('black')
            self.ROOT.blit(tarot_text, tarot_rect)
            self.ROOT.blit(tarot1_text, tarot1_rect)
            self.ROOT.blit(tarot2_text, tarot2_rect)
            self.ROOT.blit(tarot3_text, tarot3_rect)
            self.ROOT.blit(history_text, history_rect)
            self.ROOT.blit(history1_text, history1_rect)            
            
            back_button = Button(self.ROOT, "Back", font_A, (self.SCREEN_X/2 - 350), 700)
            home_button = Button(self.ROOT, "Home", font_A, (self.SCREEN_X/2 + 50), 700)
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            
            if back_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.tarot_info()
                
            if home_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.main_menu()
            
            pg.display.update()
        
   
    """---------------------------***HOROSCOPE***---------------------------"""   
    def horoscope_screen(self): #AI Generated Horoscope Page
        """Display the daily horoscope on screen"""    
        pg.display.set_caption("Daily Horoscopes")
    
    
        birth_date_info = BirthDate()
        
        font_manager = MyFont(32)
        font_A = font_manager.font_A()
        font_B = font_manager.font_B()
    
    
        #User's Birthdate:
        user_month = birth_date_info.get_selected_month()
        user_day = birth_date_info.get_selected_day()
        user_year = birth_date_info.get_selected_year()
    
        print(f"Your birthday is {user_month}/{user_day}/{user_year}")
    
    
        horo = Horoscope()
        text_sample = horo.horoscope_gen(mon= user_month, day=user_day, year=user_year)
        #print(text_sample)  #Used for testing...
        
        my_text_rect = pg.Rect(200, 100, 1000, 700)
    
        text_rendered = render_textrect(string=text_sample, font=font_B, rect=my_text_rect, text_color='white', background_color='black')
    
        running = True
        while running:
        
            self.ROOT.fill('black')
        
            self.ROOT.blit(text_rendered, my_text_rect)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                
            home_button = Button(self.ROOT, "Home", font_A, 200, 600)
            quit_button = Button(self.ROOT, "QUIT", font_A, 800, 600)
        
            if home_button.get_clicked():
                running = False
                pg.time.delay(300)
                self.main_menu()
            
            if quit_button.get_clicked():
                pg.quit()
        
                
            pg.display.update()
            
    def run(self): #Tells the program to run the title page
        self.title_page()

      
if __name__ == '__main__':
    app = TarotApp()
    app.run()