import requests

def generateText(text:str) -> str:
    url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2"

    payload = {
        "messages": [
            {
                "role": "user",
                "content": text
            }
        ],
        "system_prompt": "",
        "temperature": 0.9,
        "top_k": 5,
        "top_p": 0.9,
        "max_tokens": 500,
        "web_access": True
    }
    headers = {
        "x-rapidapi-key": "2010442decmshc62de9e7247e8e1p15b96cjsn1cf015d3184b",
        "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return (response.json()["result"])