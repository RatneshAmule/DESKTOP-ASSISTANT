import speech_recognition as sr
import pyttsx3
import os
import pyautogui
import webbrowser
import time
import wikipedia

# INITIAL SETUP 
engine = pyttsx3.init()
recognizer = sr.Recognizer()

recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True

wikipedia.set_lang("en")

def speak(text):
    if text.strip() == "":
        return
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, phrase_time_limit=5)

        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Internet issue. Please check connection.")
        return ""
    except Exception as e:
        print("Error:", e)
        return ""

def wikipedia_search(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("Your query is too broad. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("No result found on Wikipedia.")
    except Exception:
        speak("Something went wrong while searching Wikipedia.")

def handle_command(cmd):
    if not cmd:
        return

    # Wikipedia Command 
    if cmd.startswith("wiki") or cmd.startswith("wikipedia"):
        speak("Searching Wikipedia.")
        query = cmd.replace("wiki", "").replace("wikipedia", "").strip()
        if query:
            wikipedia_search(query)
        else:
            speak("Please say what you want to search.")
    
    elif "good night" in cmd:
        speak("Okay, good night.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif "goodbye" in cmd or "good bye" in cmd:
        speak("System is shutting down. Bye.")
        os.system("shutdown /s /t 5")

    elif "whatsapp" in cmd:
        speak("Opening WhatsApp.")
        pyautogui.hotkey("win", "4")

    elif "youtube" in cmd:
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")
    elif "instagram" in cmd:
        speak("Opening Insta.")
        webbrowser.open("https://instagram.com")

    elif "browser" in cmd:
        speak("Opening browser.")
        os.system("start msedge")

    elif "downloads" in cmd:
        speak("Opening downloads folder.")
        os.startfile(os.path.expanduser("~/Downloads"))

    elif "close tab" in cmd:
        pyautogui.hotkey("ctrl", "w")

    elif "minimise window" in cmd:
        pyautogui.hotkey("win", "down")

    elif "maximize window" in cmd:
        pyautogui.hotkey("win", "up")

    elif "scroll down" in cmd:
        pyautogui.scroll(-500)

    elif "scroll up" in cmd:
        pyautogui.scroll(500)

    elif "close window" in cmd:
        pyautogui.hotkey("alt", "f4")

    else:
        speak("I did not understand that command.")

# MAIN LOOP 
print("Voice Assistant Started")
speak("Voice assistant is ready.")

while True:
    command = take_command()
    handle_command(command)
    time.sleep(0.4)
