from random import randint

### Hardcoded playing data
level_1 = [["Cho Chang", "Ravenclaw"], ["Gregory Goyle", "Slytherin"],["Angelina Johnson", "Gryffindor"],["Neville Longbottom", "Gryffindor"],["Luna Lovegood", "Ravenclaw"],["Remus Lupin", "Gryffindor"],["Draco Malfoy", "Slytherin"],["Harry Potter", "Gryffindor"],["Fred Weasley", "Gryffindor"],["George Weasley", "Gryffindor"],["Ginny Weasley", "Gryffindor"],["Ron Weasley", "Gryffindor"],["Hermione Granger", "Gryffindor"],["Cedric Diggory", "Hufflepuff"]]
level_2 = [["Vogue","Madonna"],["Gonna Make You Sweat (Everybody Dance Now)","C&C Music Factory feat. F. Williams"],["Finally","Ce Ce Peniston"],["The Power","SNAP!"],["Baby Got Back","Sir Mix-A-Lot"],["Whoomp! There It Is","Tag Team"],["Show Me Love","Robin S."],["Groove Is In the Heart","Deee-Lite"],["Love Shack","The B-52s"],["Missing (Todd Terry mix)","Everything But the Girl"],["Unbelievable","EMF"],["I Like To Move It","Real 2 Real feat. The Mad Stuntman"],["Gettin' Jiggy Wit It","Will Smith"],["U Can't Touch This","MC Hammer"],["Get Ready For This","2 Unlimited"],["Good Vibrations","Marky Mark and The Funky Bunch feat. Loleatta Holloway"],["Believe (Life After Love)","Cher"],["Black Or White","Michael Jackson"],["Love Will Never Do (Without You)","Janet Jackson"],["Another Night","MC Sar and The Real McCoy"],["Touch Me (All Night Long)","Cathy Dennis"],["Rhythm is a Dancer","SNAP!"],["What Is Love?","Haddaway"],["Mr. Vain","Culture Beat"],["All That She Wants","Ace of Base"],["Be My Lover","La Bouche"],["I've Been Thinking About You","Londonbeat"],["This Is Your Night","Amber"],["Rhythm of the Night","Corona"],["C'mon N Ride It (The Train)","Quad City DJs"],["100% Pure Love","Crystal Waters"],["I'm Gonna Get You","Bizarre Inc. feat. Angie Gold"],["All Around the World","Lisa Stansfield"],["Strike It Up","Black Box"],["Everybody Everybody","Black Box feat. Martha Wash"],["Boom Boom Boom","The Outhere Brothers"],["We Like To Party","The Venga Boys"],["Here Comes the Hotstepper (Heartical mix)","Ini Kamoze"],["Tootsee Roll","69 Boyz"]]
level_3 = [["Hamburger SV", "Germany"],["FC Nurnberg", "Germany"],["Borussia Dortmund", "Germany"],["Berliner FC Dynamo", "Germany"],["FC Carl Zeiss Jena", "Germany"],["SG Dynamo Dresden", "Germany"],["FC Lokomotive Leipzig", "Germany"],["SV Werder Bremen", "Germany"],["Eintracht Frankfurt", "Germany"],["FC Bayern Munchen", "Germany"],["VfB Stuttgart", "Germany"],["Bologna FC","Italy"],["Juventus FC","Italy"],["SSC Napoli","Italy"],["FC Internazionale Milano","Italy"],["AS Roma","Italy"],["ACF Fiorentina","Italy"],["Atalanta BC","Italy"],["Hellas Verona FC","Italy"],["AC Milan","Italy"],["UC Sampdoria","Italy"],["Malmo FF","Sweden"],["Osters IF","Sweden"],["IFK Goteborg","Sweden"],["IFK Norrkoping","Sweden"],["IK Brage","Sweden"],["Athlitiki Enosi Larissas FC", "Greece"],["Panathinaikos AO", "Greece"],["PAOK", "Greece"],["AEK FC", "Greece"],["FC Nantes", "France"],["AS Cannes", "France"],["Niort FC", "France"],["AS Monaco", "France"],["FC Metz", "France"],["FC Girondins de Bordeaux", "France"],["Montpellier HSC", "France"],["Olympique de Marseille", "France"],["AS Saint-Etienne", "France"],["FC Sochaux", "France"],["AJ Auxerre", "France"]]
level_4 = [["Austria","Vienna"],["Belarus","Minsk"],["Belgium","Brussels"],["Bulgaria","Sofia"],["Croatia","Zagreb"],["Cyprus","Nicosia"],["Denmark","Copenhagen"],["Estonia","Tallinn"],["Finland","Helsinki"],["France","Paris"],["Germany","Berlin"],["Greece","Athens"],["Hungary","Budapest"],["Iceland","Reykjavik"],["Ireland","Dublin"],["Italy","Rome"],["Latvia","Riga"],["Liechtenstein","Vaduz"],["Lithuania","Vilnius"],["Luxembourg","Luxembourg"],["Macedonia","Skopje"],["Malta","Valletta"],["Moldova","Chisinau"],["Monaco","Monaco"],["Montenegro","Podgorica"],["Netherlands","Amsterdam"],["Norway","Oslo"],["Poland","Warsaw"],["Portugal","Lisbon"],["Romania","Bucharest"],["Russia","Moscow"],["San Marino","San Marino"],["Serbia","Belgrade"],["Slovakia","Bratislava"],["Slovenia","Ljubljana"],["Spain","Madrid"],["Sweden","Stockholm"],["Switzerland","Bern"],["Turkey","Ankara"],["Ukraine","Kyiv"]]
level_5 = [["Alabama","Montgomery"],["Alaska","Juneau"],["Arizona","Phoenix"],["Arkansas","Little Rock"],["California","Sacramento"],["Colorado","Denver"],["Connecticut","Hartford"],["Delaware","Dover"],["Florida","Tallahassee"],["Georgia","Atlanta"],["Hawaii","Honolulu"],["Idaho","Boise"],["Illinois","Springfield"],["Indiana","Indianapolis"],["Iowa","Des Moines"],["Kansas","Topeka"],["Kentucky","Frankfort"],["Louisiana","Baton Rouge"],["Maine","Augusta"],["Maryland","Annapolis"],["Massachusetts","Boston"],["Michigan","Lansing"],["Minnesota","Saint Paul"],["Mississippi","Jackson"],["Missouri","Jefferson City"],["Montana","Helena"],["Nebraska","Lincoln"],["Nevada","Carson City"],["New Hampshire","Concord"],["New Jersey","Trenton"],["New Mexico","Santa Fe"],["New York","Albany"],["North Carolina","Raleigh"],["North Dakota","Bismarck"],["Ohio","Columbus"],["Oklahoma","Oklahoma City"],["Oregon","Salem"],["Pennsylvania","Harrisburg"],["Rhode Island","Providence"],["South Carolina","Columbia"],["South Dakota","Pierre"],["Tennessee","Nashville"],["Texas","Austin"],["Utah","Salt Lake City"],["Vermont","Montpelier"],["Virginia","Richmond"],["Washington","Olympia"],["West Virginia","Charleston"],["Wisconsin","Madison"],["Wyoming","Cheyenne"]]

levels = [level_1,level_2,level_3,level_4,level_5]
levels_numeric = [1,2,3,4,5]
levels_coded = len(levels) # how many levels
display_start_text = ["There are 4 houses in Harry Potter series.\nRavenclaw, Slytherin, Gryffindor and Hufflepuff\nOne more thing...", "Let's live through the 90's again!", "Let's play some soccer.", "Let's guess some European cities capitals!", "Let's guess some US states capitals!"]
quiz_question = ["What is the house of", "Who sings this song:", "What country is this club from:", "What is the capital city of", "What is the capital city of"]

# Hardcoded game variables
# These data can be changed accordingly to play the game a bit differently
# number of things to guess in a level (it is the same for all levels and limited by length of shortest level
# uncomment the lines to check the length of your data
# print len(level_1)
# print len(level_2)
# print len(level_3)
# print len(level_4)
# print len(level_5)
global_max_play_array = 14
welcome_msg = "Welcome to the THERE ARE WRONG ANSWERS quiz!\nThere are some crazy fun stuff waiting for you.\nWe have " + str(levels_coded) + " levels waiting for you."


### Functions
def ask_level():
    '''
    input: ask user for the desired starting level
    output: user given level
    '''
    print "What level, would you like to play today?\n"
    level_number = 0
    while level_number not in levels_numeric:
        level_number = raw_input("Please enter a number between '1' and '5'.\n")
        try:
            int(level_number)
        except ValueError:
            print "That does not look like a number, does it?\n"
            level_number = 0
        level_number = int(level_number)
    return level_number

def ask_error():
    '''
    There are no limits to the error
    input: ask user for the errors they want to be allowed to make
    output: user given errors
    '''
    error_number = u""
    while not error_number.isnumeric():
        error_number = unicode(raw_input("How many total errors to fail level? Question always has 3 tries.\n")) #turn into unicode is required by isnumeric method
        try:
            int(error_number)
        except ValueError:
            print "Please enter a number, a NUMBER, you know, digits :)\n"
    return int(error_number)

def get_random_num(max_num):
    '''
    input: takes max value
    output: generates random value
    '''
    return randint(0,max_num)

def generate_level_array(level_data_string, num_things_to_guess):
    '''
    inputs:
    :param level_data_string: array with data to play in a level
    :param num_things_to_guess: how many elements will be needed in the game
    :return: array with randomly generated numbers to be used to pull QnA to play level
    '''
    play_array = []
    max_play_number = len(level_data_string) - 1
    max_play_array = num_things_to_guess

    while len(play_array) < max_play_array:
        num = get_random_num(max_play_number)
        if num not in play_array:
            play_array.append(num)
    return play_array

def play_level(level_data_string, err_allowed, ask_user_question, welcome_text, num_things_to_guess):
    '''
    function responsible for playing one level
    inputs: level data, errors allowed, and the text displayed to the user
    output: Boolean if the level is pass or fail, and errors made during this level
    '''
    # get random X numbers to play
    correct = 0
    total_errors = 0
    question_location = 0
    answer_location = 1
    play_array = generate_level_array(level_data_string, global_max_play_array)
    print welcome_text

    # play the level

    for problem in play_array:
        question = level_data_string[problem][question_location]
        answer = level_data_string[problem][answer_location]
        current_question_error = 0
        max_question_error = 3 # how many times can user try one question

        while current_question_error < max_question_error:
            user_answer = raw_input(ask_user_question + " " + str(question) + "\n")

            if answer.lower() == user_answer.lower():
                correct += 1
                break
            else:
                total_errors += 1
                current_question_error += 1

            if total_errors > err_allowed or current_question_error >= max_question_error:
                print "You got this question wrong " + str(current_question_error) + " times. And made " + str(total_errors) + " total mistakes. GAME OVER!"
                return False, total_errors

    win = "Great level! You made " + str(total_errors) + " total mistakes, and guessed " + str(correct) + " questions!\n"
    print win
    return True, total_errors # go to next level, keep number of total running errors



# PLAY THE ACTUAL GAME
def play_game():
    '''
    logic for playing the game encapsulated in a function
    inputs: none
    outputs: game text
    '''
    print welcome_msg
    level = ask_level()  # ask initial level
    total_errors = 0

    print "Thank you! Here it comes..."

    while level <= levels_coded:

        game, level_errors = play_level(levels[level-1], ask_error(), quiz_question[level-1], display_start_text[level-1], global_max_play_array)
        total_errors += level_errors
        if game and level < 5:
            level += 1
            print "-------------\nonto next level ....\n-------------"
        elif game and level == 5:
            print "YOU WON! You made " + str(total_errors) + " total errors."
            level += 1
        else:
            break

play_game()