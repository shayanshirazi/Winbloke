from time import sleep
import pyttsx3
from shutdown.shutdown import restart
import speech_recognition as sr

# tts engine
gender = 1
speed = 140
volume = 1
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[gender].id)
engine.setProperty('rate', speed)
engine.setProperty('volume', volume)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        Play_Mp3_Files("start.wav")
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        Play_Mp3_Files("end.wav")
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query


def Play_Mp3_Files(File_Path):
    import os, sys, time
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    File_Path = os.path.join(base_path, File_Path)

    from playsound import playsound
    playsound(File_Path)
    return


# functions

def Joke():
    import pyjokes
    joke = pyjokes.get_joke(category="neutral")
    print(joke)
    speak(joke)
    Play_Mp3_Files("laught.wav")


def Internet_Speedtest():
    from threading import Thread
    import queue
    q = queue.Queue()
    speak("Cheking your internet speed. this might take a minute")

    def speed_test():
        import speedtest

        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        
        q.put( [res["download"], res["upload"], res["ping"]] )


    speedtest = Thread(target = speed_test)

    speedtest.start()

    while speedtest.is_alive():
        Play_Mp3_Files("wait.wav")
    
    
    stop_threads = False

    def sound_until_done():
        while True:
            Play_Mp3_Files("wait.wav")
            if stop_threads:
                break
    
    res = q.get()
    s = Thread(target = sound_until_done)
    s.start()
            
    print('Download: {:.2f} Mb/s'.format(res[0] / 1024 / 1000))

    speak('Download: {:.1f} Megabyte per second\n'.format(res[0] / 1024 / 1000))

    print('Upload: {:.2f} Mb/s'.format(res[1] / 1024 / 1000))

    speak('Upload: {:.1f} Megabyte per second\n'.format(res[1] / 1024 / 1000))

    print('Ping: {}'.format(int(res[2])))
    speak('Ping: {} mili second'.format(int(res[2])))

    stop_threads = True

    return


def Shutdown():
    from shutdown import shutdown
    shutdown(force=False, warning_off=False)


def Restart():
    from shutdown import restart
    restart(force=False)      


def Hibernate():
    from shutdown import hibernate
    hibernate(force=False)  


def Logoff():
    from shutdown import logoff
    logoff(force=False)


def Get_Ip():
    from requests import get

    ip = get('https://api.ipify.org').content.decode('utf8')
    return ip


def Ip_Country(ip):
    import requests
    API = "http://ip-api.com/json/"+ip
    response = requests.get(API)
    data = response.json()
    
    return data["country"], data["regionName"]


def Weather(city):
    import python_weather
    import asyncio

    async def getweather():
        client = python_weather.Client(format=python_weather.IMPERIAL)
        weather = await client.find(city)
        speak("{:.1f} degree celsius today".format((weather.current.temperature - 32) * 5/9))

        await client.close()


    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())


def Check_Network_Connection():
  import requests
  url = "http://www.google.com"
  try:
    requests.get(url, timeout=3)
    return True
  except (requests.ConnectionError, requests.Timeout):
    return False


def Number_Of_Microphone_Connected_Devices():
  import ctypes

  winmm = ctypes.windll.winmm.waveInGetNumDevs()
  
  if winmm != 0:
      return True
  else:
      return False


def Ram():
    import psutil

    if dict(psutil.virtual_memory()._asdict())["total"] >= 2857841664:
        return True
    else:
        return False


def Storage_Space():
  import shutil

  total, used, free = shutil.disk_usage("/")

  if free // (2**30) >= 1:
      return True
  else:
      return False


def Check_Operating_System():
    import platform
    
    if platform.system() != "Windows" or platform.machine() != "AMD64":
        return False
    return True


def Change_Desktop_Background():
    import urllib.request
    import os
    import ctypes
    from threading import Thread

    stop_threads = True
    
    speak("Downloading wallpaper image")

    def sound_until_done():
        while True:
            Play_Mp3_Files("wait.wav")
            if stop_threads:
                break

    s = Thread(target = sound_until_done)
    s.start()

    urllib.request.urlretrieve("https://picsum.photos/4000/2000?random=1", "wallpaper.jpg")
    
    speak("changing desktop background")
    path = os.path.abspath(os.getcwd())+ '\\' + "wallpaper.jpg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
    os.remove(path)
    speak("done!")
    stop_threads = False


# checking system and resources
speak("cheking your system.")
if not Check_Operating_System():
    speak("Winbloke is designed for 64bit windows systems. uncompatible with this device.")
    import sys
    sys.exit()
elif not Storage_Space():
    speak("Winbloke for best performance, need at least 1 gigabyte storage. start again when you have enought space.")
    import sys
    sys.exit()
elif not Ram():
    speak("Winbloke for best performance, need at least 2 gigabyte ram. start again when you have enought ram.")
    import sys
    sys.exit()
elif not Number_Of_Microphone_Connected_Devices():
    speak("This moment, you dont have any connected microphone. you can use winbloke chatbot and not speech commands.")
elif not Check_Network_Connection():
    speak("This moment, you are not connected to internet. you can use winbloke offline mode and not full version")
else:
    from threading import Thread
    import time

    def compatible():
        Play_Mp3_Files("compatible.wav")
    speedtest = Thread(target = compatible)
    speedtest.start()
    time.sleep(0.2)
    speak("Your device is 100 percent compatible with winbloke.")
    time.sleep(0.5)

print(
    """
Commands list:
    - joke
    - weather
    - internet speedtest
    - power 
        - hibernate
        - shodown
        - restart
        - logoff
    - voice
        - voice volume
        - voice gender
        - voice speed

enjoy winbloke 0.1.0 :)
    """
)


APIs_Dict = {
    "shutdown": ["shutdown", ["turn off", "computer"], ["power off", "computer"], "shuting down"], 
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
            
            
} 


def match(string, lst):

    for i in lst:
        flag = True
        if type(i) == list:
            for j in i:
                if string.count(j) == 0:
                    flag = False
                    break
            
            if flag:
                return True
        else:
            if string.count(i) != 0:
                return True
    
    return False





while True:
    command = takeCommand()

    if match(command, APIs_Dict["shutdown"]):
        import time
        speak("your device will be shotdown in 5 seconds")
        time.sleep(0.5)
        speak("4")
        time.sleep(0.5)
        speak("3")
        time.sleep(0.5)
        speak("2")
        time.sleep(0.5)
        speak("1")
        time.sleep(0.5)
        Shutdown()
    elif match(command, APIs_Dict["restart"]):
        import time
        speak("your device will be restart in 5 seconds")
        time.sleep(0.5)
        speak("4")
        time.sleep(0.5)
        speak("3")
        time.sleep(0.5)
        speak("2")
        time.sleep(0.5)
        speak("1")
        time.sleep(0.5)
        Restart()
    elif match(command, APIs_Dict["logout"]):
        import time
        speak("your device will be lock in 5 seconds")
        time.sleep(0.5)
        speak("4")
        time.sleep(0.5)
        speak("3")
        time.sleep(0.5)
        speak("2")
        time.sleep(0.5)
        speak("1")
        time.sleep(0.5)
        Logoff()
    elif match(command, APIs_Dict["hibernate"]):
        import time
        speak("your device will be hibernate in 5 seconds")
        time.sleep(0.5)
        speak("4")
        time.sleep(0.5)
        speak("3")
        time.sleep(0.5)
        speak("2")
        time.sleep(0.5)
        speak("1")
        time.sleep(0.5)
        Hibernate()
    elif match(command, APIs_Dict["weather"]):
        user_ip = Get_Ip()
        user_region = Ip_Country(user_ip)[1]
        speak("Weather by your ip region, "+user_region+" is")
        Weather(user_region)
    elif match(command, APIs_Dict["joke"]):
        Joke()
    elif match(command, APIs_Dict["speedtest"]):
        Internet_Speedtest()
    elif match(command, APIs_Dict["desktop_wallpaper"]):
        Change_Desktop_Background()
    elif match(command, APIs_Dict["voice_gender_man"]):
        if gender == 1:
            gender = 0
            engine.setProperty('voice', voices[gender].id)
            print("voice changed!")
            speak("voice changed!")
        else:
            speak("voice gender is already man")
            print("voice gender is already man")
    elif match(command, APIs_Dict["voice_gender_woman"]):
        if gender == 0:
            gender = 1
            engine.setProperty('voice', voices[gender].id)
            print("voice changed!")
            speak("voice changed!")
        else:
            speak("voice gender is already woman")
            print("voice gender is already woman")
    elif match(command, APIs_Dict["faster_voice"]):
        speed += 20
        engine.setProperty('rate', speed)
        print("voice is faster now!")
        speak("voice is faster now!")
    elif match(command, APIs_Dict["lower_voice"]):
        speed -= 20
        engine.setProperty('rate', speed)
        print("voice is slower now!")
        speak("voice is slower now!")
    elif match(command, APIs_Dict["volume_down"]):
        volume -= 0.2
        engine.setProperty('volume', volume)
        speak("voice volume is louder now")
    elif match(command, APIs_Dict["volume_up"]):
        volume += 0.2
        engine.setProperty('volume', volume)
        speak("voice volume is louder now")
    

    
    