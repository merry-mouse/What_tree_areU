from PIL import Image

# creating an empty list where we going to store all the personality choices
personality_choices = []
# asking a user for her/his name and greeting
name = input("What is your name? (please print your name):\n")
print("Hi {}! Nice to meet you!".format(name))
# asking if the user wants to play
answer = input("This small Python program will show you \nwhat tree you could be according to your features.\nWould "
               "you like to play?\n(print yes/no)\n")


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
    print("Please choose (a number) which of these suits you best: ")
    try:
        height = int(input("I am: \n1.Tall \n2.Average height \n3.Small\n"))
        if height == 1 or height == 2 or height == 3:
            personality_choices.append(height)
        else:
            value_error_numbers()
    except ValueError:
        value_error_numbers()


def question2():
    print("Which quality suits you personality better? (choose one number only): ")
    try:
        personality = int(input("1.Tough\n2.Easygoing\n3.Both, depends on situation."))
        personality_choices.append(personality)
        print(personality)
    except ValueError:
        value_error_numbers()


if answer.lower() == "yes":
    game_start_question1()
    question2()

elif answer.lower() == "no":
    bye()
else:
    yes_or_no_answer_only()









