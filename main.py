import speech_recognition as sr
import pyttsx3 

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source)

def SpeakText(command):
    
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

while(1):    
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
             
            audio = r.listen(source)
            
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()

            print(f"Did you say ,{MyText}")
            SpeakText(f"Did you say ,{MyText}")
            
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
        
    except sr.UnknownValueError as e:
        print(f"Could not get value: {e}")