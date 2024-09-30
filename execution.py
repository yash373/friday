import pyautogui
from speech import Speech

# raw = "func,val;func,val"

class Executer:
    def __init__(self) -> None:
        pass

    def converter(self, s:str): #returns [[func, val]]
        steps = s.split(";")
        res = []
        for step in steps:
            res.append(step.split(","))
        return res

    def hotkey(self, s:str) -> None:
        chars = s.split("+")
        pyautogui.hotkey(chars)

    def typeWords(self, s:str) -> None:
        pyautogui.write(s,0.1)

    def execute(self, steps, speech: Speech):
        for step in steps:
            if step[0] == "speak":
                speech.speak(step[1])
            elif step[0] == "hkey":
                self.hotkey(step[1])
            elif step[0] == "type":
                self.typeWords(step[1])
            else:
                print("Invalid step")