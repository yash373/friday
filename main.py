from execution import Executer
from speech import Speech
import re

engine = Executer()
spch = Speech()

keyword = "friday"

def extract_link(text: str) -> str:
    # Regular expression to match URLs with or without http/https
    url_pattern = r'((https?://)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}(/[^\s]*)?)'
    
    # Find all links in the string
    links = re.findall(url_pattern, text)
    
    if links:
        # Extract just the actual URL from the tuple returned by findall
        return links[0][0]  # Return the first valid link found
    else:
        return False  # Return None if no link is found

if __name__ == '__main__':
    while True:
        spch.listen_for_word(keyword)
        while True:
            spch.speak("How can I serve you, master?")
            query = spch.listen()

            if "exit" == query:
                spch.speak("Exiting...")
                break
            elif "conduct research" in query:
                # print("will conduct research")
                engine.conduct_research(query)
                break
            elif "search youtube" in query or "youtube tutorials" in query:
                engine.search_youtube(query)
            else:
                spch.speak("I couldn't get you")