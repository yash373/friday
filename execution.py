import pyautogui
from speech import Speech
from research import generateText
import time
import pyperclip
import webbrowser

# functions of executer class
# 1. opening applications
# 2. copying to clipboard
# 3. opeing urls
# 4. search youtube tutorials
# 5. search on reddit
# 6. conduct research

class Executer:
    def __init__(self) -> None:
        self.voice = Speech()
    
    def speak(self, text:str) -> None:
        self.voice.speak(text)
    
    def open_application(self, app: str) -> None:
        self.speak(f"Opening {app}")
        pyautogui.hotkey("win","q")
        pyautogui.write(app)
        time.sleep(0.2)
        pyautogui.hotkey("enter")
        pyautogui.hotkey("esc")
        
    def copy_to_clipboard(self, text: str) -> None:
        self.speak("Text was copied to clipboard")
        pyperclip.copy(text)

    def open_url(self ,text:str) -> None:
        self.speak(f"Opening {text}")
        webbrowser.open(text)
    
    def search_youtube(self, query: str) -> None:
        self.speak(f"Opening results on youtube for {query}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    def search_reddit(self, query: str) -> None:
        self.speak(f"Opening results on reddit for {query}")
        webbrowser.open(f"https://www.reddit.com/search/?q={query}")

    def conduct_research(self, query: str) -> None:
        self.speak(f"Conducting research on {query}")
        self.speak(generateText(f"summarize: {query}"))

# e = Executer()
# e.conduct_research("ww1")