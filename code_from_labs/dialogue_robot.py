#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Using ALDialog Methods"""

import qi
import argparse
import sys

def main(session):
    """
    This example uses ALDialog methods.
    It's a short dialog session with two topics.
    """
    # Getting the service ALDialog
    ALDialog = session.service("ALDialog")
    ALDialog.setLanguage("English")

    # writing topics' qichat code as text strings (end-of-line characters are important!)

    test_content = '' 
    
    with open('test_dialogue.txt', 'r') as f:
        for line in f:
            test_content += line


    print(test_content)

    # Loading the topics directly as text strings
    test_topic_name = ALDialog.loadTopicContent(test_content)

    # Activating the loaded topics
    ALDialog.activateTopic(test_topic_name)

    # Starting the dialog engine - we need to type an arbitrary string as the identifier
    # We subscribe only ONCE, regardless of the number of topics we have activated
    ALDialog.subscribe('my_dialog_example')

    try:
        raw_input("\nSpeak to the robot using rules from both the activated topics. Press Enter when finished:")
    finally:
        # stopping the dialog engine
        ALDialog.unsubscribe('my_dialog_example')

        # Deactivating all topics
        ALDialog.deactivateTopic(test_topic_name)

        # now that the dialog engine is stopped and there are no more activated topics,
        # we can unload all topics and free the associated memory
        ALDialog.unloadTopic(test_topic_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="138.67.205.108",
                        help="Robot's IP address. If on a robot or a local Naoqi - use '127.0.0.1' (this is the default value).")
    parser.add_argument("--port", type=int, default=9559,
                        help="port number, the default value is OK in most cases")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://{}:{}".format(args.ip, args.port))
    except RuntimeError:
        print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
               " Run with -h option for help.\n".format(args.ip, args.port))
        sys.exit(1)
    main(session)
