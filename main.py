from PIL import Image

personality_choises = []
name = input("What is your name? (please print your name):\n")
print("Hi {}! Nice to meet you!".format(name))
answer = input("This small Python program will show you \nwhat tree you could be according to your features.\nWould you like to play?\n(print yes/no)\n")

def bye():
    print("Oh, {}, you are such a baobab!".format(name))
    image = Image.open('baobab.jpg')
    image.show()


def yes_or_no_answer_only():
    print("Please answer 'yes' or 'no'.")
    try_again = str(input("Would you like to try again?\n"))
    game_start_question1()


def Value_Error_numbers():
    VE_answer = str(input("You sould've choose a number 1-3 to the previous question.\nWould you like to try again? (print yes/no)"))
    if VE_answer == "yes":
        game_start_question1()
    else:
        bye()

def game_start_question1():
    print("Okay, let's start!")
    print("Please choose (a number) which of these suits you best: ")
    try:
        height = int(input("I am: \n1.Tall \n2.Average height \n3.Small\n"))
        if height == 1 or height == 2 or height == 3:
            personality_choises.append(height)
        else:
            Value_Error_numbers()


    except ValueError:
        Value_Error_numbers()

def question2():
    print("Which quality suits you personality better? (choose one number only): ")
    try:
        personality = int(input("1.Tough\n2.Easygoing\n3.Both, depends on situation."))
        personality_choises.append(personality)
        print(personality)
    except ValueError:
        Value_Error_numbers()


if answer.lower() == "yes":
    game_start_question1()
    question2()

elif answer.lower() == "no":
    bye()
else:
    yes_or_no_answer_only()









