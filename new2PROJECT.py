import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import random

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("papilia", text)
    engine.say(text)
    engine.runAndWait()

engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def tell_joke():
    jokes = [
        "Why don’t programmers like nature? It has too many bugs.",
        "I told my computer I needed a break... and it said 'No problem, I’ll crash for you!'",
        "Why did the Python developer go broke? Because he couldn’t c!"
    ]
    return random.choice(jokes)

def comfort_user():
    messages = [
        "I’m here for you. Take a deep breath, you’ve done so much already 💜",
        "Even butterflies need to rest their wings. You deserve a break 🦋",
        "Let me play something soothing or tell you a joke to lift your mood."
    ]
    return random.choice(messages)

def handle_command(command):
    if "search" in command:
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif "joke" in command:
        joke = tell_joke()
        speak(joke)
    elif "tired" in command or "exhausted" in command or "low" in command:
        message = comfort_user()
        speak(message)
        webbrowser.open("https://www.youtube.com/watch?v=2OEL4P1Rz04")
    elif "exit" in command or "bye" in command:
        speak("Goodbye! Have a great day!")
        return False
    elif command:
        speak(f"You said: {command}")
    return True

speak("Hello! What's your name?")
name = listen()
if name:
    speak(f"Nice to meet you, {name}!")

speak("How can I help you today? Say 'exit' to quit.")

conversation = []
while True:
    command = listen()
    conversation.append(f"You: {command}")
    if not handle_command(command):
        break

with open("conversation.txt", "w") as f:
    for line in conversation:
        f.write(line + "\n")
