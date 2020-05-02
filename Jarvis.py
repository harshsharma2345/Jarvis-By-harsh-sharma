import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import sys
import subprocess
import smtplib
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

engine = pyttsx3.init() # object creation

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)

def speak(audio):
    rate = engine.getProperty('rate')
    newVoiceRate = 240
    engine.setProperty('rate', newVoiceRate)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak ("Good Morning sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")

    speak("I am Jarvis,Your Assistant how can I help")
#It takes microphone input from the user and returns string output

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening...")
       r.pause_threshold=0.8
       audio=r.listen(source)
    try:
       print("Recognizing...")
       query = r.recognize_google(audio)
       print(f"User Said: {query}\n")
    except Exception as e:
         print("Say that again please...")
         return "None"
    return query
def sendEmail(to, content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('harshsharma2345@gmail.com','9694018553bhanu')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()


def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])
def taskperformlist():
    speak("I can Search in wikipedia,Send an email,play music,run games,give weather reports,open a website,Tell you the time,search online")
if __name__== "__main__":
    wishMe()

    while True:
        query = takecommand().lower()

        #logic for executing tasks based on query
        if "tasks" in query or "can" in query or "what actions" in query:
            taskperformlist()
        elif 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query or 'open youtube.com' in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening youtube")
        elif 'google' in query or 'google.com' in query:
            webbrowser.open("https://www.google.com")
            speak("Opening google")
        elif 'gmail' in query or 'gmail.com' in query:
            webbrowser.open("https://www.gmail.com")
            speak("Opening google mail")
        elif 'apple.com' in query:
            webbrowser.open("https://www.apple.com")
            speak("Opening apple")
        elif 'coronavirus' in query:
            webbrowser.open("https://www.worldometers.info/coronavirus/")
            speak("Showing coronavirus reports")

        elif 'the time'  in query:
             strTime= datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Sir, The time is{strTime}")


        elif 'email to harsh' in query:
           try:
               speak("what should I say?")
               content=takecommand()
               to  = "harsh16csu140@ncuindia.edu"
               sendEmail(to,content)
               speak("Email has been sent!")
           except Exception as e:
               print(e)
               speak("Sorry, your Email can't be sent   some   error   occurred ")
        elif 'play shayad of arijit singh' in query or 'play music' in query:
               open_file('/Users/harshsharma/Documents/music/Shayad - Love Aaj Kal - Kartik - Sara - Arushi - Pritam - Arijit Singh.webm')
        elif 'games' in query:
               speak("ohkay sir,have fun")
               open_file('/System/Applications/chess.app')

        elif 'weather' in query:
            # import required modules
            import requests, json

            # Enter your API key here
            api_key = "87e0e336972e8bd32e4bd7d65f28a7d2"

            # base_url variable to store url
            base_url = "http://api.openweathermap.org/data/2.5/weather?"

            # Give city name
            city_name = "bhiwadi"

            # complete_url variable to store
            # complete url address
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name

            # get method of requests module
            # return response object
            response = requests.get(complete_url)

            # json method of response object
            # convert json format data into
            # python format data
            x = response.json()

            # Now x contains list of nested dictionaries
            # Check the value of "cod" key is equal to
            # "404", means city is found otherwise,
            # city is not found
            if x["cod"] != "404":

                # store the value of "main"
                # key in variable y
                y = x["main"]

                # store the value corresponding
                # to the "temp" key of y
                current_temperature = y["temp"]
                tempincelsius=int(current_temperature-273)

                # store the value corresponding
                # to the "pressure" key of y
                current_pressure = y["pressure"]

                # store the value corresponding
                # to the "humidity" key of y
                current_humidiy = y["humidity"]

                # store the value of "weather"
                # key in variable z
                z = x["weather"]

                # store the value corresponding
                # to the "description" key at
                # the 0th index of z
                weather_description = z[0]["description"]

                speak("weather at your location is as follows")
                speak("Temperature is " +str(tempincelsius) +" degree celsius")
                speak("atmospheric pressure is"+str(current_pressure) +"hpa")
                speak("humidity is " + str(current_humidiy) + "percent")
                speak("weather is " +str(weather_description))

            else:
                speak(" City Not Found ")
        elif 'out' in query or 'rain' in query:
            # import required modules
            import requests, json

            # Enter your API key here
            api_key = "87e0e336972e8bd32e4bd7d65f28a7d2"

            # base_url variable to store url
            base_url = "http://api.openweathermap.org/data/2.5/weather?"

            # Give city name
            city_name = "bhiwadi"

            # complete_url variable to store
            # complete url address
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name

            # get method of requests module
            # return response object
            response = requests.get(complete_url)

            # json method of response object
            # convert json format data into
            # python format data
            x = response.json()

            # Now x contains list of nested dictionaries
            # Check the value of "cod" key is equal to
            # "404", means city is found otherwise,
            # city is not found
            if x["cod"] != "404":
                # store the value of "main"
                # key in variable y
                y = x["main"]

                # store the value corresponding
                # to the "temp" key of y
                current_temperature = y["temp"]
                tempincelsius = int(current_temperature - 273)

                # store the value corresponding
                # to the "pressure" key of y
                current_pressure = y["pressure"]

                # store the value corresponding
                # to the "humidity" key of y
                current_humidiy = y["humidity"]

                # store the value of "weather"
                # key in variable z
                z = x["weather"]

                # store the value corresponding
                # to the "description" key at
                # the 0th index of z
                weather_description = z[0]["description"]
            if str(weather_description)=="rainy" or str(weather_description)=="cloudy":
                speak("You should Take Umbrella with you sir,if possible stay at home")
            else:
                 speak("It is not going to rain today,you can go and enjoy")
        elif 'thank you' in query:
            speak("Your welcome,sir")
        elif 'search online' in query:
            querysearch = query.replace("search online for", "")
            speak("searching online for your query")
            driver = webdriver.Chrome()
            driver.get("https://www.google.co.in")
            driver.find_element_by_name("q").send_keys(str(querysearch))
            elm = driver.find_element_by_name("btnK")
            driver.implicitly_wait(2)
            elm.click()

        elif 'shutdown' in query:
            speak("I am going to sleep,will take your dreams sir")
            exit()


