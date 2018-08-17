import serial
import time
ser = serial.Serial('/dev/rfcomm0', timeout=1, baudrate=10400)
ser.open()
ser.write(b'ATZ\r\n')
time.sleep(1)
print ser.readlines()
