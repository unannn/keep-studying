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
    
    def print_continue_guide(self):
        
        x = (0,0,0)
        a = (250,0,40)
        l = (40,250,0)
        
        m = [ 
            x,x,a,x,x,x,x,x,
            x,a,a,a,x,x,x,x,
            a,x,a,x,a,x,x,x,
            x,x,a,l,x,l,l,x,
            x,x,a,l,l,x,x,l,
            x,x,a,l,x,x,x,x,
            x,x,a,l,x,x,x,x,
            x,x,a,l,x,x,x,x
        ]
        
        self.sh_matrix.set_pixels(m)
       
    
    def print_end_guide(self):
             
        x = (0,0,0)
        a = (250,0,40)
        l = (40,250,0)
    
        m = [ 
            x,x,a,x,x,x,x,x,
            x,a,x,x,x,x,x,x,
            a,a,a,a,a,a,a,a,
            x,a,x,x,l,l,l,x,
            x,x,a,l,x,x,x,l,
            x,x,x,l,l,l,l,l,
            x,x,x,l,x,x,x,x,
            x,x,x,x,l,l,l,l
        ]
        
        self.sh_matrix.set_pixels(m)

    def print_matrix(matrix,state):
        if state == enum.State.TIME_SETTING or state == enum.State.STUDYING:
            print("hi")
        else:
            self.sh_matrix.set_pixels(m)

    def print_complete(self):
        self.sh_matrix.show_message("Study complete!! Congratulation~!~!", text_colour=[255, 0, 0],scroll_speed=0.06)

    def clear_screen(self):
        self.sh_matrix.clear()
    
    
    def print_moved(self):
        
        x = (0,0,0)

        l = (255,255,0)
        r = (250,0,40)
        b = (40,250,0)

        m = [       
                [ 
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    x,l,l,x,l,x,x,x,
                    x,l,x,l,x,l,x,x,
                    x,l,x,l,x,l,x,x,
                    x,l,x,l,x,l,x,x,
                    x,l,x,l,x,l,x,x
                ],
                [ 
                    b,b,b,b,b,b,b,b,
                    b,b,b,b,b,b,b,b,
                    b,b,b,b,b,b,b,b,
                    x,x,l,l,l,x,x,x,
                    x,l,x,x,x,l,x,x,
                    x,l,x,x,x,l,x,x,
                    x,l,x,x,x,l,x,x,
                    x,x,l,l,l,x,x,x
                ],
                [ 
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    x,l,x,x,x,l,x,x,
                    x,l,x,x,x,l,x,x,
                    x,x,l,x,l,x,x,x,
                    x,x,l,x,l,x,x,x,
                    x,x,l,l,x,x,x,x
                ],
                [ 
                    b,b,b,b,b,b,b,b,
                    b,b,b,b,b,b,b,b,
                    b,b,b,b,b,b,b,b,
                    x,x,l,l,l,x,x,x,
                    x,l,x,x,x,l,x,x,
                    x,l,l,l,l,l,x,x,
                    x,l,x,x,x,x,x,x,
                    x,x,l,l,l,l,x,x
                ],
                [ 
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    x,x,x,x,x,l,x,x,
                    x,x,x,x,x,l,x,x,
                    x,l,l,l,l,l,x,x,
                    x,l,x,x,x,l,x,x,
                    x,l,l,l,l,l,x,x
                ]
        ]

        for i in range(5):
            self.sh_matrix.set_pixels(m[i])
            sleep(1)
            
    def print_absence(self):
        x = (0,0,0)

        l = (255,255,0)
        r = (250,0,40)
        b = (40,250,0)

        m = [       
                [ 
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    x,x,l,l,x,l,x,x,
                    x,l,x,x,l,l,x,x,
                    x,l,x,x,l,l,x,x,
                    x,l,x,x,l,l,x,x,
                    x,x,l,l,x,l,x,x
                ],
                [ 
                    b,b,b,b,b,b,b,b,
                    b,b,b,b,b,b,b,b,
                    b,b,b,b,b,b,b,b,
                    x,l,x,x,x,x,x,x,
                    x,l,x,x,x,x,x,x,
                    x,l,l,l,l,l,x,x,
                    x,l,x,x,x,l,x,x,
                    x,l,l,l,l,l,x,x
                ],
                [ 
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    x,l,l,l,l,l,x,x,
                    x,l,x,x,x,x,x,x,
                    x,l,l,l,l,l,x,x,
                    x,x,x,x,x,l,x,x,
                    x,l,l,l,l,l,x,x
                ],
                [ 
                    b,b,b,b,b,b,b,b,
                    b,b,b,b,b,b,b,b,
                    b,b,b,b,b,b,b,b,
                    x,x,l,l,l,x,x,x,
                    x,l,x,x,x,l,x,x,
                    x,l,l,l,l,l,x,x,
                    x,l,x,x,x,x,x,x,
                    x,x,l,l,l,l,x,x
                ],
                [ 
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    x,l,l,l,l,x,x,x,
                    x,l,x,x,x,l,x,x,
                    x,l,x,x,x,l,x,x,
                    x,l,x,x,x,l,x,x,
                    x,l,x,x,x,l,x,x
                ],
                [ 
                    b,b,b,b,b,b,b,b,
                    b,b,b,b,b,b,b,b,
                    b,b,b,b,b,b,b,b,
                    x,x,l,l,l,x,x,x,
                    x,l,x,x,x,l,x,x,
                    x,l,x,x,x,x,x,x,
                    x,l,x,x,x,l,x,x,
                    x,x,l,l,l,x,x,x
                ],
                [ 
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    x,x,l,l,l,x,x,x,
                    x,l,x,x,x,l,x,x,
                    x,l,l,l,l,l,x,x,
                    x,l,x,x,x,x,x,x,
                    x,x,l,l,l,l,x,x
                ]
        ]

        for i in range(7):
            self.sh_matrix.set_pixels(m[i])
            sleep(1)

    
    def print_sleep(self):

        x = (0,0,0)

        l = (255,255,0)
        r = (250,0,40)
        b = (40,250,0)
        
        m = [
                [ 
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    x,l,l,l,l,l,x,x,
                    x,l,x,x,x,x,x,x,
                    x,l,l,l,l,l,x,x,
                    x,x,x,x,x,l,x,x,
                    x,l,l,l,l,l,x,x
                ],
                [ 
                    b,b,b,b,b,b,b,b,
                    b,b,b,b,b,b,b,b,
                    b,b,b,b,b,b,b,b,
                    x,x,l,x,x,x,x,x,
                    x,x,l,x,x,x,x,x,
                    x,x,l,x,x,x,x,x,
                    x,x,l,x,x,x,x,x,
                    x,x,l,x,x,x,x,x
                ],
                [ 
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    x,x,l,l,l,x,x,x,
                    x,l,x,x,x,l,x,x,
                    x,l,l,l,l,l,x,x,
                    x,l,x,x,x,x,x,x,
                    x,x,l,l,l,l,x,x
                ],
                [ 
                    b,b,b,b,b,b,b,b,
                    b,b,b,b,b,b,b,b,
                    b,b,b,b,b,b,b,b,
                    x,x,l,l,l,x,x,x,
                    x,l,x,x,x,l,x,x,
                    x,l,l,l,l,l,x,x,
                    x,l,x,x,x,x,x,x,
                    x,x,l,l,l,l,x,x
                ],
                [ 
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    r,r,r,r,r,r,r,r,
                    x,l,l,l,l,l,x,x,
                    x,l,x,x,x,l,x,x,
                    x,l,l,l,l,l,x,x,
                    x,l,x,x,x,x,x,x,
                    x,l,x,x,x,x,x,x
                ]
        ]

        for i in range(5):
            self.sh_matrix.set_pixels(m[i])
            sleep(1)

