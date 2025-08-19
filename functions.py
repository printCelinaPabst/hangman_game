import json
import os


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

# Determines the path to the 'data' directory, relative to the current Python file.
# This ensures platform-independent access to local resources.
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

# Defines the path to the 'words_collection.json' file located in the 'data' directory.
# This file contains the word collection used for reading or writing operations within the application.
WORDS_FILE = os.path.join(DATA_DIR, "words_collection.json")

# function to save words to json
def save_words():
    try:
        """try loading existing data from words_collection.json file"""
        with open(WORDS_FILE, "r") as f:
            data = json.load(f)

    except FileNotFoundError:
        """if the file does not exist, initialize empty lists"""
        data = {"easy": [], "mid": [], "hard": []}

    # add words to empty lists and then extend to the JSON structure
    data["easy"].extend(easy_words)
    data["mid"].extend(mid_words)
    data["hard"].extend(hard_words)

    # Remove duplicate entries in each category
    for key in data:
        data[key] = list(set(data[key]))

    #sort each category
    data["easy"].sort()
    data["mid"].sort()
    data["hard"].sort()

    # save the updated data back to the json file
    with open(WORDS_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print("saved to JSON file.")
#-----------------------------------

# load words from JSON file 
def get_words():
    try:
        with open(WORDS_FILE, "r") as f:
            data = json.load(f)
        return data["easy"], data["mid"], data["hard"]
    except FileNotFoundError:
        print("File not found. Check path or generate the JSON first.")
        return [], [], []

#######----------use funtions here to save words------------####

#add_easy()
#add_mid()
#add_hard()

save_words() #dont forget to save 