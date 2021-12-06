import pyttsx3 as p
import speech_recognition as sr 
from datetime import datetime
from datetime import date
import pytz
 

engine = p.init()
listen = True
rate = engine.setProperty('rate' , 140)
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)

engine.say("hello , i am  suman's sister , what can i do for you ?")
engine.runAndWait()


r = sr.Recognizer()
mic = sr.Microphone()
while listen:
    with mic as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening")
        audio = r.listen(source)
        text=r.recognize_google(audio)
        print(text)
        if (text == "time"):
            zone = pytz.timezone('Asia/Kolkata')
            curentTime=datetime.now(zone)
            engine.say(curentTime.strftime("%H:%M"))
            engine.runAndWait()
        if (text == "date"):
            curentDate = datetime.today()
            engine.say(curentDate.strftime("%d:%m:%Y"))
            engine.runAndWait()  
        if  (text == "stop") or (text == "bro stop") or (text == "sister stop") or (text == "bro bye bye") or (text == " bro bye"):
            engine.stop
            engine.say("Okay Bro Bye Bye ! Have a good day ")
            listen = False
            engine.runAndWait()
        
