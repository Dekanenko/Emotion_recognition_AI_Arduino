import serial
import time

# Initialize serial connection
arduino = serial.Serial(port='/dev/tty.usbserial-1120', baudrate=9600, timeout=1) #here, you should define your own port
time.sleep(2)

def send_rgb(red, green, blue):
    if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
        # Send RGB values as bytes
        arduino.write(bytes([red, green, blue]))
    else:
        print("Error: RGB values must be between 0 and 255.")
    time.sleep(1)
