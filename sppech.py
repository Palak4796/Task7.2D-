import speech_recognition as sr
from gpiozero import LED
from time import sleep

led = LED(17)

def recognize_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("say 'ON' or 'OFF'...")
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio).lower()
            
while True:
    command = recognize_speech()
    
    if command:
        if "on" in command:
            led.on()
            print("LED is Glowing")
        elif "off" in command:
            led.off()
            print("LED is Not Glowing")
    
    sleep(1)
