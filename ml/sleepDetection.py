import dlib
import numpy
import cv2

from picamera import PiCamera
from time import sleep
import time
import math
import os 

from flow import enum

class SleepDetection:
    
    def __init__(self):
        print("init")
        self.image_number = 0    
        self.detector = dlib.get_frontal_face_detector()
        print(os.path.dirname(os.path.realpath(__file__)))
        self.predictor = dlib.shape_predictor(f"{os.path.dirname(os.path.realpath(__file__))}/shape_predictor_68_face_landmarks.dat")
        self.current_eye_state = []
        self.user_absence_count = 0 

    def is_sleepiness_or_absense(self):

        print("is_sleepiness_or_absense 들어몸")
        self.capture_image()
        print("사진찍음")
        current_eye_landmark = self.get_eye_landmark()
        print("랜드마크 얻음")
        
        #자리비움 감지(10회 검사에도 얼굴인식 안될 경우 부재라고 판단)
        if len(current_eye_landmark) == 0:
            
            self.user_absence_count += 1  

            if self.user_absence_count > 10:
                print("자리비움")
                self.current_eye_state.clear()
                return enum.State.STUDY_STOPED_ABSENSE          
            
            print("아직공부중")

            return enum.State.STUDYING
      

        if self.get_EAR(current_eye_landmark) < 0.21: #눈감을 때 마다 스택에 추가
            self.current_eye_state.insert(0,True)
        else:
            self.current_eye_state.insert(0,False)


        if len(self.current_eye_state) > 7:
            self.current_eye_state.pop()
            
            #졸음감지
            if self.count_eye_state() > 5:
                self.current_eye_state.clear()
                return enum.State.STUDY_STOPED_SLEEPINESS

        return enum.State.STUDYING


    def capture_image(self):
                
        camera = PiCamera()

        camera.resolution = (512,512)
        camera.start_preview()
        #sleep(3)
        #camera.rotation = 180

        camera.capture(f'{os.getcwd()}/image/detection_image.jpg')
                

        if self.image_number > 6:
            self.image_number = 0

        camera.stop_preview()
        camera.close()
    
    def get_eye_landmark(self):
        
        photo = cv2.imread(f'{os.getcwd()}/image/detection_image.jpg')
        detect = self.detector(photo,1)
        print("detect:",detect)
        print("detect-length:",len(detect))

        if len(detect) == 0:#사람없음
            return []

        shape = self.predictor(photo,detect[0])

        self.image_number += 1

        landmark_location = []

        landmark_location.append(shape.part(36))
        landmark_location.append(shape.part(37))
        landmark_location.append(shape.part(38))
        landmark_location.append(shape.part(39))
        landmark_location.append(shape.part(40))
        landmark_location.append(shape.part(41))

        return landmark_location
    
    def get_EAR(self, eye_landmark):
        
        # if len(self.current_eye_state) > 5:
        #     self.current_eye_state.pop()
        A = self.get_distance(eye_landmark[1],eye_landmark[5])
        B = self.get_distance(eye_landmark[2],eye_landmark[4])
        C = self.get_distance(eye_landmark[0],eye_landmark[3])

        ear = (A+B) / (2.0 * C)

        print("EAR : ", ear)
        return ear
        
    
    def count_eye_state(self):

        count = 0

        for i in range(len(self.current_eye_state)):
            if self.current_eye_state[i] == True:
                count += 1
        
        return count
    
    def get_distance(self, dot1, dot2):
        
        dx = dot1.x - dot2.x
        dy = dot1.y - dot2.y
        
        return math.sqrt(dx**2 + dy**2)


# sleep_detection = SleepDetection()

# for i in range(30):

    
#     start = time.time()
#     detect = sleep_detection.is_sleepiness()
    
#     print(f"{i}번째 속도: {time.time()-start}")
#     print("list : ", sleep_detection.current_eye_state)
#     print(f"졸고 있니? : {detect}" )