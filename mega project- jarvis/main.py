
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "bfad2f22adc247818b1e622dd264046f"

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if "open google" in c.lower():
      webbrowser.open("http://google.com")
    elif "open facebook" in c.lower():
         webbrowser.open("http://facebook.com") 
    elif "open youtube" in c.lower():
         webbrowser.open("http://youtube.com")    
    elif c.lower().startswith("play"):
       song = c.split("play ", 1)[1]
       if song in musicLibrary.music:
          speak(f"Playing {song}...")
          webbrowser.open(musicLibrary.music[song])  

       else:
         speak("Sorry, I couldn't find that song." )
    elif "news" in c.lower():
       r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}") 
       if r.status_code == 200:
        data = r.json()  # Parse the JSON response
        articles = data.get('articles', [])
        
        for article in articles:
            title = article.get('title')
            
            
            speak ({title})
             
        else:
          print(f"Failed to fetch news: {r.status_code}")      

 
if __name__ == "__main__":
    speak("Initializing jarvis...")
    
    while True:
        #Listen for wake word jarvis       
        # obtain audio from the microphone

        r = sr.Recognizer()
        '''with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=2, phrase_time_limit=1)'''

        
        # recognize speech using Sphinx
        print("recognizing...")
        try:
            with sr.Microphone() as source:
             print("Listening...")
             audio = r.listen(source, timeout=1, phrase_time_limit=1)
             command = r.recognize_google(audio)

            if(command.lower() == "jarvis"):
               speak("Ya")
            with sr.Microphone() as source:
             print("Jarvis Active")
             audio = r.listen(source)
             command = r.recognize_google(audio)

             processCommand(command)
        except Exception as e:
           print("Error;{0}".format(e))
    