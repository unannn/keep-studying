from enum import Enum

class State(Enum):
    
    TIME_SETTING = 1
    STUDYING = 2
    STUDY_READY = 3
    
    STUDY_STOPED_MOVEMENT = 4
    STUDY_STOPED_SLEEPINESS = 5
    STUDY_STOPED_ABSENSE = 6
    STUDY_STOPED_USER = 7
    
    STUDY_COMPLETE = 8

    STUDY_END = 9
    PROGRAM_END = 10
