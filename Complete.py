import cv2
import numpy as np
import serial
import time as t
import threading as th 

font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(2)

color_search = np.zeros((200, 200, 3), np.uint8)
color_selected = np.zeros((200, 200, 3), np.uint8)
right_count =0
left_count = 0
hue = 0
flag = False
flag1 = False
flagultimate = False
last_count = 0
last_count1 = 0


def select_color(event, x, y, flags, param):
    global hue

    B = frame[y, x][0]
    G = frame[y, x][1]
    R = frame[y, x][2]
    color_search[:] = (B, G, R)

    if event == cv2.EVENT_LBUTTONDOWN:
        color_selected[:] = (B, G, R)
        hue = hsv[y, x][0]


def search_contours(mask,frames):
    contours_count = 0
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        
        area = cv2.contourArea(contour)
        if 200 < area :
            cv2.drawContours(frames, [contour], -1, (0, 255, 0), 2)
            contours_count += 1
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
            else:
                cX, cY = 0, 0
            cv2.circle(frames, (cX, cY), 3, (255, 255, 255), -1)
            cv2.putText(frames, f"{contours_count}", (cX - 25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),
                        2)

    return contours_count


def nothing(x):
    pass


def secuencia():
    global flagultimate
    send("X")
    send("C")
    flagultimate = False
def desicion(Front, Right):
    
    global flag
    global flag1
    global flagultimate
    if flagultimate != True:
        if Front>=Right:
            if flag != True:
                flag = True
                flag1 = False
                ser.flush()
                send("Y")
                send("A")
            
        else:
            if flag1 != True:
                flag1 = True
                flag = False
                ser.flush()
                send("Z")
                send("B")
                flagultimate = True
                S = th.Timer(1.0, secuencia)  
                S.start()  
            
            
    
        

def main():
    global hsv
    global frame
    global ser
    global right_count
    global left_count
    global last_count
    global last_count1
    while True:
        try:
            ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 1) # ttyACM1 for Arduino board
            break
        except:
            print("CONECTE EL ARDUINO PORFAVOR..........")
            t.sleep(3)
    print("--------INICIANDO PROGRAMA-----------")
    t.sleep(5)
    ser.flush()
    t.sleep(5)

    
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', select_color)

    cv2.namedWindow('Trackbars')
    cv2.resizeWindow('Trackbars', 400, 80)

    cv2.createTrackbar('Lower-Hue', 'Trackbars', 14, 179, nothing)
    cv2.createTrackbar('Upper-Hue', 'Trackbars', 18, 179, nothing)

    cv2.createTrackbar('Ancho', 'Trackbars', 427, 480, nothing)
    cv2.createTrackbar('Alto', 'Trackbars', 297, 640, nothing)
    cv2.createTrackbar('Ancho_c', 'Trackbars', 102, 480, nothing)
    cv2.createTrackbar('Alto_c', 'Trackbars', 143, 640, nothing)
    cv2.createTrackbar('Ancho_1', 'Trackbars', 415, 480, nothing)
    cv2.createTrackbar('Alto_1', 'Trackbars', 341, 640, nothing)
    cv2.createTrackbar('Ancho_c_1', 'Trackbars', 107, 480, nothing)
    cv2.createTrackbar('Alto_c_1', 'Trackbars', 473, 640, nothing)
    while True:

        _, framess = cap.read()
        
        

        diff_lower_hue = cv2.getTrackbarPos('Lower-Hue', 'Trackbars')
        diff_upper_hue = cv2.getTrackbarPos('Upper-Hue', 'Trackbars')
        ancho = cv2.getTrackbarPos('Ancho', 'Trackbars')
        alto = cv2.getTrackbarPos('Alto', 'Trackbars')
        ancho_c = cv2.getTrackbarPos('Ancho_c', 'Trackbars')
        alto_c = cv2.getTrackbarPos('Alto_c', 'Trackbars')
        ancho_1 = cv2.getTrackbarPos('Ancho_1', 'Trackbars')
        alto_1 = cv2.getTrackbarPos('Alto_1', 'Trackbars')
        ancho_c_1 = cv2.getTrackbarPos('Ancho_c_1', 'Trackbars')
        alto_c_1 = cv2.getTrackbarPos('Alto_c_1', 'Trackbars')

        frame = cv2.GaussianBlur(framess[ancho_c:ancho,alto_c:alto],(5,5),0)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        frame_1 = cv2.GaussianBlur(framess[ancho_c_1:ancho_1,alto_1:alto_c_1],(5,5),0)
        hsv_1 = cv2.cvtColor(frame_1, cv2.COLOR_BGR2HSV)

        lower_hue = 0 if hue - diff_lower_hue < 0 else hue - diff_lower_hue
        upper_hue = hue + diff_upper_hue if hue + diff_upper_hue < 179 else 179

        lower_hsv = np.array([lower_hue, 50, 20])
        upper_hsv = np.array([upper_hue, 255, 255])

        mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
        kernel = np.ones((9,9),np.uint8)
        mask = cv2.erode(mask,kernel,iterations = 1)
        mask = cv2.dilate(mask,kernel,iterations = 4)
        mask = cv2.erode(mask,kernel,iterations = 3)
        mask_1 = cv2.inRange(hsv_1, lower_hsv, upper_hsv)
        mask_1 = cv2.erode(mask_1,kernel,iterations = 1)
        mask_1 = cv2.dilate(mask_1,kernel,iterations = 4)
        mask_1 = cv2.erode(mask_1,kernel,iterations = 3)


        count = search_contours(mask,frame)
        count_1 = search_contours(mask_1,frame_1)
        print(right_count)
        if count != last_count:
            right_count = 0
        else:
            right_count += 1
        if count_1 != last_count1:
            left_count = 0
        else:
            left_count += 1
        if right_count >= 40 or left_count >= 40:
            desicion(count,count_1)
            right_count = 0
            left_count = 0
        last_count = count
        last_count1 = count_1






        cv2.putText(frame, f'Total: {count}', (5, 30), font, 1, (255, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(frame_1, f'Total: {count_1}', (5, 30), font, 1, (255, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('mask', mask)
        cv2.imshow('image', frame)
        cv2.imshow('image2', frame_1)
        cv2.imshow('color_search', color_search)
        cv2.imshow('color_selected', color_selected)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()

def send(commandToSend):
    print ("Writing: ",  commandToSend)
    ser.write(str(commandToSend).encode())
    t.sleep(1)
    ser.flush() #flush the buffer

if __name__ == "__main__":
    main()