# Welcome To The Bad Translator!
# This script uses the terminal to run your text through google translate 10 times until its badly translated.
# Made by: Jyomama28 or Jyoeymama on github!

import requests
import time
import random

def translate(text, src, dest):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": src,
        "tl": dest,
        "dt": "t",
        "q": text
    }
    response = requests.get(url, params=params)
    result = response.json()
    return result[0][0][0]

def bad_translate(text, rounds=10):
    languages = ['fr', 'de', 'it', 'es', 'ru', 'zh-CN', 'ja', 'ar', 'hi', 'pt']
    current_text = text
    src = 'en'
    for i in range(rounds):
        dest = random.choice(languages)  
        current_text = translate(current_text, src, dest)
        print(f"Round {i+1}: {src} → {dest} → {current_text}")  
        time.sleep(0.5) 
        src = dest

    final_text = translate(current_text, src, 'en')
    return final_text

if __name__ == "__main__":
    while True:
        user_input = input("Enter text to badly translate (or type 'exit' to quit): ")
        if user_input.strip().lower() == 'exit':
            print("Exiting Bad Translator. Goodbye!")
            break
        result = bad_translate(user_input, rounds=10)
        print("\nFinal badly translated text:", result)
        print("Bad Translation Complete!\n")