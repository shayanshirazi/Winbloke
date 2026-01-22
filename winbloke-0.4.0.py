import pyttsx3
import speech_recognition as sr
import os
import sys
from playsound import playsound
import platform
import requests
import wmi
import pyjokes
import speedtest
from shutdown import *
import python_weather
import asyncio
import urllib.request
import ctypes
import webbrowser
import wikipedia
import cv2
import winshell
import queue
from GoogleNews import GoogleNews
import winapps

class Voice:
    gender = 1
    speed = 140
    volume = 1
    sound_effect = True

    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[self.gender].id)
        self.engine.setProperty('rate', self.speed)
        self.engine.setProperty('volume', self.volume)
    
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def change_gender(self, new_gender):
        self.gender = new_gender
        self.engine.setProperty('voice', self.voices[self.gender].id)

    def change_speed(self, new_speed):
        self.speed = new_speed
        self.engine.setProperty('rate', self.speed)

    def change_volume(self, new_volume):
        self.volume = new_volume
        self.engine.setProperty('volume', self.volume)

    def take_command(self):
        with sr.Microphone() as source:
            self.recognizer.pause_threshold = 1
            self.play_sound("start.wav")
            audio = self.recognizer.listen(source)
        
        try:
            query = self.recognizer.recognize_google(audio)
            self.play_sound("end.wav")
            return query
    
        except Exception:
            return None
    

    def play_sound(self, file_path):
        if self.sound_effect:
            base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
            file_path = 'sound/' + file_path
            file_Path = os.path.join(base_path, file_path)
            playsound(file_Path)



class System:
    def __init__(self):
        computer = wmi.WMI()
        os_info = computer.Win32_OperatingSystem()[0]
    
        self.os_type = platform.system()
        self.os_name = os_info.Name.encode('utf-8').split(b'|')[0]
        self.CPU = computer.Win32_Processor()[0].Name
        self.GPU = computer.Win32_VideoController()[0].Name
        self.ram = round(float(os_info.TotalVisibleMemorySize) / 1048576)

        self.name = platform.uname().node
        self.machine = platform.machine()

        self.ip = requests.get('https://api.ipify.org').content.decode('utf8')
        ip_information = requests.get("http://ip-api.com/json/"+self.ip).json()
        self.country = ip_information["country"]
        self.country_code = ip_information["countryCode"]
        self.city = ip_information["regionName"]
        self.microphone_count = ctypes.windll.winmm.waveInGetNumDevs()

    def Shutdown(self):
        shutdown(force=False, warning_off=False)

    def Restart(self):
        restart(force=False)      

    def Hibernate(self):
        hibernate(force=False)  

    def Logoff(self):
        logoff(force=False)

    def Check_Network_Connection():
        try:
            requests.get("https://www.google.com", timeout=3)
            return True
        except (requests.ConnectionError, requests.Timeout):
            return False





class API:
    def __init__(self):
        pass

    def Joke(self):
        joke = pyjokes.get_joke(category="neutral")
        return joke

    def Internet_Speedtest(self):
        test = speedtest.Speedtest()
        test.get_servers()
        test.get_best_server()
        test.download()
        test.upload()
        res = test.results.dict()
        
        return ( res["download"]/1024000, res["upload"]/ 1024000, int(res["ping"]) )
    
    def Weather(self, city):
        q = queue.Queue()
        async def getweather():
            client = python_weather.Client(format=python_weather.IMPERIAL)
            weather = await client.find(city)
            await client.close()
        
            q.put( weather.current.temperature)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(getweather())

        return q.get()

    
    def Random_Wallpaper(self):
        urllib.request.urlretrieve("https://picsum.photos/4000/2000?random=1", "wallpaper.jpg")

        return os.path.abspath(os.getcwd())+ '\\' + "wallpaper.jpg"
    
    def Change_Desktop_Photo(self, path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
        os.remove(path)
    

    def Bitcoin_Price(self):
        return int(str(requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()["bpi"]["USD"]["rate"]).replace(",", "").split(".")[0])
        
    
    def Open_Site(self, url):
        webbrowser.open(url)

    def Wikipedia_Search(self, subject):
        return wikipedia.summary(subject, sentences=1)


    def Capture_Photo(self):
        cap = cv2.VideoCapture(0)
        ret,frame = cap.read()

        while(True):
            cv2.imshow('Photo',frame)
            if cv2.waitKey(1) & 0xFF > ord('a'):
                cv2.imwrite('capture.png',frame)
                cv2.destroyAllWindows()
                break

        cap.release()
        os.remove('capture.png')
    

    def Delete_Temprery_Files(self):
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        
    
    def Google_News(self, country):
        googlenews = GoogleNews(lang='en')
        googlenews.get_news(country)

        return googlenews.get_texts()


    def Show_Installed_App():
        apps = []

        for app in winapps.list_installed(): 
            apps.append(app.name)
        
        return apps


class Command:
    APIs_Dict = {
        "shutdown": ["shutdown", "shut down", ["turn off", "computer"], ["power off", "computer"], "shuting down"], 
        "restart": [["restart", "computer"], ["restarting", "computer"], ["restarter", "button"]],
        "logout": [ "logout", ["log", "out"], "lock", ["change", "user"]],
        "hibernate": ["hibernate"],
        "weather": ["weather", "climate", "clime"],
        "joke": ["joke", ["make", "me", "laught"], ["make", "me", "happy"], "jest", "witticism", "quip", "pleasantry", "pun", ["old", "chestnut"], ["double", "entendre"], "gag", "wisecrack"],
        "speedtest": [["speed", "test"], ["speed", "internet"], ["speed", "network"]],
        "desktop_wallpaper" : [["change", "desktop", "backgrounnd"],["change", "desktop", "picture"], ["changing", "desktop", "picture"], ["change", "desktop", "wallpaper"], ["changing", "desktop", "wallpaper"], ["tired", "desktop", "photo"], ["new", "wallpaper"]],
        "voice_gender_man" : [["voice", "male"], ["voice", "man"]],
        "voice_gender_woman" : [["voice", "female"], ["voice", "woman"]],
        "faster_voice" : [["voice", "fast"], ["voice", "hight"]],
        "lower_voice" : [["voice", "slower"], ["voice", "down"]],
        "volume_down" : [["volume", "soften"], ["volume", "subdue"], ["volume", "benumb"], ["volume", "dampen"], "deaf", ["voice", "loud"]],
        "volume_up" : [["volume", "up"], ["volume", "boost"], ["volume", "enhance"], ["volume", "increase"], ["volume", "intensifies"], "louder", ["volume", "raise"]],
        "bitcoin": ["bitcoin"],
        "open_site": [ ["dot", "open"], ["open", "."], ["go to", "dot"], ["go to", "."] ],
        "wikipedia": ["wikipedia"],
        "capture_photo": [ ["take", "photo"], ["capture", "photo"] ],
        "empty_recycle_bin": [ ["empty", "recycle bin"], "recycle bin" ],
    } 


    def __init__(self):
        pass