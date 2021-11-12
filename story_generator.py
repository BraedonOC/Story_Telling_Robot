import yaml

def write_to_yaml(story_dict):
    yaml.dump(story_dict)


def create_node():
    print("Creating Story Node")
    node = {"lines" : [], "question" : "", 'options' : []}
    while True:
        line_dict = {}
        line_dict["text"] = input("Input the line you would like the robot to say:")
        if line_dict["text"] == "":
            print("cannot have no text associated with the line please try again better")
            continue
        line_dict["voice"] = input("What voice should this line use?  (enter nothing for narrator)")
        line_dict["gesture"] = input("What gesture would you like during this line?")
        if line_dict["voice"] == "":
            print("setting voice to be default narrator")
            line_dict["voice"] = narrator
        if line_dict["gesture"] == "":
            print("setting gesture to be default gesture")
            line_dict["gesture"] = narrator
        node["lines"].append(line_dict)
        if input("Would you like to enter another line? y/n").toupper() != "Y":
            break

    # loop until a question is provided  
    while node["question"] == "":
        node["question"] = input("What is the question associated with this node?")

    while True:
        next_node_number += 1
        target = input(f"target for option {next_node_number}")




    
    





