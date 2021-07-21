import smtplib

import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia  # pip install wikipedia
import smtpd
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty("voices")

# this is for change the assistant voice 0 for male 1 for female
engine.setProperty("voice", voices[1].id)

# this change the speed of assistant
# newVoiceRate = 190
engine.setProperty("rate", 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# it show corrent time
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


# time()

# it speak current date
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)

    speak("the current date is ")
    speak(date)
    speak(month)
    speak(year)


# date()


# wish me how can i help you
def wishme():
    speak("welcome back aparna !")

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good morning ")
    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    elif hour >= 18 and hour <= 24:
        speak("good evening ")
    else:
        speak("Good night")

    speak("sera at your service . How can I help you ?")


# wishme()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        # it will wait for a 1 second
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogninzing...")
        query = r.recognize_google(audio, language='en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please ...")
        return "None"
    return query


# takeCommand()

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("aparna.likhitkar@gmail.com", "password ")
    server.sendmail("aparna.likhitkar@gmail.com", to), content
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\Pthon program\screenshot\ss.png")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)

    battery = psutil.sensors_battery
    speak("bettery is at ")
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_jokes())


if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()
        print(query)
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        elif "send email" in query:
            try:
                speak("what should i say ?")
                content = takeCommand()
                to = "aparna.likhitkar@gmail.com"
                sendmail(to, content)
                speak("Email sent successfully ")
            except Exception as e:
                speak(e)
                speak("Unable to send the message ")

        elif "search in chrome " in query:
            speak("what should I search ?")
            chromepath = "C:/Users\aparn\AppData\Local\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "logout" in query:
            os.system("Shutdown -1 ")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1 ")

        elif "restart" in query:
            os.system("shutdown /r /t 1 ")

        elif "play songs" in query:
            songs_dir = "C:/Users/aparn/OneDrive/Effortless English"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif "remember that " in query:
            speak("what should i remember ?")
            data = takeCommand()
            speak("you said me to remember " + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "do you know anything " in query:
            remember = open("data.txt", "w")
            speak("you said me to remember that " + remember.read())
        elif "screenshot " in query:
            screenshot()
            speak("done!")

        elif "cpu " in query:
            cpu()

        elif "joke" in query:
            jokes()
