from PIL import Image

# creating an empty list where we going to store all the personality choices
personality_choices = []
# asking a user for her/his name and greeting
name = input("What is your name? (please print your name):\n")
print("Hi {}! Nice to meet you!".format(name))
# asking if the user wants to play
answer = input("This small Python program will show you \nwhat tree you could be according to your features.\nWould "
               "you like to play?\n(print yes/no)\n")

def clean_personality_choices():
    # cleaning the list with all the personality choices made by the user if she/he decides to start the game from
    # the beginning. If the list is already clean, the function does nothing
    if len(personality_choices) == 0:
        pass
    else:
        personality_choices.clear()

def bye():
    # this function will be used if the user doesn't want to play
    # it will finish the game and show a funny picture of the baobab
    print("Oh, {}, you are such a baobab!".format(name))
    image = Image.open('baobab.jpg')
    image.show()


def yes_or_no_answer_only():
    # this function called if user put anything else as input when he/she needs to answer "yes" or "no" only
    # it will ask if the user wants to try again and if yes, redirect to the first answer
    print("Please answer 'yes' or 'no'.")
    try_again = str(input("Would you like to try again?\n"))
    game_start_question1()


def value_error_numbers():
    # this function is called if the user put str or number larger than 3 as answer and asks if the user wants to try
    # again. If the answer is "yes" it redirect to the first question and to "buy" function if "no"
    ve_answer = str(input("You should've choose a number 1-3 to the previous question.\nWould you like to try again? ("
                          "print yes/no)"))
    if ve_answer == "yes":
        game_start_question1()
    else:
        bye()


def game_start_question1():
    # The start of the game and the first question about the height of the person
    # if the user put wrong number, out of range or a str as the answer, this function redirects to value_error_numbers
    print("Okay, let's start!")
    print("Please choose (a number) which of those suits you best: ")
    clean_personality_choices()
    try:
        height = int(input("I am: \n1.Tall \n2.Average height \n3.Small\n"))
        if height == 1 or height == 2 or height == 3:
            personality_choices.append(height)
        else:
            value_error_numbers()
    except ValueError:
        value_error_numbers()


def question2():
    # asking user about his/her personality and storing the answer in a list with previous answers
    # the answer should be a number 1-3, if the user input a number out of range/str she will see
    # an error message and can try to play the game from the beginning
    print("Which quality suits you personality better? (choose one number only): ")
    try:
        personality = int(input("1.Tough\n2.Easygoing\n3.Both, depends on situation.\n"))
        if personality == 1 or personality == 2 or personality == 3:
            personality_choices.append(personality)
            question3()
    except ValueError:
        value_error_numbers()


def question3():
    # asking the user about her/his season preferences, storing the answer(number) in the list with other answers
    print("Which season is you favorite? (choose one number only):\n")
    try:
        weather_choice = int(input("1.Winter\n2.Spring\n3.Summer\n4.Autumn\n"))
        if weather_choice == 1 or weather_choice == 2 or weather_choice == 3 or weather_choice == 4:
            personality_choices.append(weather_choice)
            question4()
    except ValueError:
        value_error_numbers()


def question4():
    # asking the user about his/her haircut and storing the answer in a list with previous answers
    print("What is the length of your hair? (choose one number):\n")
    try:
        haircut = int(input("1.Bold\n2.Short hair\n3.Shoulder-length\n4.Long\n"))
        if haircut == 1 or haircut == 2 or haircut == 3 or haircut == 4:
            personality_choices.append(haircut)
            analyzing_answers()
    except ValueError:
        value_error_numbers()


def analyzing_answers():
    if personality_choices[0] == 1:
        tall()
    elif personality_choices[0] == 2:
        average()
    elif personality_choices[0] == 3:
        small()
    pass

def tall():
    # if the user is tall and tough/both easygoing and tough
    if personality_choices[1] == 1 or personality_choices[1] == 3:
        # if she likes winter and she is strong
        if personality_choices[2] == 1:
            # if he is bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great oak tree!".format(name))
                print("You can find some interesting facts about oak trees at this webpage:\n"
                      "https://www.thefactsite.com/oak-tree-facts/")
                oak_image = Image.open('oak_tree.png')
                oak_image.show()
            # or if she has short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful and strong Siberian Pine (Cedar)!".format(name))
                print("You can find some interesting facts about Siberian Pine Tree at this webpage:\n"
                      "https://www.goldenoils.co.uk/amazing-facts-about-siberian-pine-tree/")
                siberian_pine = Image.open('siberian_pine.jpg')
                siberian_pine.show()
            # or if he has shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Birch!".format(name))
                print("You can find some interesting facts about Birch Tree at this webpage:\n"
                      "http://justfunfacts.com/interesting-facts-about-birch-trees/")
                birch_tree = Image.open('birch.jpg')
                birch_tree.show()
            # or if she has long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Willow!".format(name))
                print("You can find some interesting facts about Willow at this webpage:\n"
                      "https://garden.lovetoknow.com/wiki/Weeping_Willow_Tree_Facts")
                willow = Image.open('willow.jpg')
                willow.show()


def average():
    pass


def small():
    pass






if answer.lower() == "yes":
    game_start_question1()
    question2()

elif answer.lower() == "no":
    bye()
else:
    yes_or_no_answer_only()









