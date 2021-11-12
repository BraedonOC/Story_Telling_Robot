import yaml


story = {}
node_name_map = {}
next_node_number = 1

def write_story_to_yaml(story_name):
    with open(f"{story_name}.yaml", "w") as f:
        yaml.dump(story, f)

def print_node_names(node_id_list):
    for node_id in node_id_list:
        try:
            print(f"{node_id}: {node_name_map[node_id]}")
        except KeyError:
            try:
                print(f"{node_id}: {story[node_id]['question']}")
            except KeyError:
                print(f"{node_id} : {story[node_id]['lines'][0]['text'][0:20]} (No question)")

def create_node():
    global story
    global node_name_map
    global next_node_number
    node = {"lines" : [], "question" : "", 'options' : []}
    print("..................................")
    print("          Write Lines")
    print("..................................")
    while True:
        line_dict = {}
        print("Input the line you would like the robot to say: ")
        line_dict["text"] = input("")
        if line_dict["text"] == "":
            print("cannot have no text associated with the line please try again better")
            continue
        line_dict["voice"] = input("What voice should this line use?  (enter nothing for narrator): ")
        line_dict["gesture"] = input("What gesture would you like during this line? (enter nothing for idle): ")
        if line_dict["voice"] == "":
            print("setting voice to be default narrator")
            line_dict["voice"] = "narrator"
        if line_dict["gesture"] == "idle":
            print("setting gesture to be default gesture")
            line_dict["gesture"] = narrator
        node["lines"].append(line_dict)
        if input("Would you like to enter another line? y/n  ").upper() != "Y":
            break

    # loop until a question is provided  
    print("..................................")
    print("        Create Question")
    print("..................................")

    print()
    print("What is the question associated with this node?")
    node["question"] = input()
    if node["question"] == "":
        node.pop("question")

    # loop for creating options
    print("..................................")
    print("        Create Options")
    print("..................................")
    while True:
        option = {'target' : '', 'keyphrases' : []}
        target_node_id = -1
        # loop for getting input from user for the target 
        while True:
            print("Which node would you like this option to bring the story to?")
            print("To list the current nodes type 'list' and then 'enter'")
            print("If you want this option to lead to a new node, type 'new' and then hit 'enter'")
            user_option = input()
            if user_option.upper() == 'LIST':
                print_node_names(story.keys())
            elif user_option.upper() == 'NEW':
                node_name = input("Enter name or note associated with this node (doesn't need to be unique): ")
                node_name_map[next_node_number] = node_name
                option["target"] = node_name
                target_node_id = next_node_number
                next_node_number += 1
                break
            else:
                target_node_id = user_option
                try:
                    target_node_id = int(user_option)
                except:
                    pass
                if target_node_id not in story.keys():
                    print("That node hasn't been created yet, if you would like to add a new node type 'new'")
                option["target"] = target_node_id 
                break

        if "question" not in node.keys():
            node["options"].append(option)
            break

        while True:
            print(f"Add a keyphrase associated with this answer or hit 'enter' to finish writing keyphrase")
            print(f"already added keyphrases: {option['keyphrases']}")
            keyphrase_response = input()
            if keyphrase_response == '':
                break
            else:
                option['keyphrases'].append(keyphrase_response)

        node["options"].append(option)
        if input("Would you like to add another option? y/n ").upper() != "Y":
            break
    return node

def find_empty_references():
    empty_references = []
    for key in story.keys():
        try:
            for option in story[key]["options"]:
                if option["target"] not in story.keys():
                    empty_references.append(option["target"])
        except KeyError:
            print(f"node {key} caused an error")


    empty_references = list(dict.fromkeys(empty_references))
    return empty_references

def create_story_node(): 
    global new_node_id
    while True:
        empty_references = find_empty_references()
        print("Would you like to create a new node or fill in an option? y/n ")
        print("Current nodes that are referenced but don't exist yet: ")
        print(empty_references)
        print("To create one of these nodes type its number, to create a new node type 'new'")
        user_node_input = input()

        if user_node_input.upper() == "NEW" or user_node_input.upper() == "":
            new_node_id = next_node_number
            next_node_number += 1
            story[new_node_id] = create_node()
            return new_node_id

        try:
            int_id = int(user_node_input)
            user_node_input = int_id
        except:
            pass
        new_node_id = user_node_input
        if user_node_input not in empty_references:
            print("That isn't an empty reference!!!")
            print("Starting over node creation because I'm lazy")
            continue

        story[new_node_id] = create_node()
        return new_node_id


def create_story(file_to_load = None):
    global story
    print(" ________  _________  ________  ________      ___    ___       ___    ___ ________  _____ ______   ___       ___  ________  _______   ________     ")
    print("|\   ____\|\___   ___\\   __  \|\   __  \    |\  \  /  /|     |\  \  /  /|\   __  \|\   _ \  _   \|\  \     |\  \|\_____  \|\  ___ \ |\   __  \    ")
    print("\ \  \___|\|___ \  \_\ \  \|\  \ \  \|\  \   \ \  \/  / /     \ \  \/  / | \  \|\  \ \  \\\__\ \  \ \  \    \ \  \\|___/  /\ \   __/|\ \  \|\  \  ") 
    print(" \ \_____  \   \ \  \ \ \  \\\  \ \   _  _\   \ \    / /       \ \    / / \ \   __  \ \  \\|__| \  \ \  \    \ \  \   /  / /\ \  \_|/_\ \   _  _\ ") 
    print("  \|____|\  \   \ \  \ \ \  \\\  \ \  \\  \|   \/  /  /         \/  /  /   \ \  \ \  \ \  \    \ \  \ \  \____\ \  \ /  /_/__\ \  \_|\ \ \  \\  \|") 
    print("    ____\_\  \   \ \__\ \ \_______\ \__\\ _\ __/  / /         __/  / /      \ \__\ \__\ \__\    \ \__\ \_______\ \__\\________\ \_______\ \__\\ _\ ")
    print("   |\_________\   \|__|  \|_______|\|__|\|__|\___/ /         |\___/ /        \|__|\|__|\|__|     \|__|\|_______|\|__|\|_______|\|_______|\|__|\|__|")
    print("   \|_________|                             \|___|/          \|___|/                                                                               ")
    print("\n\n")

    if file_to_load != 0:
        with open(file_to_load, 'r') as f:
            story = yaml.load(f, Loader=yaml.FullLoader)
        next_node_number = len(story.keys()) + 1
        print(f"Loaded file with {next_node_number  - 1} nodes")

    while True:
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        print("         Creating Story Node           ")
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        create_story_node()
        print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        print("      Node Creation Complete")
        print("Would you like to create another node? y/n ")
        user_response = input()
        if user_response.upper() == "Y":
            continue
        break

    write_story_to_yaml("full_story_test")

create_story("stories/fuller_story.yaml")

