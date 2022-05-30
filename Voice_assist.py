#SDP Harsh Assawa Roll No. 13

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import ctypes
import winshell
import subprocess
import requests
import json
import wolframalpha
import random
import smtplib
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tweepy
import pyautogui as p
import pyfirmata

#To set voice of assistant
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#To wish the user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")


    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")


    else:
        print("Good Evening!")
        speak("Good Evening!")


    print("I am your assistant. How may I help you")
    speak("I am your assistant. How may I help you")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     

    server.login('harshassawa24@gmail.com', 'shilpapawan135')
    server.sendmail('harshassawa24@gmail.com', to, content)
    server.close()

consumer_key = 'qF92gC79TCClIzyvJSyoScn0i'
consumer_secret = 'Udw251TubpTaQgD9uyFFWFrTd1uEHBmSSbunGz27CbYoS1zk4y'
access_token = '888454318889848837-zF6A1by9IUhaik6f7MVP7hxX9UFFX6I'
access_token_secret = 'TrkZDaHlE0e1uDLX6GDWI1pYDhaZmpKRb4bwC4Z2xK3Vu'

def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None

board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()
board.digital[7].mode = pyfirmata.OUTPUT
board.digital[7].write(1)
    

if __name__ == '__main__': 
    clear = lambda: os.system('cls') 

# This Function will clean any 
# command before execution of this python file 
    clear() 
    wishMe()
    webbrowser.register('chrome',
	    None,
	    webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))


    while True: 

        query = takeCommand().lower() 

        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")
            

        elif 'wikipedia' in query: 
            speak('Searching Wikipedia...') 
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences = 3) 
            speak("According to Wikipedia") 
            print(results)
            speak(results)
            
        elif 'how are you' in query:
            print("I am fine, Thank you") 
            print("How are you, Sir")
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in  query:
            print("It's good to know that your fine, How may I help you")
            speak("It's good to know that your fine, How may I help you")

        elif "who made you" in query or "who created you" in query: 
            print("I have been created by Harsh.")
            speak("I have been created by Harsh.")
        
        elif 'who am i' in query: 
            print("If you talk, then definately you are a human.")
            speak("If you talk, then definately you are a human.")
			
        elif 'lock the windows' in query or 'lock'in query: 
            print("Locking the device") 
            speak("locking the device") 
            ctypes.windll.user32.LockWorkStation()
            exit()

        elif 'shutdown the windows' in query: 
            print("Hold On a Sec ! Your system is on its way to shut down")
            speak("Hold On a Sec ! Your system is on its way to shut down") 
            subprocess.call(["shutdown", "/p","/f"])

        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled")

        elif "restart the windows" in query: 
            print("Hold On a Sec ! Your system is on its way to restart")
            speak("Hold On a Sec ! Your system is on its way to restart")
            subprocess.call(["shutdown", "/r"])

        elif 'open youtube' in query: 
            print("Here you go to Youtube\n")
            speak("Here you go to Youtube\n") 
            webbrowser.get('chrome').open("youtube.com")
            exit() 

        elif 'open google chrome' in query: 
            print("Here you go to Google\n") 
            speak("Here you go to Google\n") 
            webbrowser.get('chrome').open("google.com")
            exit()

        elif 'open google meet' in query:
            print("Here you go to Google meet\n") 
            speak("Here you go to Google meet\n")
            webbrowser.get('chrome').open("https://meet.google.com/")
            exit()

        elif 'open eduplus' in query:
            print("Here you go to eduplus\n") 
            speak("Here you go to eduplus\n")
            webbrowser.get('chrome').open("https://www.vierp.in/")
            exit()

        elif 'check my internet speed' in query:
            print("Here you go to Fast.com\n") 
            speak("Here you go to Fast.com\n")
            webbrowser.get('chrome').open("https://fast.com/")

        elif 'open whatsapp' in query:
            print("Here you go to whatsapp\n") 
            speak("Here you go to whatsapp\n")
            webbrowser.get('chrome').open("https://web.whatsapp.com/")
            exit()

        elif 'to shop online' in query:
            print("Here you go to Amazon\n") 
            speak("Here you go to Amazon\n")
            webbrowser.get('chrome').open("https://www.amazon.in/")
            exit()


        elif 'open visual studio' in query:
            print("Opening Visual Studio")
            speak("Opening Visual Studio") 
            appli = r"C:\Users\Harsh\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(appli)
            exit()

        
        elif 'open microsoft word' in query:
            print("Opening Word")
            speak("Opening Word") 
            appli = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word"
            os.startfile(appli)
            exit()

        elif 'open microsoft excel' in query:
            print("Opening Excel")
            speak("Opening Excel") 
            appli = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel"
            os.startfile(appli)
            exit()

        elif 'open microsoft powerpoint' in query:
            print("Opening Powerpoint")
            speak("Opening Powerpoint")
            appli = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint"
            os.startfile(appli)
            exit()

        elif 'open discord' in query:
            print("Opening Discord")
            speak("Opening Discord")
            appli = r"C:\Users\Harsh\AppData\Local\Discord\app-0.0.309/Discord"
            os.startfile(appli)
            exit()

        elif "what's the weather in" in query: 

            query = query.replace("what's the weather in", "") 
            city_name = query
            api_key = "dbe810963fb6b446cc5dc13d9e6cf552"
            base_url = "http://api.openweathermap.org/data/2.5/weather?" 
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            

            if x["cod"] != "404": 
                y = x["main"] 
                current_temperature = y["temp"] 
                temp_min= y["temp_min"]
                temp_max= y["temp_max"] 
                z = x["weather"] 
                weather_description = z[0]['description']
                print(city_name + "'s" + " weather :")
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n Min temperature = " +str(temp_min)+"\n Max temperature = " +str(temp_max)+"\n Description = " +str(weather_description))
                speak("Currently the temperature in")
                speak(city_name)
                speak("is")
                speak(current_temperature)
                speak(" kelvins")
                speak(" with the minimum of")
                speak(temp_min)
                speak(" kelvins")
                speak(" and the maximum of")
                speak(temp_max)
                speak(" kelvins")
                speak(" and is")
                speak(weather_description)
                
            else: 
                speak(" City Not Found ")

        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
            exit()

        
        elif "calculate" in query:  

            app_id = "PGKJJQ-KRUWU33P8T"
            client = wolframalpha.Client(app_id) 
            
            indx = query.lower().split().index('calculate')  
            query = query.split()[indx + 1:]  
            res = client.query(' '.join(query))
            if res['@success']=='true':
                pod0=res['pod'][0]['subpod']['plaintext']
                pod1=res['pod'][1]
            if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
                result = pod1['subpod']['plaintext']  
                print("The answer is " + result)  
                speak("The answer is " + result)
            

        elif 'play music' in query or "play song" in query:
            print("Here you go with your favourite music") 
            speak("Here you go with your favourite music") 
            music_dir = "E:\\Songs"
            songs = os.listdir(music_dir)
            random= random.choice(songs)
            os.startfile(os.path.join(music_dir, random))
            exit()

        elif 'email to harsh' in query:
            try:
                print("What should I say?")
                speak("What should I say?")
                content = takeCommand()
                to = "harshassawa2002@gmail.com"  
                sendEmail(to, content.capitalize())
                print("Email has been sent !")
                speak("Email has been sent !")
                exit()
            except Exception as e:
                print(e)
                print("I am not able to send this email")
                speak("I am not able to send this email")
                exit()
 
        elif 'send a mail' in query:
            try:
                print("What should I say?")
                speak("What should I say?")
                content = takeCommand()
                print("Whom should I send")
                speak("whom should i send")
                print("Email: ")
                to = input()    
                sendEmail(to, content.capitalize())
                print("Email has been sent !")
                speak("Email has been sent !")
                exit()
            except Exception as e:
                print(e)
                print("I am not able to send this email")
                speak("I am not able to send this email")
                exit()
        
        elif 'search google for' in query:
             
            query = query.replace("search google for", "")
            webbrowser.get('chrome').open("https://www.google.com/search?q="+ query)
            print("Searched Google for" + query)
            speak("Searched Google for")
            speak(query)
            exit()

        elif 'search youtube for' in query:

            query = query.replace("search youtube for", "")
            webbrowser.get('chrome').open("https://www.youtube.com/results?search_query="+ query)
            print("Searched Youtube for" + query)
            speak("Searched Youtube for")
            speak(query)
            exit()

        elif 'exit' in query:
            print("Thanks for giving me your time")
            speak("Thanks for giving me your time") 
            exit()

        elif 'news' in query:
             
            try: 
                jsonObj = urlopen('''https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=0bfc41e474034a3eb10cb5b644d7b911''')
                data = json.load(jsonObj)
                i = 1
                print('Here are some top news from the BBC News') 
                speak('here are some top news from the BBC News')
                print('''=============== BBC News ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))

        elif 'send a whatsapp message' in query:
            print("Whom do you want to send the message?")
            speak("Whom do you want to send the message")
            
            options = Options()
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.add_experimental_option('useAutomationExtension', False)

            driver = webdriver.Chrome('D:\College Files\TY- 1st Sem\SDP\chromedriver', options=options)
            driver.maximize_window()
            driver.get('https://web.whatsapp.com')

            time.sleep(2)

            whom = takeCommand()
            whomto = whom
            to = whomto.title()
            
            query = query.replace("send a whatsapp message", to)

            user = driver.find_element_by_xpath('//*[@title= "{}"]'.format(to)).click()

            print("What's the mesage you want to send?")
            speak("What's the mesage you want to send")
            msg = takeCommand()
            string = msg
            final_message = string.capitalize()
            count = 1
            query = "ZZz"
            
            query = query.replace("ZZz",final_message)

            for i in range(count):
                driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(query)
                send= driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]')
                send.click()
            
            print("Message sent successfully!")
            speak("Message sent successfully")
            
            exit()

        elif 'tic tac toe' in query:
            
            print("Welcome to tic tac toe game")
            speak("Welcome to tic tac toe game")

            # variable's
            win = 0
            lose = 0
            X = 'X'
            O = 'O'

            # definitions
            def win_check():
                global r1, r2, r3, r4, r5, r6, r7, r8, r9
                global X_win, O_win, tie
                global u_name, u2_name
                global win
                if r1 == 'X' and r2 == 'X' and r3 == 'X':
                    X_win = True
                elif r4 == 'X' and r5 == 'X' and r6 == 'X':
                    X_win = True
                elif r7 == 'X' and r8 == 'X' and r9 == 'X':
                    X_win = True
                elif r1 == 'X' and r4 == 'X' and r7 == 'X':
                    X_win = True
                elif r2 == 'X' and r5 == 'X' and r8 == 'X':
                    X_win = True
                elif r3 == 'X' and r6 == 'X' and r9 == 'X':
                    X_win = True
                elif r1 == 'X' and r5 == 'X' and r9 == 'X':
                    X_win = True
                elif r3 == 'X' and r5 == 'X' and r7 == 'X':
                    X_win = True
                elif r1 == 'O' and r2 == 'O' and r3 == 'O':
                    O_win = True
                elif r4 == 'O' and r5 == 'O' and r6 == 'O':
                    O_win = True
                elif r7 == 'O' and r8 == 'O' and r9 == 'O':
                    O_win = True
                elif r1 == 'O' and r4 == 'O' and r7 == 'O':
                    O_win = True
                elif r2 == 'O' and r5 == 'O' and r8 == 'O':
                    O_win = True
                elif r3 == 'O' and r6 == 'O' and r9 == 'O':
                    O_win = True
                elif r1 == 'O' and r5 == 'O' and r9 == 'O':
                    O_win = True
                elif r3 == 'O' and r5 == 'O' and r7 == 'O':
                    O_win = True
                if O_win:
                    win = True
                    
                    return print('Winner is', u2_name.upper()), win
                    speak("The Winner is" )
                    speak(u2_name.upper())
                if X_win:
                    win = True
                    print('The Winner is', u_name.upper()), win
                    speak('The Winner is')
                    speak(u_name.upper())
                    
                    exit()
                
                if r1 != '-' and r2 != '-' and r3 != '-' and r4 != '-' and r5 != '-' and r6 != '-' and r7 != '-' and r8 != '-' and r9 != '-':
                    tie = True
                    
                    return print('This game is a tie'), tie
                    speak('This game is a tie'), tie

            def rule():
                
                print('In Tic-Tac-Toe you have to make a straight line out of 3-O or 3-X')
                speak('In Tic-Tac-Toe you have to make a straight line out of 3-O or 3-X')
                
                print('For example:')
                speak('For example:')
                print(" X | O | X \n ---------- \n X | X | O \n ----------\n X | O | O \n")

            def check_game_o():
                global r1, r2, r3, r4, r5, r6, r7, r8, r9, command_2
                command_2= int(takeCommand())
                retry_check = False
                if command_2 == 1 and r1 == '-':
                    r1 = O
                elif command_2 == 2 and r2 == '-':
                    r2 = O
                elif command_2 == 3 and r3 == '-':
                    r3 = O
                elif command_2 == 4 and r4 == '-':
                    r4 = O
                elif command_2 == 5 and r5 == '-':
                    r5 = O
                elif command_2 == 6 and r6 == '-':
                    r6 = O
                elif command_2 == 7 and r7 == '-':
                    r7 = O
                elif command_2 == 8 and r8 == '-':
                    r8 = O
                elif command_2 == 9 and r9 == '-':
                    r9 = O
                elif command_2 == 1 and r1 != '-' or command_2 == 2 and r2 != '-' or command_2 == 3 and r3 != '-' or command_2 == 4 and r4 != '-' or command_2 == 5 and r5 != '-' or command_2 == 6 and r6 != '-' or command_2 == 8 and r8 != '-' or command_2 == 7 and r7 != '-' or command_2 == 9 and r9 != '-':
                    while not retry_check:
                        
                        print("Don't be Over smart! Try a place which is available as you can not over write a "
                        "place: ")
                        speak("Don't be Over smart! Try a place which is available as you can not over write a "
                        "place: ")
                        command_2=int(takeCommand())
                        check_game_o()
                        retry_check = True
                elif command_2 > 9:
                    retry_check = False
                    while not retry_check:
                        
                        print("Please select a number between 1-9 ONLY: ")
                        speak("Please select a number between 1-9 ONLY: ")
                        command_2= takeCommand()
                        check_game_o()
                        retry_check = True

                return r1, r2, r3, r4, r5, r6, r7, r8, r9

            def check_game_x():
                global r1, r2, r3, r4, r5, r6, r7, r8, r9, command
                command= int(takeCommand())
                retry_check = False
                if command == 1 and r1 == '-':
                    r1 = X
                elif command == 2 and r2 == '-':
                    r2 = X
                elif command == 3 and r3 == '-':
                    r3 = X
                elif command == 4 and r4 == '-':
                    r4 = X
                elif command == 5 and r5 == '-':
                    r5 = X
                elif command == 6 and r6 == '-':
                    r6 = X
                elif command == 7 and r7 == '-':
                    r7 = X
                elif command == 8 and r8 == '-':
                    r8 = X
                elif command == 9 and r9 == '-':
                    r9 = X
                elif command == 1 and r1 != '-' or command == 2 and r2 != '-' or command == 3 and r3 != '-' or command == 4 and r4 != '-' or command == 5 and r5 != '-' or command == 6 and r6 != '-' or command == 8 and r8 != '-' or command == 7 and r7 != '-' or command == 9 and r9 != '-':
                    while not retry_check:
                        print("Don't be Over smart! Try a place which is available as you can not over write a "
                        "place: ")
                        speak("Don't be Over smart! Try a place which is available as you can not over write a "
                        "place: ")
                        
                        command=int(takeCommand())
                        check_game_x()
                        retry_check = True
                elif command > 9:
                    retry_check = False
                    while not retry_check:
                        
                        print("Please select a number between 1-9 ONLY: ")
                        speak("Please select a number between 1-9 ONLY: ")
                    
                        command=int(takeCommand())
                        check_game_x()
                        retry_check = True
                return r1, r2, r3, r4, r5, r6, r7, r8, r9

            def computer_turn():
                global r1, r2, r3, r4, r5, r6, r7, r8, r9, command_2
                global comp_turn
                comp_turn = False
                while not comp_turn:
                    command_2 = random.randrange(1, 10)
                    if command_2 == 1 and r1 == '-':
                        r1 = O
                        comp_turn = True
                    elif command_2 == 2 and r2 == '-':
                        r2 = O
                        comp_turn = True
                    elif command_2 == 3 and r3 == '-':
                        r3 = O
                        comp_turn = True
                    elif command_2 == 4 and r4 == '-':
                        r4 = O
                        comp_turn = True
                    elif command_2 == 5 and r5 == '-':
                        r5 = O
                        comp_turn = True
                    elif command_2 == 6 and r6 == '-':
                        r6 = O
                        comp_turn = True
                    elif command_2 == 7 and r7 == '-':
                        r7 = O
                        comp_turn = True
                    elif command_2 == 8 and r8 == '-':
                        r8 = O
                        comp_turn = True
                    elif command_2 == 9 and r9 == '-':
                        r9 = O
                        comp_turn = True
                speak('I choose')
                speak(command_2)        
                return r1, r2, r3, r4, r5, r6, r7, r8, r9, print('I choose', command_2)
                

            def write_log():
                global u_name, u2_name, X_win, O_win
                global r1, r2, r3, r4, r5, r6, r7, r8, r9
                log = open('log.txt', 'a')
                log.seek(0)
                if X_win:
                    vb = u_name
                elif O_win:
                    vb = u2_name
                else:
                    vb = 'Tie'
                log.write('\n {} vs {} | {}'.format(u_name, u2_name, vb).upper())
                log.seek(0)
                log.write("\n\n {} | {} | {} \n ---------- \n {} | {} | {} \n ----------\n {} | {} | {}\n\n\n".format(r1, r2, r3, r4, r5, r6, r7, r8, r9))

            def read_log():
                log = open('log.txt', 'r')
                log.seek(0)
                print('\n\n')
                print(log.read(),'\n\n')  

            rule()
            time.sleep(0.5)
            time.sleep(0.5)
            while True:
                r1 = '-'
                r2 = '-'
                r3 = '-'
                r4 = '-'
                r5 = '-'
                r6 = '-'
                r7 = '-'
                r8 = '-'
                r9 = '-'
                u_name = 'Player 1'
                u2_name = 'Player 2'
                X_win = False
                O_win = False
                comp_turn = False
                win = False
                tie = False    
                print('Would you link to play with your friend or bot(f/b): ')
                speak('Would you like to play with your friend or bot') 
                
                duo_ai= takeCommand()
                
                
                if duo_ai == 'friend' or duo_ai == 'f' or duo_ai == 'my friend' or duo_ai == 'duo' or duo_ai == 'human':
                    game_on = True
                    
                    print('Hello, I am A.I. robot and i am your umpire today.')
                    speak('Hello, I am A.I. robot and i am your umpire today.')
                    
                    print('What should i call you player 1(X)? ')
                    speak('What should i call you player 1(X)? ')
                    u_name=input("Name: ")

                    print('What should i call you player 2(O)? ')
                    speak('What should i call you player 2(O)? ')
                    u2_name = input("Name: ")
                    
                    print("Let's see who wins today.")
                    speak("lets see who wins today.")

                    
                    print("Let's start with the game now", u_name.upper(), 'vs', u2_name.upper(), '\n')
                    speak("lets start with the game now")
                    speak(u_name.upper())
                    speak('versus')
                    speak(u2_name.upper())
                    
                    print("The positions are numbered from 1 to 9")
                    speak("The positions are numbered from 1 to 9")
                    print(' ', 1, '|', 2, '|', 3, '\n ---------- \n', '', 4, '|', 5, '|', 6, '\n ----------\n', '', 7,
                    '|', 8, '|', 9, '\n')
                    while game_on:
                        print('Which position you want to place the X to(1-9 only): ')
                        speak('Which position you want to place the X to(1-9 only): ')
                        
                        check_game_x()
                        print('\n ', r1, '|', r2, '|', r3, '\n ---------- \n', '', r4, '|', r5, '|', r6, '\n ----------\n', '',
                        r7, '|', r8, '|', r9, '\n')

                        win_check()
                        if win or tie:
                            write_log()
                            break
                        print('Which position you want to place the O to(1-9 only): ')
                        speak('Which position you want to place the O to(1-9 only): ')

                        check_game_o()
                        print('\n ', r1, '|', r2, '|', r3, '\n ---------- \n', '', r4, '|', r5, '|', r6, '\n ----------\n', '',
                        r7, '|', r8, '|', r9, '\n')

                        win_check()
                        if win or tie:
                            write_log()
                            break

                elif duo_ai == 'computer' or duo_ai == 'bot' or duo_ai == 'ai' or duo_ai == 'single' or duo_ai == 'b':
                    print('Hello, I am A.I. robot and i am your opponent today.')
                    speak('Hello, I am A.I. robot and i am your opponent today.')
                    
                    print('What should i call you? ')
                    speak('What should i call you? ')
                    
                    u_name= input("Name: ")
                    
                    print("Let's see if you can beat me.")
                    speak('lets see if you can beat me')
                    
                    u2_name = 'bot'

                    print("Let's start with the game now", u_name.upper(), '\n')
                    speak("lets start with the game now")
                    speak(u_name)
                    
                    print("The positions are numbered from 1 to 9")
                    speak("The positions are numbered from 1 to 9")
                    
                    print(' ', 1, '|', 2, '|', 3, '\n ---------- \n', '', 4, '|', 5, '|', 6, '\n ----------\n', '', 7,
                    '|', 8, '|', 9, '\n')
                    game_on = True
                    while game_on:
                        print('Which position you want to place the X to(1-9 only): ')
                        speak('Which position you want to place the X to(1-9 only): ')
                        
                        
                        check_game_x()
                        print('\n ', r1, '|', r2, '|', r3, '\n ---------- \n', '', r4, '|', r5, '|', r6, '\n ----------\n', '',
                        r7, '|', r8, '|', r9, '\n')

                        win_check()
                        if win or tie:
                            write_log() 
                            break
                        print("It's my turn now")
                        speak("It's my turn now")
                        
                        computer_turn()

                        print('\n ', r1, '|', r2, '|', r3, '\n ---------- \n', '', r4, '|', r5, '|', r6, '\n ----------\n', '',
                        r7, '|', r8, '|', r9, '\n')
                        win_check()
                        if win or tie:
                            write_log()
                            break

            else:
                print("It's seems some error occurred, please check your spellings.")
                speak("It's seems some error occurred, please check your spellings.")

        elif 'tweet' in query:
            oauth = OAuth()
            api = tweepy.API(oauth)
            
            print("What do you want to tweet")
            speak("What do you want to tweet")
            post_tweet = takeCommand()
            final_tweet = post_tweet.capitalize()
            api.update_status(final_tweet)
            time.sleep(2)

            print("Tweet posted successfully")
            speak("Tweet posted successfully")
            exit()

        elif 'increase volume' in query:
            p.hotkey('volumeup','volumeup')
            print("Volume increased")
            speak("Volume increased")

        elif 'decrease volume' in query:
            p.hotkey('volumedown','volumedown')
            print("Volume decreased")
            speak("Volume decreased")

        elif 'page down' in query:
            p.hotkey('pgdn')

        elif 'page up' in query:
            p.hotkey('pgup')

        elif 'move this window to the left' in query:
            p.hotkey('winleft','left')

        elif 'move this window to the right' in query:
            p.hotkey('winleft','right')

        elif 'turn on the light' in query:
            print("Turning on lights")
            speak("Turning on lights")
            board.digital[7].write(0)
            print("Turned on lights")
            speak("Turned on lights")
        
        elif 'turn off the light' in query:
            print("Turning off lights")
            speak("Turning off lights")
            board.digital[7].write(1)
            print("Turned off lights")
            speak("Turned off lights")

        
