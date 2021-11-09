from naoqi import ALProxy

ip = "138.67.201.73" 
motion = ALProxy("ALMotion", ip, 9559)
tts = ALProxy("ALTextToSpeech", ip, 9559)
motion.setStiffnesses("Body", 1.0)
motion.moveInit()
motion.post.moveTo(0.5, 0, 0)
tts.say("I am now on my way to destroy all humans")


