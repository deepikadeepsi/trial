#import speech_recognition 
from PIL import Image    
import pytesseract
 # converts the text to speech  
#import pyttsx3   
from simple_colors import *          
from googletrans import Translator 
from gtts import gTTS
import os

  

#engine=pyttsx3.init('sapi5')   
#voices=engine.getProperty('voices')
#engine.setProperty('voice','voices[1].id')

#def speak(k):
    # engine.say(k)                             
    # engine.runAndWait()
  

img = Image.open('C:\coding\images.png')     
  

print(img)                          

pytesseract.pytesseract.tesseract_cmd ='C:\Program Files\Tesseract-OCR\Tesseract.exe'  
result = pytesseract.image_to_string(img)  

with open("C:\\coding\\abc.txt","w") as file:    
     #open(“c:\\temp.txt”, “w”)
                 print(file.write(result))
                 language='en'
                 myobj = gTTS(text=result,lang=language,slow=False)
                 print(myobj)
                 h="The text present in image is:\n"
                 print (blue('THE TEXT FROM IMAGE:', ['bold','underlined']))
                 print(result[:-1])
         # for line in f:
        #print(line)         
                 
              #with open('the-zen-of-python.txt') as f:
    #contents = f.read()
    #print(contents)      
p = Translator()
                     

k = p.translate(result,dest='kn')  
print (blue('TRANSLATION', ['bold','underlined']))
print(k)



#def speak(k):
    #engine.say(k)                             
    #engine.runAndWait()

#print(k)
#print()
#engine = print.init()
  
# an audio will be played which speaks the test if pyttsx3 recognizes it
#engine.say(k)                             
#engine.runAndWait()

#language='kn'
#myobj = gTTS(text=k, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")