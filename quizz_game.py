from random import randint

### Hardcoded data
level_1 = [["Cho Chang", "Ravenclaw"], ["Gregory Goyle", "Slytherin"],["Angelina Johnson", "Gryffindor"],["Neville Longbottom", "Gryffindor"],["Luna Lovegood", "Ravenclaw"],["Remus Lupin", "Gryffindor"],["Draco Malfoy", "Slytherin"],["Harry Potter", "Gryffindor"],["Fred Weasley", "Gryffindor"],["George Weasley", "Gryffindor"],["Ginny Weasley", "Gryffindor"],["Ron Weasley", "Gryffindor"],["Hermione Granger", "Gryffindor"],["Cedric Diggory", "Hufflepuff"]]
level_2 = ""
level_3 = ""
level_4 = ""
level_5 = [["Alabama","Montgomery"],["Alaska","Juneau"],["Arizona","Phoenix"],["Arkansas","Little Rock"],["California","Sacramento"],["Colorado","Denver"],["Connecticut","Hartford"],["Delaware","Dover"],["Florida","Tallahassee"],["Georgia","Atlanta"],["Hawaii","Honolulu"],["Idaho","Boise"],["Illinois","Springfield"],["Indiana","Indianapolis"],["Iowa","Des Moines"],["Kansas","Topeka"],["Kentucky","Frankfort"],["Louisiana","Baton Rouge"],["Maine","Augusta"],["Maryland","Annapolis"],["Massachusetts","Boston"],["Michigan","Lansing"],["Minnesota","Saint Paul"],["Mississippi","Jackson"],["Missouri","Jefferson City"],["Montana","Helena"],["Nebraska","Lincoln"],["Nevada","Carson City"],["New Hampshire","Concord"],["New Jersey","Trenton"],["New Mexico","Santa Fe"],["New York","Albany"],["North Carolina","Raleigh"],["North Dakota","Bismarck"],["Ohio","Columbus"],["Oklahoma","Oklahoma City"],["Oregon","Salem"],["Pennsylvania","Harrisburg"],["Rhode Island","Providence"],["South Carolina","Columbia"],["South Dakota","Pierre"],["Tennessee","Nashville"],["Texas","Austin"],["Utah","Salt Lake City"],["Vermont","Montpelier"],["Virginia","Richmond"],["Washington","Olympia"],["West Virginia","Charleston"],["Wisconsin","Madison"],["Wyoming","Cheyenne"]]

levels = [1, 2, 3, 4, 5]
levels_array = [level_1,level_2,level_3,level_4,level_5]

### Functions
def ask_level():
    print "What level, would you like to play today?\n"
    level_number = 0
    while level_number not in levels:
        level_number = raw_input("Please enter a number between '1' and '5'.\n")
        try:
            int(level_number)
        except ValueError:
            print "That does not look like a number, does it?\n"
            level_number = 0
        level_number = int(level_number)
    return level_number

def ask_error():
    error_number = u""
    while not error_number.isnumeric():
        error_number = unicode(raw_input("How many errors before I fail you?\n")) #turn into unicode is required by isnumeric method
        try:
            int(error_number)
        except ValueError:
            print "Please enter a number, a NUMBER, you know, digits :)\n"
    print error_number
    return int(error_number)

def get_random_num(max_num):
    return randint(0,max_num)


def play_quiz_level(level_data_string, err_allowed, ask_user_question):
    # get random 15 numbers to play
    correct = 0
    errors = 0
    max = len(level_data_string) - 1
    play_array = []

    while len(play_array) <= 3: # the amount of things to play
        num = get_random_num(max)
        if num not in play_array:
            play_array.append(num)
    print play_array

    # play the level

    for number in play_array:
        question = level_data_string[number][0]
        answer = level_data_string[number][1]

        user_answer = raw_input(ask_user_question + " " + str(question) + "?\n")

        if answer.lower() == user_answer.lower():
            correct += 1
        else:
            errors += 1

        if errors > err_allowed:
            print "Sorry, you made " + str(errors) + " mistakes. GAME OVER!"
            return False
        print question, answer, user_answer

    win = "Great game! You made " + str(errors) + " mistakes, and guessed " + str(correct) + "! You ROCK.\n"
    print win
    return True

#TODO: check if rand takes the last digit as well! so it takes all 50 states and o10 to play

        # ask how many failed attempts per this level are allowed
        # count the failed attempts
        # reset fails on next levels
        # ask user if they want to play next level and ask for allowed attamps, taking enter = "" as same as before

        # Level 5, randomly pick 15 US capital cities
        # as hardest level, play one of the quizzes with 1 error allowed
        # maybe check for no input ?

# PLAY THE ACTUAL GAME
def play_game():
    levels_coded = len(levels)
    welcome_msg = "Welcome to the THERE ARE WRONG ANSWERS quiz!\nThere are some crazy fun stuff waiting for you.\nWe have " + str(levels_coded) + " levels waiting for you."
    print welcome_msg
    level = ask_level()
    print "Thank you! Here it comes..."

    while level <= levels_coded:
        if level == 1:
            print "There are 4 houses in Harry Potter series."
            print "Ravenclaw,", "Slytherin,", "Gryffindor", "and Hufflepuff"
            print "One more thing..."
            game = play_quiz_level(level_1, ask_error(), "What is the house of")
            if game:
                print "-------------"
                print "onto level 2...."
                level = 2
            else:
                break
        elif level == 2:
            game = play_quiz_level(level_5, ask_error(), "What is the house of")
            if game:
                print "-------------"
                print "onto level 3...."
                level = 3
            else:
                break
        elif level == 3:
            game = play_quiz_level(level_5, ask_error(), "What is the capital city of")
            if game:
                print "-------------"
                print "onto level 4...."
                level = 4
            else:
                break
        elif level == 4:
            game = play_quiz_level(level_5, ask_error(), "What is the capital city of")
            if game:
                print "-------------"
                print "onto level 5...."
                level = 5
            else:
                break
        elif level == 5:
            game = play_quiz_level(level_5, ask_error(), "What is the capital city of")
            if game:
                print "YOU WON IT ALL!!!"
            break

play_game()