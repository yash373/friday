import pyautogui
from speech import Speech
from research import generateText
import time

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
        pyautogui.hotkey("win","q")
        pyautogui.write(app)
        time.sleep(0.2)
        pyautogui.hotkey("enter")
        
    def copy_to_clipboard(self, text: str) -> None:
        pass

    def open_url(self, text:str) -> None:
        pass
    
    def search_youtube(self, query: str) -> None:
        pass

    def search_reddit(self, query: str) -> None:
        pass

    def conduct_research(self, query: str) -> None:
        pass