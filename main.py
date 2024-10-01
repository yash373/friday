from execution import Executer
from speech import Speech
import re

engine = Executer()
spch = Speech()

keyword = "Arise"

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
        query = spch.listen()
        query = query.lower()

        print(query)