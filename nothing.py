import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit 
import wikipedia
import os
import pyautogui
import requests
from pytube import YouTube
import datetime   
from playsound import playsound  
import keyboard
from googletrans import Translator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)

def Speak(Audio):
    print("   ")
    print(f": {Audio}")
    engine.say(Audio) 
    print("    ")
    engine.runAndWait()

def Wishme():
    hour =int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        Speak("Good Morning Sir !")

    elif hour >= 12 and hour<18:
        Speak("Good Afternoon Sir !")

    else:
        Speak("Good Evening  sir !")

def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:   
        return "None"
        
    return query.lower()

def TaskExe():
    Wishme()
    Speak(" Please tell me your name ")
    name = takecommand()
    Speak(f"Hello {name} ")
    Speak("How May I Help You?")

    def Music():
        Speak("Tell Me The Name oF The Song!")
        musicName = takecommand()
        pywhatkit.playonyt(musicName)

        Speak("Your Song Has Been Started! , Enjoy Sir!")

    def OpenApps():
        Speak("Ok Sir , Wait a Second!")

        if 'vs code' in query:
            os.startfile("C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'telegram' in query:
            os.startfile("E:\\Telegram Desktop\\Telegram.exe")

        elif 'notepad' in query:
            os.startfile("C:\\Program Files (x86)\\Notepad++\\notepad++.exe")
               
        elif 'made easy' in query:
            webbrowser.open("C:\Program Files\Made Easy\MadeEasyLive.exe")
             
        elif 'meeting' in query:
            webbrowser.open("https://meet.google.com/?hs=197&pli=1&authuser=0")    

        elif 'classroom' in query:
            webbrowser.open('https://classroom.google.com/u/0/h')

        elif 'jamboard' in query:
            webbrowser.open('https://jamboard.google.com/u/0/')

        elif 'gmail' in query:
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')    

        elif 'photos' in query:
            webbrowser.open('https://photos.google.com/?tab=mq&pageId=none')

        elif 'translator' in query:
            webbrowser.open('https://translate.google.co.in/?hl=en-GB&tab=qT')

        elif 'news' in query:
            webbrowser.open('https://news.google.com/topstories?tab=Tn&hl=hi&gl=IN&ceid=IN:hi')

        elif 'calendar' in query:
            webbrowser.open('https://calendar.google.com/calendar/u/0/r?tab=nc&pli=1')        

        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'maps' in query:
            webbrowser.open('https://www.google.co.in/maps/@23.2491486,77.5046096,15z?hl=en&authuser=0')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')

        Speak("Your Command Has Been Completed Sir!")
               
    def CloseAPPS():
        Speak(f"Ok {name} , Wait A second!")

        if 'youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        elif 'telegram' in query:
            keyboard.press_and_release('alt+F4')

        elif 'vs code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'notepad' in query:
            keyboard.press_and_release('alt+F4')

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        Speak("Your Command Has Been Succesfully Completed!")

    def YoutubeAuto():
        Speak("Whats Your Command ?")
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press_and_release('space bar')

        elif 'next' in comm:
            keyboard.press_and_release('shift+n')

        elif 'mute' in comm:
            keyboard.press_and_release('m')

        elif 'forward' in comm:
            keyboard.press_and_release('l')

        elif 'back' in comm:
            keyboard.press_and_release('j')

        elif 'full screen' in comm:
            keyboard.press_and_release('f')

        elif 'film mode' in comm:
            keyboard.press_and_release('t')

        Speak(f"Done  {name} ")

    def ChromeAuto():
        Speak("Chrome Automation started!")

        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

    def screenshot():
        Speak(f"Ok {name} , What Should I Name That File ?")
        path = takecommand()
        path1name = path + ".png"
        path1 = "E:\\sk\\"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("E:\\sk\\")
        Speak("Here Is Your ScreenShot") 

    while True:

        query = takecommand()

        if 'hello' in query:
            Speak(f"Hello {name}  , I Am Your Personal AI Assistant!")


        elif 'how are you' in query:
            Speak(f"I Am Fine {name} Sir!")
            Speak("Whats About YOU?")

        elif 'switch off' in query:
            Speak(f"Ok {name}  , You Can Call Me Anytime !")
            
            hour =int(datetime.datetime.now().hour)
            if hour >= 0 and hour<12:
                Speak("Good day sir!")

            elif hour >= 12 and hour<18:
                Speak("Good day sir!")
                
            else:
                Speak("Good night  sir !")
            
            break

        elif 'youtube search' in query:
            Speak(f"OK {name} , This Is What I found For Your Search!")
            query = query.replace("nothing","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            pywhatkit.playonyt(query)

        elif 'launch' in query:
            Speak("Tell Me The Name Of The Website!")
            site = takecommand()
            web = 'https://www.' + site + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("nothing","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")

        elif 'screenshot' in query:
            screenshot()

        elif 'open jamboard' in query:
            OpenApps()

        elif 'open photos' in query:
            OpenApps()

        elif 'open classroom' in query:
            OpenApps()

        elif 'open drive' in query:
            OpenApps()  

        elif 'open calendar' in query:
            OpenApps()

        elif 'open gmail' in query:
            OpenApps()  

        elif 'meeting' in query:
            OpenApps()      

        elif 'open translator' in query:
            OpenApps()         

        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'open vs code' in query:
            OpenApps()

        elif 'open notepad'in query:
            OpenApps()

        elif 'open madeeasy'in query:
            OpenApps()    

        elif 'open youtube' in query:
            OpenApps()
            
        elif 'open telegram' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'close chrome' in query:
            CloseAPPS()

        elif 'music' in query:
            Music()

        elif 'close telegram' in query:
            CloseAPPS()

        elif 'close instagram' in query:
            CloseAPPS()

        elif 'close vs code' in query:
            CloseAPPS()

        elif 'close notepad' in query:
            CloseAPPS()
           
        elif 'undo' in query:
            keyboard.press_and_release('ctrl+ z') 

        elif 'select all' in query:
            keyboard.press_and_release('ctrl+ a')    

        elif 'control' in query:
            keyboard.press_and_release('ctrl+ v')

        elif 'cut' in query:
            keyboard.press_and_release('ctrl+ x')

        elif 'copy' in query:
            keyboard.press_and_release('ctrl+ c')
            Speak("copied sir")

        elif 'pause' in query:
            keyboard.press_and_release('k')
        
        elif 'play' in query:
            keyboard.press_and_release('k')

        elif 'next' in query:
            keyboard.press_and_release('shift+n')

        elif 'mute' in query:
            keyboard.press_and_release('m')

        elif 'restart' in query:
            keyboard.press_and_release('0')

        elif 'forward' in query:
            keyboard.press_and_release('l')

        elif 'back' in query:
            keyboard.press_and_release('j')

        elif 'full screen' in query:
            keyboard.press_and_release('f')

        elif 'new tab' in query:
            keyboard.press_and_release('ctrl+ n')    

        elif 'film mode' in query:
            keyboard.press_and_release('t')

        elif 'close tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'repeat my word' in query:
            Speak("Speak Sir!")
            jj = takecommand()
            Speak(f"You Said : {jj}")

        elif ' location' in query:
            Speak("Ok Sir , Wait A Second!")
            webbrowser.open('https://www.google.com/maps/place/A-Sector,+Gopal+Nagar,+Bhopal,+Madhya+Pradesh+462022/@23.2458573,77.4907322,17z/data=!3m1!4b1!4m5!3m4!1s0x397c41e828fb430d:0xa54fc1eccd8662f2!8m2!3d23.2459388!4d77.4927793')

        elif 'alarm' in query:
            Speak("Enter The Time !")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time To Wake Up Sir!")
                    Speak("Alarm Closed!")

                elif now>time:
                    break

        elif 'google search' in query: 
            import wikipedia as googleScrap
            query = query.replace("nothing","")
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                Speak(result)

            except:
                Speak("No Speakable Data Available!")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"sir , the time is {strTime}")

        elif 'close it' in query:
            keyboard.press_and_release('alt+F4')  

        elif 'home' in query:
            os.startfile('E:\\Nothing\\nothing.py')     

TaskExe()
