import serial
import time as t

while True:
    try:
        ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 1) # ttyACM1 for Arduino board
        break
    except:
        print("CONECTE EL ARDUINO PORFAVOR..........")
        t.sleep(3)

def send(commandToSend):
    print ("Writing: ",  commandToSend)
    ser.write(str(commandToSend).encode())
    t.sleep(1)
    ser.flush() #flush the buffer

print ("Starting up") # get the distatnce in mm
t.sleep(5)
ser.flush()
t.sleep(5)

send("A")
t.sleep(1)
send("Z")
t.sleep(1)
send("B")
t.sleep(1)
send("X")
t.sleep(1)
send("C")
t.sleep(1)
send("Y")
