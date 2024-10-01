from execution import Executer
from speech import Speech

engine = Executer()
spch = Speech()

keyword = "Arise"

if __name__ == '__main__':
    while True:
        spch.listen_for_word(keyword)
        query = spch.listen()
        query = query.lower()

        print(query)