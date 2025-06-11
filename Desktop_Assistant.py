import speech_recognition as sr
import pyttsx3
import os
import pyautogui
import webbrowser
import time

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        speak("Voice recognition service is not available.")
        return None


def handle_command(cmd):
    if "good night" in cmd:
        speak("okay, Byee")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif "goodbye" in cmd or "good bye" in cmd:
        speak("See you later")
        os.system("shutdown /s /t 5")
    elif "whatsapp" in cmd:
        speak("Opening WhatsApp.")
        pyautogui.hotkey("win", "4")
    elif "youtube" in cmd:
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")
        time.sleep(5)
    elif "history" in cmd:
                pyautogui.click(x=75, y=369)
    elif "home" in cmd:
                pyautogui.click(x=79, y=182)
    elif "search" in cmd:
                pyautogui.click(x=1264, y=122)
        # Voice search click can be added here later
    elif "browser" in cmd:
        speak("Opening Edge.")
        os.system("start msedge")
    elif "downloads" in cmd:
        speak("Opening Downloads ")
        downloads = os.path.expanduser("~/Downloads")
        os.startfile(downloads)
    elif "close this tab" in cmd:
        speak("okay")
        pyautogui.hotkey("ctrl", "w")
    elif "minimise window" in cmd:
        speak("Sure")
        pyautogui.hotkey("win", "down")
    elif "maximize window" in cmd:
        speak("Okay")
        pyautogui.hotkey("win", "up")
    elif "scroll down" in cmd:
        pyautogui.hotkey("down")
    elif "scroll up" in cmd:
        pyautogui.hotkey("up")
        
    elif "close this window" in cmd or "close window" in cmd:
        speak("Closing")
        pyautogui.hotkey("alt", "f4")
    else:
        speak(" ")

# Main loop with failed attempt control
fail_count = 0
MAX_FAILS = 3

# Main loop — silent on failed recognition
while True:
    command = take_command()
    if command:
        handle_command(command)
    # else: do nothing (stay quiet)

    else:
        fail_count += 1
        if fail_count == MAX_FAILS:
            speak(" ")
            fail_count = 0  # reset after speaking once
