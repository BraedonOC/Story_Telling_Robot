import yaml 
import qi
import argparse 
from sys import argv
import time
from naoqi import ALProxy

#class Node:
#    def __init__(self, story, question, branch_list, params):
#        self.branch_list = branch_list
#        self.story = story
#        self.question = question
#        self.params = params  # we may want to expand params into more arguments


NAO_MODE = True
FAST_MODE = False
start_node = "intro" 

interesting_voices = {'narrator' : 1,
          'adult male' : 0.9,
          'mysterious' : 0.88,
          'boy child' : 1.2,
          'evil' : 0.6, 
          'woman' : 1.2
      }

bland = {'narrator' : 1,
          'mysterious' : 1,
          'adult male' : 1,
          'boy child' : 1,
          'evil' : 1 ,
          'woman' : 1
      }

voices = interesting_voices

class RobotBrain:
    def __init__(self):
        if NAO_MODE:
            self.initialize_NAO()

        self.say("I'm ready to tell a story")

    def initialize_NAO(self):
       # self.audio = self.session.service('ALAudioPlayerProxy')
       # self.audio.setVolume(0.1)
            
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", type=str, default="138.67.231.171",
                            help="Robot's IP address. If on a robot or a local Naoqi - use '169.254.74.67' (this is the default value).")
        parser.add_argument("--port", type=int, default=9559,
                            help="port number, the default value is OK in most cases")
        parser.add_argument("--story", type=str, default="full_story.yaml",
                            help="the path to the yaml file containing a story for the robot to tell")

        args = parser.parse_args()
        self.read_story_yaml(args.story)
        self.ip = args.ip
        self.port = args.port
        self.session = qi.Session()
        self.audio_device = ALProxy("ALAudioDevice", self.ip, 9559)
        # print(ALProxy('ALSpeechRecognition', self.ip, 9559).__dict__)
        self.audio_device.setOutputVolume(50)
        try:
            self.session.connect("tcp://{}:{}".format(self.ip, self.port))
        except RuntimeError:
            print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
                   " Run with -h option for help.\n".format(self.ip, self.port))
            sys.exit(1)
            pass

        self.mem = self.session.service('ALMemory')
        self.listener = self.session.service("ALSpeechRecognition")

        self.listener.setLanguage('English')
        self.listener.subscribe("Story_Robot")
        self.listener.unsubscribe('Story_Robot')
        self.talker = self.session.service('ALTextToSpeech')
        self.talker.setParameter("defaultVoiceSpeed", 90)

    def say(self, text_to_say, voice='narrator', question=False):
        if voice == None:
            voice = 'narrator'

        if voice == 'evil':
            if NAO_MODE:
                self.audio_device.setOutputVolume(70)
        if FAST_MODE and not question and voice != 'evil':
            text_to_say = text_to_say[0:20]
        if NAO_MODE:
            # self.talker.setParameter("pitchShift", voices[voice])
            self.talker.setParameter("pitchShift", voices[voice])
            self.talker.say(text_to_say)
            self.audio_device.setOutputVolume(50)
        else: 
            print('{} voice: {}'.format(voice, text_to_say))
            print('---------------------------------------')

        
    def listen(self, keyphrase_sets):
        user_choice = None


        if NAO_MODE:
            vocab = [] 
            for keyphrase_set in keyphrase_sets:
                vocab.extend(keyphrase_set)

            #This creates a vocabulary for the speech recognition to look through
            self.listener.pause(True)
            time.sleep(0.1)
            self.listener.removeAllContext()
            print('vocab: {}'.format(vocab))
            self.listener.setVocabulary(vocab, True)
            self.listener.pause(False)

            #start recognition
            self.listener.subscribe(self.ip)
            print ('speech recognition engine started')
            self.mem = ALProxy("ALMemory", self.ip, 9559)
            self.mem.subscribeToEvent('WordRecognized', self.ip, 'wordRecognized')

            #Gives it time to process words said and or listen
            self.listener.pause(False)
            time.sleep(4)

            #stop recognition
            self.listener.unsubscribe(self.ip)

            #Hopefully this will print any recognized words
            data = self.mem.getData('WordRecognized')
            print("data: {}".format(data))
            user_response = data[0][6:-6]
            confidence = data[1]
            print("user response: {}".format(user_response))
            if confidence < 0.48:
                return None

            for keyphrase_set_i in range(len(keyphrase_sets)):
                if user_response in keyphrase_sets[keyphrase_set_i]:
                    return keyphrase_set_i
            
                    


      #      self.listener.setVocabulary(vocab, True)
            # Start the speech recognition engine with user Test_ASR
            self.listener.subscribe("Story_Robot")
            print('Speech recognition engine started')
            self.listener.pause(False)
            time.sleep(5)
            self.listener.unsubscribe("Story_Robot")
            print('I recognized:')
            print(self.mem.getData('WordRecognized'))

        else:
            user_response = raw_input().lower()
#            print("raw response: {}".format(user_response))
#            for keyphrase_set_i in range(len(keyphrase_sets)):
#                if user_response in keyphrase_sets[keyphrase_set_i]:
#                    # might also want to check if any words overlap between the user input 
#                    # and the actual keyphrase
#                    # set the choice that the user made to be equal to 
#                    user_choice = keyphrase_set_i  
            for keyphrase_set_i in range(len(keyphrase_sets)):
                if user_response in keyphrase_sets[keyphrase_set_i]:
                    return keyphrase_set_i
        
    def read_story_yaml(self, story_filepath):
        with open(story_filepath, 'r') as sf:
            self.story = yaml.load(sf, Loader = yaml.FullLoader)

    def get_keyphrase_sets(self, current_id): 
        keyphrase_sets = []
        for option in range(len(self.story[current_id]['options'])):
            keyphrase_sets.append(self.story[current_id]['options'][option]['keyphrases'])
            print("option {} is {}".format(option, self.story[current_id]['options'][option]['keyphrases']))
        return keyphrase_sets

    def tell_story(self):
    #    current_id = 'intro'
        current_id = start_node

        while True:
            if current_id == "exit":
                return
            # read the story
            print('read {} lines'.format(len(self.story[current_id]['lines'])))
            ble = True 
            for line in self.story[current_id]['lines']:
                self.say(line['text'], line['voice'])

            while True:  # loop util it gets a response, we might want to do this differently 
                if 'question' not in self.story[current_id].keys():
                    current_id = self.story[current_id]['options'][0]['target']
                    ble = False 
                    break
                    
                self.say(self.story[current_id]['question'], 'narrator', True)

                # each option has a set of keyphrases associated with it
                # extract the sets of keyphrases from the options, retaining their same 
                # order and structure
                keyphrase_sets = self.get_keyphrase_sets(current_id)
                user_choice = self.listen(keyphrase_sets) 

                if user_choice != None:
                    if self.story[current_id]['options'][user_choice]['target'] == "exit":
                        return 
                    break
                    

                self.say('THAT\'S NOT AN OPTION... please try again', 'evil')
            # the target of the option stores the node that we go to if the user chooses this option 
            #print("current id: {}".format(current_id))
            #print("user choice : {}".format(user_choice))
            #print("target value: {}".format(self.story[current_id]['options'][user_choice]['target']))
            if ble:
                current_id = self.story[current_id]['options'][user_choice]['target']


if __name__ == "__main__":
    test_brain = RobotBrain() 
    #test_brain.read_story_yaml('full_story.yaml')
#    test_brain.read_story_yaml(argv[1])
    test_brain.tell_story()

