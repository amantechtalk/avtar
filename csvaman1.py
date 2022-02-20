





import cv2 
import csv
import pyttsx3
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process
import speech_recognition as sr
import time
x=10
int(x)
for x in range(1,10) :
 r = sr.Recognizer()

 t=1
 int(t)
 x=x+1
 with sr.Microphone() as source:
     print("speak into microphone")

     audio= r.listen(source)
 try:


        print("question:"+ r.recognize_google(audio))
        aman3=r.recognize_google(audio) 
 except sr.UnknownValueError:
        print("Audio ")
 except sr.RequestError as e:
        print("aman;{0}".format(e))

 



 matrix = []
 j=0
 i=0
 l=0
 with open('bot1.csv') as f:
    reader = csv.reader(f)
    matrix.append(list(reader))
    

 for x in range (1,12):
    aman4=matrix[0][i]
    aman5=aman4[0]
    aman6=aman4[1]
    str(aman6)
    str(aman5)
       
    i=i+1
   
    aman=fuzz.token_sort_ratio(aman3,aman5) 
       
    if aman >= 80:
         
           
           
           
  
  
# define a video capture object 
            vid = cv2.VideoCapture('aman4.mp4') 
  
            while(True): 
       
     # Capture the video frame 
     # by frame cv2.namedWindow('Resized Window', cv2.WINDOW_NORMAL)
                ret, frame = vid.read()
         #resize the window according to the screen resolution
                cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
                cv2.resizeWindow('frame', 1700, 1200)
                 
                   
    # Display the resulting frame 
                cv2.imshow('frame', frame)
                t=t+1
                if(t%51==0):
                       l=l+1
                       print("aman")
                       engine =pyttsx3.init()
                       voices=engine.getProperty('voices')
                       engine.setProperty('voice',voices[1].id)
                       try:
                        engine.say(aman4[l])
                        engine.runAndWait()
                       except:
                         break
                time.sleep(0.01)
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
                if cv2.waitKey(1) & 0xFF == ord('q'): 
                    break
  
# After the loop release the cap object 
            #vid.release() 
# Destroy all the windows 
            # cv2.destroyAllWindows()
           
            j=j+1
            print(aman6)
            
       
      

