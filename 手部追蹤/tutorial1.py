import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mp_Draw = mp.solutions.drawing_utils




while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('frame', frame)
        print('播放中')
        
        frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        result_p = hands.process(frame_RGB)
        hand_Landmarks =  result_p.multi_hand_landmarks
        print(hand_Landmarks)
        
        if hand_Landmarks:
            for hand_landmark in hand_Landmarks:
                mp_Draw.draw_landmarks(frame, hand_landmark, mpHands.HAND_CONNECTIONS)          # draw_landmarks(圖片, 點座標, 連接點)
                
        
        
    else:
        print('break / finish')
        break
    
    if cv2.waitKey(90) == ord('q') or cv2.waitKey(90) == 27:
        print('中止')
        break
    
    
    
    