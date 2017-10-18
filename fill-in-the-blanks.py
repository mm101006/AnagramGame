
# ======================================================================================
                        # Functions Section
# function flow: player_name ---> attempts ----> main() --> start_game() --> Easy Medium or Hard() --> play_game --> check_for_match --> guess-word --> word_in_pos --> user_attempts

# ======================================================================================
# player_name function asks for the user's name 
def player_name(): 
    print """So you want to play a game....
    But first who am I playing with?"""
    
    name = ""
    
    while name.isalpha() == False or len(name) <= 1:
        name = raw_input("What is your name? ").title()

        if name.isalpha() == True and len(name) > 1:
            break
    return name

#this function asks the user how many attempts they would like to have before they have to start over.     
def attempts():
    tries = raw_input("How many attempts would you like before you lose? ")
    if tries == str(0):
        print "Well that is dumb!"
        attempts()
    else:
        while tries.isdigit() == False:
            tries = raw_input("How many attempts would you like before you lose? ")
        return int(tries)
    
# Main function starts the game, triggers the start_game function. Once start_game returns the difficulty, the corresponding difficulty level begins. 
def main():
    difficulty = start_game()
    if difficulty == 'Easy':
        easy()
        main()
    elif difficulty == "Medium":
        medium()       
        main()
    else:
        hard()

# The user then picks a difficulty which is returned to the main function.  
def start_game():
    print "What difficulty would you like to try? "
    response = ""
    while response not in {"Easy", "Medium", "Hard"}:
        response = raw_input("Please enter Easy, Medium, or Hard. ").title()
    return response
    
    
# The easy function when called triggers a series of comments and questions. 
# The function also returns the new phrase created when the blanks are filled in.  
def easy():
    print "Of course you would have selected easy. Anyways, let's begin:", "\n"
    print phrases[0]['fill_in_blank'], "\n"
    play_game(phrases[0], placeholder_for_blanks)
    print "\n", "Very good, off to the next one.", "\n"
    raw_input("Press Enter to continue..." + "\n")
    print phrases[1]['fill_in_blank'], "\n"
    play_game(phrases[1], placeholder_for_blanks)
    print "\n", "You are on a roll...Now on to the next one.", "\n"
    raw_input("Press Enter to continue..." + "\n")
    print phrases[2]['fill_in_blank'], "\n"
    play_game(phrases[2], placeholder_for_blanks)
    print "\n", "Waaaay to Go!!! Here is your last fill in the blank.", "\n"
    raw_input("Press Enter to continue..." + "\n")
    print phrases[3]['fill_in_blank'], "\n"
    play_game(phrases[3], placeholder_for_blanks)
    print "\n", "Congrats on finishing the game on easy. Shall we try a different difficulty?", "\n"

# The medium function when called basically does the same thing the easy function does.
def medium():
    print "Oh! Looks like, " + user + ", " "likes some adversity in your life. Anyways, lets begin." + "\n"
    print phrases[4]['fill_in_blank'], "\n"
    play_game(phrases[4], placeholder_for_blanks)
    print "\n", "Here we go again!!! Here is your last fill in the blank.", "\n"
    raw_input("Press Enter to continue..." + "\n")
    print phrases[5]['fill_in_blank'], "\n"
    play_game(phrases[5], placeholder_for_blanks)
    print "\n", "Congrats on finishing the game on medium. Shall we try a different difficulty?", "\n"

# The hard function when called basically does the same thing as the easy and medium function does.
def hard():
    print "Are you ready to be bamboozled? For this one you will not be given a particular word to solve. Instead this one requires you to use letters from the phrase to form a new phrase.", "\n"
    print phrases[6]['fill_in_blank'], "\n"
    play_game(phrases[6], placeholder_for_blanks)
    print "\n", "Congrats on finishing the game on hard. And now I will share a secret with you....", "\n"
    print """Eh, did I say secret, I meant quote: 'It was a common practice with the Talmudists to conceal 
    secret meanings and sounds of words by transposing the words. pg. 699 Morals and Dogma""" 
    quit()

# this function checks to see if the user has gone over the amount of attempts they have chosen, if so the game rerun the main function.  
def user_attempts(store_anagrams, store_solution, grab_next):
    user_attempts = 0
    user_input = raw_input("What is the anagram of " + store_anagrams[grab_next] + "? ").lower()
    while user_input != store_solution[grab_next]:
        if user_attempts < tries - 1:
            print "Please try again!"
            user_attempts += 1
            user_input = raw_input("What is the anagram of " + store_anagrams[grab_next] + "? ").lower()
        else: 
            print "You lose!"
            main()
    return user_input

# word_in_pos function is checking to see if the phrase has any matches in placeholder for blanks
def word_in_pos(word, placeholder_for_blanks):
    for pos in placeholder_for_blanks:
        if pos in word:
            return pos
    return None    

# Takes the expression and goes through each word checking to see if there is a match by calling the word_in_pos function. If there is a prompt asks the user to fill in the blank.  
# The function user_attempts is then called checking to see if the user has gone over their limit on tries. 
def guess_word(expression, store_anagrams, store_solution, replaced):
    grab_next = 0
    for word in expression:
        replacement = word_in_pos(word, placeholder_for_blanks)
        if replacement != None:
            find_word = expression.index(word)
            user_correct = user_attempts(store_anagrams, store_solution, grab_next)
            word = word.replace(replacement, user_correct)
            replaced.append(word)
            first_part = " ".join(replaced[:])
            second_part = " ".join(expression[find_word+1:])
            print "That is correct!"
            print "\n" + first_part + " " + second_part
            grab_next += 1
        else:
            replaced.append(word)
    
# word_in_pos function is spliting the expression by blank spaces. And then calls the function interchange_word. 
def check_for_match(expression, replaced, store_anagrams, store_solution):
    phrase = expression['fill_in_blank']
    expression = phrase.split()
    guess_word(expression, store_anagrams, store_solution, replaced)

# play_game function is retrieving the key words from the dictionary and then appends them into a list. The phrase from the dictionary is also being retrieved and then split up.
# the check_for_match function is then called. 
def play_game(expression, placeholder_for_blanks):
    word_to_anagram = expression['anagram']
    word_to_solution = expression['solution']
    store_anagrams = []
    for word in word_to_anagram:
        store_anagrams.append(word)
    store_solution = []
    for word in word_to_solution:
        store_solution.append(word)
    replaced = []
    check_for_match(expression, replaced, store_anagrams, store_solution)

# =====================================================================================
                        # Global Variables / Intro
# =====================================================================================
user = player_name()
tries = attempts()

print "Welcome, " + user + ",", """for this game I will give you a phrase, 
within that phrase will contain blanks that you have to return the anagagram for.
Be aware that there could be multiple possibilities for each keyword. 
For this game I am looking for one particular anagram of the missing word. 
This game will be weird, and how weird it gets depends on the difficulty."""

# =====================================================================================
                        # Data Bank
# =====================================================================================


placeholder_for_blanks = ["___1___", "___2___", "___3___", "___4___"]

phrases = {0: {"fill_in_blank": """During Monday night a popular television show is aired. 
    This tv show is called Monday Night 'Raw'. 
    It features two individuals or teams of people at ___1___ with each other.""", 
            "anagram": ["raw"], 
            "solution": ["war"]
          }, 
          1: {"fill_in_blank": """'ESPN' used to host a radio show called The herd with Colin Cowherd.  
    Herds are often kept in ___1___ where animals get to play.""",
             "anagram": ["ESPN"],
             "solution": ["pens"]
         },
          2: {"fill_in_blank":"""A popular tv-show by the name The Simpsons began airing in 1989.
    One of the main characters is 'Bart', he is often portrayed as a ___1___ in the show.""",
            "anagram": ["Bart"],
            "solution": ["brat"]
        },
         3: {"fill_in_blank":"""In 1999, the movie The Matrix was released. This movie was about sentient machines suppressing humanity.
    A computer programmer named 'Neo' is the ___1___ who saves the world.""",
            "anagram": ["Neo"],
            "solution": ["one"]
        },
         4: {"fill_in_blank":"""In the bible, the book of Genesis speaks of a garden, which became known as the 'Garden' of 'Eden'. 
    The moral of the story of Genesis is the ___1___ of ___2___ .""",
            "anagram": ["Garden", "Eden"],
            "solution": ["danger", "need"]
        },
        5: {"fill_in_blank":"""A jolly red giant by the name 'Santa' brings gifts to children who 'live' a life of being well-behaved. 
    However, this jolly red giant is, ___1___ and only grants wishes for ___2___ people.""",
            "anagram": ["santa", "live"],
            "solution": ["satan", "evil"]
        },
        6: {"fill_in_blank":"""This anagram was featured in the movie Rosemary's Baby. It began like this:
    'All of them witches', ___1___ ___2___ ___3___ ___4___ .""",
            "anagram": ["1st_word", "2nd_word", "3rd_word", "4th_word"],
            "solution": ["comes", "with", "the", "fall"]
        }
} 
        
main() 




