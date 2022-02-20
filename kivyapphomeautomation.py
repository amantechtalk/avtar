import kivy 
from kivy.app import App 
from kivy.uix.label import Label 
  
  
# Replace this with your  
# current version 
kivy.require('1.11.1')  

class MyFirstKivyApp(App):

 def build(self):


     import csv
     import pyttsx3
     from fuzzywuzzy import fuzz 
     from fuzzywuzzy import process
     import speech_recognition as sr


     r = sr.Recognizer()


     with sr.Microphone() as source:
         print("speak into microphone")

         audio= r.listen(source)
     try:


            print("question:"+ r.recognize_google(audio))

     except sr.UnknownValueError:
            print("Audio ")
     except sr.RequestError as e:
            print("aman;{0}".format(e))

     aman3=r.recognize_google(audio) 



     matrix = []
     j=0
     i=0
     with open('bot1.csv') as f:
        reader = csv.reader(f)
        matrix.append(list(reader))
    

     for x in range (1,10):
        aman4=matrix[0][i]
        aman5=aman4[0]
        aman6=aman4[1]
        str(aman6)
        str(aman5)
       
        i=i+1
   
        aman=fuzz.token_sort_ratio(aman3,aman5) 
       
        if aman == 100:
         
           
            print("aman")
            engine =pyttsx3.init()
            voices=engine.getProperty('voices')
            engine.setProperty('voice',voices[1].id)
            engine.say(aman6)
            engine.runAndWait()
            j=j+1
            break
       
      
      
       
     return Label(aman6)  
MyFirstKivyApp().run()     


