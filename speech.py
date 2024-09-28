import speech_recognition as sr
import pyttsx3

class Speech:
    def __init__(self):
        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()
    
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")

            try:
                self.r.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.r.listen(source)
                MyText = self.r.recognize_google(audio)
                text = text.lower()
            except sr.RequestError as e:
                print(f"Could not request results: {e}")
            except sr.UnknownValueError as e:
                print(f"Could not get value: {e}")

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()    