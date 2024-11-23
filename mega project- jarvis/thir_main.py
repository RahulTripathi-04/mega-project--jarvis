import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if "open google" in c.lower():
      speak("opening google..")
      webbrowser.open("http://google.com")
    elif "open facebook" in c.lower():
         speak("opening facebook..")
         webbrowser.open("http://facebook.com") 
    elif "open youtube" in c.lower():
         speak("opening youtube..")
         webbrowser.open("http://youtube.com")    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1] 
        link = musicLibrary.music[song]
        webbrowser.open(link)
           
 
if __name__ == "__main__":
    speak("Initializing jarvis...")
    
    while True:
        #Listen for wake word jarvis       
        # obtain audio from the microphone

        r = sr.Recognizer()
      

        
        # recognize speech using Sphinx
        print("recognizing...")
        try:
            with sr.Microphone() as source:
             print("Listening...")
             audio = r.listen(source, timeout=1, phrase_time_limit=1)
             command = r.recognize_google(audio)

            if(command.lower() == "jarvis"):
               speak("Yes")
            with sr.Microphone() as source:
             print("Jarvis Active")
             audio = r.listen(source)
             Command = r.recognize_google(audio)

             processCommand(command)
        except Exception as e:
           print("Error;{0}".format(e))
    