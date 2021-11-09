#Source https://stackoverflow.com/questions/39224702/nao-robot-not-returning-recognized-words-getdata-is-empty

import time
from naoqi import ALProxy

#Initializes variables for later
data = []

#Put the IP address in for IP
#This initializes the recognition to work with english
IP = "138.67.201.73"
asr = ALProxy("ALSpeechRecognition", IP, 9559)
asr.setLanguage("English")

#This creates a vocabulary for the speech recognition to look through
asr.pause(True)
vocabulary = ["hello world", "bye"]
asr.setVocabulary(vocabulary, True)
asr.pause(False)

#This is how you use text to speech
tts = ALProxy("ALTextToSpeech", IP, 9559)
tts.say("because I can't hear you")

#start recognition
asr.subscribe(IP)
print 'speech recognition engine started'
memProxy = ALProxy("ALMemory", IP, 9559)
memProxy.subscribeToEvent('WordRecognized', IP, 'wordRecognized')

#Gives it time to process words said and or listen
asr.pause(False)
time.sleep(3)

#stop recognition
asr.unsubscribe(IP)

#Hopefully this will print any recognized words
data = memProxy.getData("WordRecognized")
print("data: {}".format(data))
