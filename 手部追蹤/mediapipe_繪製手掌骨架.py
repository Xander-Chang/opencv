import cv2, time
import mediapipe as mp


precious_time = 0


mp_hands = mp.solutions.hands
Hands = mp_hands.Hands()

mp_draw = mp.solutions.drawing_utils
hand_mark_style = mp_draw.DrawingSpec(color=(255,0,0),thickness=3)
hand_line_style = mp_draw.DrawingSpec(color=(0,0,255),thickness=3)



cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("camera isn't opened")
    
while True:
    ret, img = cap.read()
    if ret:
        # 1. 將BGR轉成RBG,偵測手
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = Hands.process(img_rgb)
        
        # 影像視窗大小
        print('影像視窗大小', img.shape)
        img = cv2.resize(img,(640,480))
        y_height = img.shape[0]               # 也可以 cap.resize()
        x_width = img.shape[1]
        
        hand_landmarks = result.multi_hand_landmarks
        if hand_landmarks:
            for hand_landmark in hand_landmarks:
                # 2. 畫點、畫連接線
                mp_draw.draw_landmarks(img,
                                       hand_landmark,
                                       mp_hands.HAND_CONNECTIONS,
                                       hand_mark_style,
                                       hand_line_style)
                # 3. 找點位置
                for i, Land_Mark in enumerate(hand_landmark.landmark):
                    x_position = int(Land_Mark.x * x_width)
                    y_position = int(Land_Mark.y * y_height)
                    print(i, '\t點的座標:',[x_position, y_position], Land_Mark.z)
                    
                    # 4. 寫上節點數字
                    cv2.putText(img,str(i),(x_position -30, y_position +5),
                                cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,255,0),2)
                    # 5. 在某節點 畫圈
                    if i == 9:
                        cv2.circle(img, (x_position, y_position), 60,(20,120,180), 
                                   cv2.FILLED)
        
        # 6. FPS 每偵幾秒
        current_time = time.time()
        fps = int(1/(current_time - precious_time))
        precious_time = time.time()
        cv2.putText(img,f'FPS:{fps}',(30, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
        
        
        cv2.imshow('img',img)
        print('播放中')
    
    
    else:
        print("finish")
        break
        
    if cv2.waitKey(90) == ord('q') or cv2.waitKey(90) == 27:
        print('中止')
        break
        