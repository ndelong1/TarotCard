"""horoscope.py
Using openai API generates a dailyu horoscope for the user based on their birthday."""

import os
import openai
import datetime as dt
import pygame as pg
from dotenv import load_dotenv

load_dotenv()

my_id = os.getenv("API_Key")

openai.api_key = my_id

class Horoscope:
    def __init__(self):
        self.today_date = dt.date.today()
        pg.init()

    def horoscope_gen(self, mon, day, year):
        self.user_birthday = f"{mon}/{day}/{year}"    
        prompt = (f"Generate a daily horoscope for the user. Follow these rules: 1. Use {self.user_birthday} for the user's zodiac sign. 2. KEEP IT SHORT. 3. Do Not say 'User'. 4. Today's date is {self.today_date}")
        
        response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=200,
        )
        return response.choices[0].text
    
def render_textrect(string, font, rect, text_color, background_color, justification=0):
    ##### NOT MY OWN FUNCTION!! found at: <<https://www.pygame.org/pcr/text_rect/index.php>>
    ##### Author: David Clark
    
    final_lines = []

    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided
    # rectangle.

    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # Start a new line
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.    
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line
                else:
                    final_lines.append(accumulated_line)
                    accumulated_line = word + " "
            final_lines.append(accumulated_line)
        else:
            final_lines.append(requested_line)

    # Let's try to write the text out on the surface.

    surface = pg.Surface(rect.size)
    surface.fill(background_color)

    accumulated_height = 0
    for line in final_lines:
        # if accumulated_height + font.size(line)[1] >= rect.height:
            # raise TextRectException, "Once word-wrapped, the text string was too tall to fit in the rect."
        if line != "":
            tempsurface = font.render(line, 1, text_color)
            if justification == 0:
                surface.blit(tempsurface, (0, accumulated_height))
            elif justification == 1:
                surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
            elif justification == 2:
                surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
            # else:
                # raise TextRectException, "Invalid justification argument: " + str(justification)
        accumulated_height += font.size(line)[1]

    return surface


if __name__ == '__main__':
    my_app = Horoscope()
    print(my_app.horoscope_gen())

