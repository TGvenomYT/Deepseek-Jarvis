import requests
import speech_recognition as sr
import pyttsx3
import os

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
Authorization=os.getenv('Authorization')

# List available voices
voices = engine.getProperty('voices')
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name}")

# Set the desired voice (e.g., the second voice in the list)
if len(voices) > 29:
    engine.setProperty('voice', voices[27].id)
else:
    print("Voice index 29 is out of range. Using default voice.")
    

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and convert it to text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None

# Function to interact with DeepSeek API
def deepseek_query(query):
    api_url = "https://api.deepseek.com/query"
    headers = {
        "Authorization": "API_KEY",
        "Content-Type": "application/json"
    }
    data = {
        "query": query
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get("response")
    else:
        return "Sorry, I couldn't process your request."

# Main function to run the assistant
def main():
    speak("Hello, I am Jarvis. How can I assist you ?")

    while True:
        query = listen()
        if query:
            response = deepseek_query(query)
            speak(response)

if __name__ == "__main__":
    main()
