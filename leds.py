#import Pi GPIO and time modules
import RPi.GPIO as GPIO
import time
import urllib.request, json 
 
#set up GPIO numbering and turn off warnings (don't worry if you don't understand this right now)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
#set up which pin to control the LED from and set it to output
ledPinYellow = 40
ledPinBlue = 35
ledPinRed = 36
ledPinWhite = 38
ledPinGreen = 37

GPIO.setup(ledPinYellow, GPIO.OUT)
GPIO.setup(ledPinBlue, GPIO.OUT)
GPIO.setup(ledPinRed, GPIO.OUT)
GPIO.setup(ledPinWhite, GPIO.OUT)
GPIO.setup(ledPinGreen, GPIO.OUT)
data = ""
emotion = ""


while True:
    with urllib.request.urlopen("http://www.physcatch.sk/machinelearning.php") as url:
        data = json.load(url)
        print(data)
        emotion = data[0]["emotion"]



    print(emotion) 



    if(emotion == "Angry"):
        GPIO.output(ledPinRed,GPIO.HIGH)
        GPIO.output(ledPinGreen,GPIO.LOW)
        GPIO.output(ledPinBlue,GPIO.LOW)
        GPIO.output(ledPinYellow,GPIO.LOW)
        GPIO.output(ledPinWhite,GPIO.LOW)
            
    if(emotion == "Neutral"):
        GPIO.output(ledPinWhite,GPIO.HIGH)
        GPIO.output(ledPinGreen,GPIO.LOW)
        GPIO.output(ledPinBlue,GPIO.LOW)
        GPIO.output(ledPinYellow,GPIO.LOW)
        GPIO.output(ledPinRed,GPIO.LOW)
    
            
    if(emotion == "Happy"):
        GPIO.output(ledPinGreen,GPIO.HIGH)
        GPIO.output(ledPinRed,GPIO.LOW)
        GPIO.output(ledPinBlue,GPIO.LOW)
        GPIO.output(ledPinYellow,GPIO.LOW)
        GPIO.output(ledPinWhite,GPIO.LOW)
            
    if(emotion == "Sad"):
        GPIO.output(ledPinBlue,GPIO.HIGH)
        GPIO.output(ledPinGreen,GPIO.LOW)
        GPIO.output(ledPinRed,GPIO.LOW)
        GPIO.output(ledPinYellow,GPIO.LOW)
        GPIO.output(ledPinWhite,GPIO.LOW)

            
    if(emotion == "Fearful"):
        GPIO.output(ledPinYellow,GPIO.HIGH)
        GPIO.output(ledPinGreen,GPIO.LOW)
        GPIO.output(ledPinBlue,GPIO.LOW)
        GPIO.output(ledPinRed,GPIO.LOW)
        GPIO.output(ledPinWhite,GPIO.LOW)
            
    if(emotion == "Surprised"):
        GPIO.output(ledPinGreen,GPIO.HIGH)
        GPIO.output(ledPinBlue,GPIO.HIGH)
        GPIO.output(ledPinYellow,GPIO.HIGH)
        GPIO.output(ledPinRed,GPIO.HIGH)
        GPIO.output(ledPinWhite,GPIO.HIGH)
    
    
