import sys
sys.path.append("/home/pi/keep-studying")

from flow import serviceFlow,enum


flow = serviceFlow.ServiceFlow()

#running = True
while True:
    
    state, minute = flow.set_studyTime()    
    if state == enum.State.PROGRAM_END: #왼쪽 조이스틱 누르면 프로그램 종료
        break;


    while state == enum.State.STUDYING:

        state,minute = flow.start_study(minute)

        #공부 완료
        if state == enum.State.STUDY_COMPLETE: 
            flow.complete_study()            
            break
        #공부 정지
        else:
            state = flow.pause_study(state)

            if state == enum.State.STUDY_END:
                break;
            


    
        
    

