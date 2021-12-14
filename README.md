# Story Telling Robot
This repository contains the code for a robot that tells an interactive "choose your own adventure story".
The code was developed by group 2B for CSCI 436.

## Robot Usage
To use this code it's important to have the Python NAO SDK properly installed and configured.  
Once the SDK is configured you should be able to use our code by running:
`python2 story_telling_robot --ip <ip address of NAO>`
By default, our robot will tell the story that we wrote, however this can be changed by using the `--story` flag.

## Story Generator Usage
In order to use the story generator Python3 is required.
The generator can be launched by using the command:
`python3 story_yamlizer.py <path to story file>`
The story yamlizer will then walk you through creating a story and you should just need to follow the prompts.


