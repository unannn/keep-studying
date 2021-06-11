import time
from time import sleep

from senseHatControl import acceleration,matrix,joystick

import database
from ml import sleepDetection
from flow import enum

class ServiceFlow:
    
    def __init__(self):
        
        self.sh_matrix = matrix.SHMatrix()
        self.sh_joystick = joystick.Joystick()
        self.sh_acceleration = acceleration.Acceleration()
        self.sleep_detection = sleepDetection.SleepDetection()

        self.cycle = 2 #차감 시간 (원래 60초)

    def set_studyTime(self):      
        
        error = None
        minute = 1
        self.sh_matrix.print_number(minute)
        while True:

            direction = self.sh_joystick.get_joystick_direction()

            if direction is None:
                #error = "direction is NONE!!"
                #return error
                print("direction is NONE!!")
            else:
                if direction == "down":
                    minute -= 1                    
                    minute = self.check_time_availability(minute)
                    #self.sh_matrix.print_next()
                    self.sh_matrix.print_number(minute)
                
                elif direction == "up":
                    minute += 1
                    minute = self.check_time_availability(minute)
                    #self.sh_matrix.print_next()
                    self.sh_matrix.print_number(minute)
                
                elif direction == "middle":
                    self.sh_matrix.print_next()
                    
                    return enum.State.STUDYING,minute
                elif direction == "left":
                    return enum.State.PROGRAM_END,minute

    def start_study(self, minute):

        for count in reversed(range(1,4)):
            #self.sh_matrix.print_number(count)
            self.sh_matrix.print_count(count)
            print(minute)
            time.sleep(1)

        self.sh_matrix.print_next()
        
        while minute > 0:
            
            self.sh_matrix.print_number(minute)
            start_time = time.time()

            elapsed_time = time.time() - start_time
            ten_second_count = 0
            
            while elapsed_time < self.cycle:
                
                print("시간 : %s" %elapsed_time)
                
                sleep(1)
                elapsed_time = time.time() - start_time
                
                joystick_direction = None
                joystick_events = self.sh_joystick.get_current_events()
                if len(joystick_events) > 0:
                    joystick_direction = joystick_events[0].direction
                
                print("조이스틱")
                #조이스틱 감지
                if joystick_direction == "up":                    
                    return enum.State.STUDY_STOPED_USER, minute
                
                print("기기움직임")

                #기기움직임 감지
                if self.sh_acceleration.is_moved():
                    return enum.State.STUDY_STOPED_MOVEMENT, minute

                print("집중력저하")
                #집중력 저하 감지
                detect = self.sleep_detection.is_sleepiness_or_absense()
                if detect != enum.State.STUDYING:
                    print(detect,min)
                    return detect, minute
                
                print("단위초메트릭스")

                if int(elapsed_time / (self.cycle/ 8) )  > ten_second_count:
                    self.sh_matrix.set_pixel_red(7 - ten_second_count,0)
                    ten_second_count += 1
               

            minute -= 1

        return enum.State.STUDY_COMPLETE, minute

    def complete_study(self):
        #축하 화면출력
        self.sh_matrix.print_complete()
        #오늘 공부시간 추가
        database.StudyDataDB().insert(1)

    def pause_study(self,puase_case):
        # 정지사유에 출력
        
        if puase_case == enum.State.STUDY_STOPED_MOVEMENT:
            print("움직였음")
        elif puase_case ==  enum.State.STUDY_STOPED_ABSENSE:
            print("부재로인한 정지")
        elif pause_case ==  enum.State.STUDY_STOPED_SLEEPINESS:
            print("졸음으로 인한 정지")
        else:
            print("임의정지")

        sleep(1)

        #공부 정지, 재시작 선택 출력과 기다리기
        print("재시작이면 ↑, 종료면 ←")
        while True:

            direction = self.sh_joystick.get_joystick_direction()
            
            if direction == "up":
                return enum.State.STUDYING 
            elif direction == "left":
                return enum.State.STUDY_END
            

    def print_count(self,second):
        acceleration.example()
    
    def check_time_availability(self, minute):
        if minute > 0 and minute <= 99:
            return minute

        if minute < 1:
            return 1

        if minute > 99:
            return 99         


    def __del__(self):
        self.sh_matrix.clear_screen()
        