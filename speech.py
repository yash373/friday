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
                text = self.r.recognize_google(audio)
                text = text.lower()
                return text
            except sr.RequestError as e:
                print(f"Could not request results: {e}")
            except sr.UnknownValueError as e:
                print(f"Could not get value: {e}")
    
    def listen_for_word(self ,word):
        with sr.Microphone() as source:
            print("Listening for the word...")
            self.r.adjust_for_ambient_noise(source)  # Adjust for background noise
            
            while True:
                try:
                    # Capture the audio
                    audio = self.r.listen(source)
                    # Convert speech to text
                    text = self.r.recognize_google(audio).lower()
                    print(f"Recognized: {text}")
                    
                    # Check if the word is in the recognized text
                    if word.lower() in text:
                        print(f"The word '{word}' was said!")
                        break
                    
                except sr.UnknownValueError:
                    # If the speech is unintelligible
                    print("Could not understand audio")
                except sr.RequestError as e:
                    # If there's an issue with the recognition service
                    print(f"Recognition error: {e}")

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()    