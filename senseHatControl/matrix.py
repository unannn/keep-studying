from sense_hat import SenseHat
from senseHatControl import time_number
from time import sleep
from flow import enum
import database

class SHMatrix:

    def __init__(self):
        self.sh_matrix = SenseHat()
        self.sh_matrix.low_light = True


    def add_study_number(self, m):
        today_study_number = len(database.StudyDataDB().select())

        for i in range(today_study_number):
            m[i] = [0,102,254]

        return m
    
    def print_number(self,minute):       
        
        m = time_number.get_time(minute)
        
        o = [20,200,20]
        x = [0,0,0]
        a = [200,20,200]
        for i in range(len(m)):
            if m[i] == 1:
                if i % 8 < 4:
                    m[i] = o
                else:
                    m[i] = a
            else:
                m[i] = x
        
        m = self.add_study_number(m)
       

        self.sh_matrix.set_pixels(m)
    
    def print_count(self, count):
        self.sh_matrix.show_letter(str(count))
    
    def set_pixel_red(self, x,y):
        self.sh_matrix.set_pixel(x,y,255,0,0)

    def print_next(self):
        x = [0,0,0]
        o = [25,7,137]
        m = [ 
            x,x,x,x,x,x,x,x,
            x,x,x,x,x,x,x,x,
            x,x,x,x,x,x,x,x,
            x,x,x,x,x,x,x,x,
            x,x,x,x,x,x,x,x,
            x,x,x,x,x,x,x,x,
            x,x,x,x,x,x,x,x,
            x,x,x,x,x,x,x,x
        ]

        for i in range(8):
            for j in range(8):
                m[i + j* 8] = o
                if i > 0:
                    m[i + j* 8 - 1] = x
                
                if i < 7:
                    m[i + j* 8 + 1] = o
            self.sh_matrix.set_pixels(m)
            sleep(0.03)
            
    def print_matrix(matrix,state):
        if state == enum.State.TIME_SETTING or state == enum.State.STUDYING:
            print("hi")
        else:
            self.sh_matrix.set_pixels(m)

    def print_complete(self):
        self.sh_matrix.show_message("Study complete!! Congratulation~!~!", text_colour=[255, 0, 0],scroll_speed=0.06)

    def clear_screen(self):
        self.sh_matrix.clear()
        


'''
X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

sense.set_pixels(question_mark)
'''

