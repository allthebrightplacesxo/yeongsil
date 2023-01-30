import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pygame
import pygame.camera
from googletrans import Translator


listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
  engine.say(text)
  engine.runAndWait()  # This function will make the speech audible in the system, if you don't write this command then the speech will not be audible to you.

def take_command():
  try:
    with sr.Microphone() as source:
      print("listening...")
      voice = listener.listen(source)
      command = listener.recognize_google(voice)  # to transcribe any speech in the recording.
      command = command.lower()
      if 'alex' in command:
        command = command.replace('alex', '')
        print(command)
  except:
    pass
  return command

def run_alex():
  command = take_command()

  if 'play' in command:
    song = command.replace('play', '')
    talk('playing' + song)
    pywhatkit.playonyt(song)

  elif 'open camera' in command:
    pygame.camera.init()
    camlist = pygame.camera.list_cameras()
    if camlist:
    
        # initializing the cam variable with default camera
        cam = pygame.camera.Camera(camlist[0], (640, 480))
    
        # opening the camera
        cam.start()
    
        # capturing the single image
        image = cam.get_image()
    
        # saving the image
        pygame.image.save(image, "filename.jpg")

    
    # if camera is not detected the moving to else part
    else:
        print("No camera on current device")

  # elif 'translate' in command:
  #   translator = 

  elif 'time' in command:
    time = datetime.datetime.now().strftime('%I:%M:%S %p')
    talk('Current time is' + time)

  elif 'how are you' in command:
    talk('im fine, thank you. and you?')

  elif 'who is' in command:
    person = command.replace('who is', '')
    info = wikipedia.summary(person, 1)
    print(info)
    talk(info)

  elif 'friend' in command:
    talk('of course bestie!')

  elif 'joke' in command:
    print(pyjokes.get_joke())
    talk(pyjokes.get_joke())


  



  else:
    talk('i did not get that, could you repeat it please?')


run_alex()