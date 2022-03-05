import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
import pyautogui
import psutil
import cv2
import random
from requests import get
import pywhatkit as pwt
import wikipedia
import smtplib

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)


def wishMe():
    speak("Welcome Back Sir...!")

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    elif hour >= 18 and hour < 22:
        speak("Good Evening!")
    else:
        speak("Good Night!")

    speak("Alex 2.O,At your Service. How can I help you \...?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio)
        print("You said: {}".format(query))
    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"

    return query


def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\Projects\SY SDP\\ss.png")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery = psutil.sensors_battery
    speak("Battery is at " + battery)

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aniruddhamanoharjoshi@gmail.com', 'Password here')
    server.sendmail('aniruddhamanoharjoshi@gmail.com', to, content)
    server.close()


# def jokes():

#     print(pyjokes.get_jokes())
#     speak(pyjokes.get_jokes())


if __name__ == "__main__":
    wishMe()

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
                speak("searching wikipedia....")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
            #wb.open("wikipedia.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            wb.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            wb.open("stackoverflow.com")

        #elif "search in chrome" in query:
            #speak("What should i search ?")
            ##wb.register('chrome', None, wb.BackgroundBrowser(chromepath))
            #search = takeCommand().lower()
            #wb.get('chrome').open_new_tab("https:\\www."+search+".com")
        elif "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "remember that" in query:
            speak("What sould I Remember?")
            query = takeCommand()
            speak("you said me to remember" + query)
            remember = open("query.txt", "w")
            remember.write(query)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("query.txt", "r")
            speak("you said me to remember that" + remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("Done")
        elif "cpu" in query:
            cpu()

            break
        elif "tell me a joke" in query:
            jokes = open("joke.txt", "r")
            speak(jokes.read())
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        
        elif "open notepad" in query:
            npath = 'C:\\Windows\\system32\\notepad.exe'
            os.startfile(npath)
            speak("Done")

        elif "open command prompt" in query:
            os.system("start cmd")
            speak("Done")
        
        elif "tell me about yourself" in query:
            speak(" my name is alex. I am developed by aniruddha joshi in his second year of engineering in the year 2021. professor deepali deshpande guided him")
        elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(1)
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows()
                speak("Have a look. I opened Webcam")
        
        elif "play music" in query:
            music_dir = "E:\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        
        elif "ip address of the network" in query:
            ip = get('https://api.ipify.org').text
            speak(f'your IP address is {ip}')
            print(f'your IP address is {ip}')
        

        elif "open youtube" in query:
            wb.open("www.youtube.com")

        elif "search on google" in query:
            speak("sir, what should I search on google")
            cm = takeCommand().lower()
            wb.open(f"{cm}")

        #elif "Send the whatsapp message" in query:
            #pwt.sendwhatmsg("+917725912536", "This is testing protocol",a,b)

        elif "play songs on youtube" in query:
            speak("which song")
            query = str(takeCommand())
            pwt.playonyt(query)

        elif "play videos on youtube" in query:
            speak("which video, aniruddha?")
            query = str(takeCommand())
            pwt.playonyt(query)

        elif "email to aniruddha" in query:
                try:
                    speak("what should i say?")
                    content = takeCommand()
                    to = "aniruddha.joshi20@vit.edu"
                    sendEmail(to,content)
                    speak("Email has been sent to Aniruddha")

                except Exception as e:
                    print(e)
                    speak("sorry sir, i am not able to sent this mail ")


        elif 'news' in query:
            news = wb.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
        
        #elif "camera" in query or "take a photo" in query:
            #cap = cv2.VideoCapture(0)
            #cv2.Capture(0,"robo camera","img.jpg")
        
        #elif 'open R Studio' in query:
            #appli = r"C:\\Program Files\\RStudio\\bin\\RStudio.exe"
            #os.startfile(appli)
            
        elif 'powerpoint presentation' in query:
            speak("opening Power Point presentation")
            power = r"D:\\Projects\\SY SDP\\SDP PPT.pptx"
            os.startfile(power)
            