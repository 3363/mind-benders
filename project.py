from random import randint

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

level_0 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

level_1 = ""
level_2 = ""
level_3 = ""
level_4 = ""
level_5 = [["Alabama","Montgomery"],["Alaska","Juneau"],["Arizona","Phoenix"],["Arkansas","Little Rock"],["California","Sacramento"],["Colorado","Denver"],["Connecticut","Hartford"],["Delaware","Dover"],["Florida","Tallahassee"],["Georgia","Atlanta"],["Hawaii","Honolulu"],["Idaho","Boise"],["Illinois","Springfield"],["Indiana","Indianapolis"],["Iowa","Des Moines"],["Kansas","Topeka"],["Kentucky","Frankfort"],["Louisiana","Baton Rouge"],["Maine","Augusta"],["Maryland","Annapolis"],["Massachusetts","Boston"],["Michigan","Lansing"],["Minnesota","Saint Paul"],["Mississippi","Jackson"],["Missouri","Jefferson City"],["Montana","Helena"],["Nebraska","Lincoln"],["Nevada","Carson City"],["New Hampshire","Concord"],["New Jersey","Trenton"],["New Mexico","Santa Fe"],["New York","Albany"],["North Carolina","Raleigh"],["North Dakota","Bismarck"],["Ohio","Columbus"],["Oklahoma","Oklahoma City"],["Oregon","Salem"],["Pennsylvania","Harrisburg"],["Rhode Island","Providence"],["South Carolina","Columbia"],["South Dakota","Pierre"],["Tennessee","Nashville"],["Texas","Austin"],["Utah","Salt Lake City"],["Vermont","Montpelier"],["Virginia","Richmond"],["Washington","Olympia"],["West Virginia","Charleston"],["Wisconsin","Madison"],["Wyoming","Cheyenne"]]

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

# Ask for level from user

levels = [1, 2, 3, 4, 5]

def ask_level():
    print "What level, would you like to play today?"
    level_number = 0
    while level_number not in levels:
        level_number = raw_input("Please enter a number between '1' and '5'.  ")
        try:
            int(level_number)
        except ValueError:
            print "That does not look like a number, does it?"
            level_number = 0
        level_number = int(level_number)
    return level_number

def ask_error():
    error_number = u""
    while not error_number.isnumeric():
        error_number = unicode(raw_input("How many errors before I fail you?  ")) #turn into unicode is required by isnumeric method
        try:
            int(error_number)
        except ValueError:
            print "Please enter a number, a NUMBER, you know, digits :)"
        try:
            int(error_number) < 7
        except ValueError:
            print "Let's not go overboard!"
    return int(error_number)

level = ask_level()
errors_allowed = ask_error()

print level
print errors_allowed

def get_random_num(max_num):
    return randint(0,max_num)


def play_quiz_level(level_data_string):
    # get random 15 numbers to play
    max = len(level_data_string)
    play_array = []

    while len(play_array) <= 10:
        num = get_random_num(max)
        if num in play_array:
            num = get_random_num(max)
        play_array.append(num)

    return play_array

    replaced = "".join(replaced)


#TODO: check if rand takes the last digit as well! so it takes all 50 states and o10 to play

        # ask how many failed attempts per this level are allowed
        # count the failed attempts
        # reset fails on next levels
        # ask user if they want to play next level and ask for allowed attamps, taking enter = "" as same as before

        # Level 5, randomly pick 15 US capital cities

print play_quiz_level(level_5)