from sense_hat import SenseHat
from time import sleep
#from enum import enum
'''
class Joystick_direction(enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 4
    MIDLE = 5
'''

class Joystick:
    
    def __init__(self):
        self.sh_joystick = SenseHat()

    def get_joystick_direction(self):

        first_event = self.sh_joystick.stick.wait_for_event(emptybuffer=True)
        print("1 : The joystick was {} {}".format(first_event.action, first_event.direction))
        # sleep(0.1)
        # second_event = self.sh_joystick.stick.wait_for_event(emptybuffer=True)
        # print("2 : The joystick was {} {}".format(second_event.action, second_event.direction))

        if (first_event.action == "pressed"):
            return first_event.direction
        
        if first_event.action == "held":
            return first_event.direction

        return None
    def get_current_events(self):

        return self.sh_joystick.stick.get_events()
    