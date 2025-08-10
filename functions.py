import json


# Empty lists for word categories based on difficulty level
easy_words = []
mid_words = []
hard_words = []


# add words to easy_words list
def add_easy(*word):
    easy_words.extend(word)


# add words to mid_words list   
def add_mid(*word):
    mid_words.extend(word)


# add words to hard_words list   
def add_hard(*word):
    hard_words.extend(word)

#--------------------------------

# Define the filename to store the words in JSON format
DATEI = "words_collection.json"

# function to save words to json
def save_words():
    try:
        # try loading existing data from JSON file
        with open(DATEI, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        # if the file does not exist, initialize empty lists
        data = {"easy": [], "mid": [], "hard": []}

    # add words from current word_lists to the JSON structure
    data["easy"].extend(easy_words)
    data["mid"].extend(mid_words)
    data["hard"].extend(hard_words)

    # Remove duplicate entries in each category
    for key in data:
        data[key] = list(set(data[key]))
    #sort each category

    # save the updated data back to the json file
    with open(DATEI, "w") as f:
        json.dump(data, f, indent=4)
    print("saved to JSON file.")
#-----------------------------------

# load words from JSON file 
def get_words():
    try:
        with open(DATEI, "r") as f:
            data = json.load(f)
        return data["easy"], data["mid"], data["hard"]
    except FileNotFoundError:
        print("File not found. Check path or generate the JSON first.")
        return [], [], []

#######----------use funtions here to save words------------####

#add_easy()
#add_mid()
#add_hard)

#save_words() #dont forget to save 