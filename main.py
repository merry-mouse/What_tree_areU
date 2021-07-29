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
    if personality_choices[0] == 1 or personality_choices[0] == 2:
        # it is always nicer to guess that a person is a bit taller =)
        # that's why tall and average are in the same group
        tall_and_average()
    elif personality_choices[0] == 3:
        small()
    pass

def tall_and_average():
    # if the user is tall and tough/both easygoing and tough
    # cause it is always nicer to guess that the person is stronger and tougher =)
    if personality_choices[1] == 1 or personality_choices[1] == 3:
        # if she likes WINTER
        if personality_choices[2] == 1:
            # if bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great oak tree!".format(name))
                print("You can find some interesting facts about oak trees at this webpage:\n"
                      "https://www.thefactsite.com/oak-tree-facts/")
                oak_image = Image.open('oak_tree.png')
                oak_image.show()
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful and strong Siberian Pine (Cedar)!".format(name))
                print("You can find some interesting facts about Siberian Pine Tree at this webpage:\n"
                      "https://www.goldenoils.co.uk/amazing-facts-about-siberian-pine-tree/")
                siberian_pine = Image.open('siberian_pine.jpg')
                siberian_pine.show()
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Birch!".format(name))
                print("You can find some interesting facts about Birch Tree at this webpage:\n"
                      "http://justfunfacts.com/interesting-facts-about-birch-trees/")
                birch_tree = Image.open('birch.jpg')
                birch_tree.show()
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Willow!".format(name))
                print("You can find some interesting facts about Willow at this webpage:\n"
                      "https://garden.lovetoknow.com/wiki/Weeping_Willow_Tree_Facts")
                willow = Image.open('willow.jpg')
                willow.show()
        # if likes SPRING
        elif personality_choices[2] == 2:
            # if bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Walnut tree!".format(name))
                print("You can find some interesting facts about oak trees at this webpage:\n"
                      "https://www.softschools.com/facts/plants/walnut_tree_facts/614/")
                walnut_image = Image.open('walnut_tree.jpg')
                walnut_image.show()
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Beech (long eeeXD) tree!".format(name))
                print("You can find some interesting facts about Beech Tree at this webpage:\n"
                      "http://justfunfacts.com/interesting-facts-beech-trees/")
                beech = Image.open('beech_tree.jpg')
                beech.show()
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Sycamore tree!".format(name))
                print("You can find some interesting facts about Sycamore Tree at this webpage:\n"
                      "https://www.softschools.com/facts/plants/sycamore_tree_facts/1209/#:~:text=Interesting%20Sycamore%20tree%20Facts%3A,pieces%20represent%20exfoliating%2C%20old%20bark.")
                sycamore_tree = Image.open('sycamore.jpg')
                sycamore_tree.show()
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Cupressus cashmeriana!".format(name))
                print("You can find some interesting facts about Willow at this webpage:\n"
                      "https://en.wikipedia.org/wiki/Cupressus_cashmeriana")
                cacshmeriana = Image.open('Cupressus.jpg')
                cacshmeriana.show()
        # if likes SUMMER
        elif personality_choices[2] == 3:
            # if bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Giant Red Cedar!".format(name))
                print("You can find some interesting facts about Giant Red Cedar at this webpage:\n"
                        "https://www.encyclopedia.com/plants-and-animals/plants/plants/red-cedar")
                GiantRedCedar_image = Image.open('giantRedCedar.jpg')
                GiantRedCedar_image.show()
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Acacia tree!".format(name))
                print("You can find some interesting facts about Acacia at this webpage:\n"
                        "https://www.softschools.com/facts/plants/acacia_facts/1047/#:~:text=Acacia%20usually%20grows%20to%20the,impression%20of%20a%20giant%20fern.")
                acacia_image = Image.open('acacia.jpg')
                acacia_image.show()
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Ceiba (Kapok) tree!".format(name))
                print("You can find some interesting facts about Ceiba Tree at this webpage:\n"
                        "https://www.rainforest-alliance.org/species/kapok-tree")
                ceiba_tree = Image.open('ceiba_tree.jpg')
                ceiba_tree.show()
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Cathedral (Curtain) Fig!".format(name))
                print("You can find some interesting facts about Cathedral Fig at this webpage:\n"
                        "https://en.wikipedia.org/wiki/Curtain_Fig_Tree")
                cathedral_tree = Image.open('cathedral_fig.jpg')
                cathedral_tree.show()
        # if likes AUTUMN
        elif personality_choices[2] == 4:
            # if bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Buckeye tree!".format(name))
                print("You can find some interesting facts about Buckeye at this webpage:\n"
                        "https://homeguides.sfgate.com/buckeye-tree-40387.html")
                buckeye_image = Image.open('buckeye.png')
                buckeye_image.show()
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Black cherry tree!".format(name))
                print("You can find some interesting facts about Black cherry at this webpage:\n"
                        "https://the-natural-web.org/2016/06/03/black-cherry-for-wildlife-and-people-too/")
                black_cherry_image = Image.open('black_cherry.jpg')
                black_cherry_image.show()
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Sourwood tree!".format(name))
                print("You can find some interesting facts about Sourwood at this webpage:\n"
                        "https://www.arborday.org/trees/treeguide/TreeDetail.cfm?ItemID=921")
                sourwood_tree = Image.open('sourwood.jpg')
                sourwood_tree.show()
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Hornbeam tree!".format(name))
                print("You can find some interesting facts about Hornbeam at this webpage:\n"
                        "https://www.britannica.com/plant/hornbeam")
                hornbeam_tree = Image.open('hornbeam.jpg')
                hornbeam_tree.show()

    # if the user is TALL and EASYGOING
    elif personality_choices[1] == 2:
        # if she likes WINTER
        if personality_choices[2] == 1:
            # if BOLD
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Gmelin larch tree!".format(name))
                print("You can find some interesting facts about Gmelin larch at this webpage:\n"
                      "https://en.wikipedia.org/wiki/Larix_gmelinii")
                gmelin_image = Image.open('larix_gmelini.jpg')
                gmelin_image.show()
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful and strong Ash tree!".format(name))
                print("You can find some interesting facts about Ash Tree at this webpage:\n"
                      "https://www.softschools.com/facts/plants/ash_tree_facts/672/#:~:text=Ash%20tree%20is%20deciduous%20tree,that%20provide%20enough%20direct%20sunlight.")
                ash = Image.open('ash_tree.jpg')
                ash.show()
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Birch!".format(name))
                print("You can find some interesting facts about Birch Tree at this webpage:\n"
                      "http://justfunfacts.com/interesting-facts-about-birch-trees/")
                birch_tree = Image.open('birch.jpg')
                birch_tree.show()
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Willow!".format(name))
                print("You can find some interesting facts about Willow at this webpage:\n"
                      "https://garden.lovetoknow.com/wiki/Weeping_Willow_Tree_Facts")
                willow = Image.open('willow.jpg')
                willow.show()
        # if likes SPRING
        elif personality_choices[2] == 2:
            # if bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Walnut tree!".format(name))
                print("You can find some interesting facts about oak trees at this webpage:\n"
                      "https://www.softschools.com/facts/plants/walnut_tree_facts/614/")
                walnut_image = Image.open('walnut_tree.jpg')
                walnut_image.show()
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Apple tree!".format(name))
                print("You can find some interesting facts about Apple trees at this webpage:\n"
                      "https://web.extension.illinois.edu/apples/facts.cfm")
                apple = Image.open('apple_tree.jpg')
                apple.show()
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful Peach tree!".format(name))
                print("You can find some interesting facts about Peach Tree at this webpage:\n"
                      "https://en.wikipedia.org/wiki/Peach")
                peach_tree = Image.open('peach_tree.jpg')
                peach_tree.show()
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Weeping Silver Birch!".format(name))
                print("You can find some interesting facts about Weeping Silver Birch\n"
                      "https://www.paramountplants.co.uk/blog/index.php/weeping-birch-trees/")
                weeping_birch = Image.open('weeping_birch.jpg')
                weeping_birch.show()
        # if likes SUMMER
        elif personality_choices[2] == 3:
            # if bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great and strong Coast Redwood!".format(name))
                print("You can find some interesting facts about Coast Redwood at this webpage:\n"
                        "https://www.treehugger.com/facts-about-coast-redwoods-worlds-tallest-trees-4858758")
                coast_redwood_image = Image.open('redwood.jpg')
                coast_redwood_image.show()
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Eucalyptus tree!".format(name))
                print("You can find some interesting facts about Eucalyptus at this webpage:\n"
                        "https://www.ambientbp.com/blog/7-facts-eucalyptus-trees")
                eucalyptus_image = Image.open('Eucaliptus.jpg')
                eucalyptus_image.show()
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Ceiba (Kapok) tree!".format(name))
                print("You can find some interesting facts about Ceiba Tree at this webpage:\n"
                        "https://www.rainforest-alliance.org/species/kapok-tree")
                ceiba_tree = Image.open('ceiba_tree.jpg')
                ceiba_tree.show()
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Cathedral (Curtain) Fig!".format(name))
                print("You can find some interesting facts about Cathedral Fig at this webpage:\n"
                        "https://en.wikipedia.org/wiki/Curtain_Fig_Tree")
                cathedral_tree = Image.open('cathedral_fig.jpg')
                cathedral_tree.show()
        # if likes AUTUMN
        elif personality_choices[2] == 4:
            # if bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Poplar tree!".format(name))
                print("You can find some interesting facts about Poplar at this webpage:\n"
                        "https://www.softschools.com/facts/plants/poplar_tree_facts/600/#:~:text=It%20can%20grow%20from%2050,even%20on%20the%20slightest%20breeze.")
                poplar_image = Image.open('poplar_tree.jpg')
                poplar_image.show()
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Populus Aigeiros tree!".format(name))
                print("You can find some interesting facts about Populus Aigeiros at this webpage:\n"
                        "https://en.wikipedia.org/wiki/Populus_sect._Aigeiros")
                Populus_Aigeiros_image = Image.open('Populus_Aigerous.jpg')
                Populus_Aigeiros_image.show()
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Acer rubrum tree!".format(name))
                print("You can find some interesting facts about Acer rubrumat this webpage:\n"
                        "https://en.wikipedia.org/wiki/Acer_rubrum")
                acer_rubrum_tree = Image.open('acer_rubrum.jpg')
                acer_rubrum_tree.show()
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Camperdown Elm tree!".format(name))
                print("You can find some interesting facts about Camperdown Elm at this webpage:\n"
                        "http://newlangsyne.com/articles/trees/camperdown.htm")
                elm_tree = Image.open('camperdown_elm.jpg')
                elm_tree.show()


def small():

    pass






if answer.lower() == "yes":
    game_start_question1()
    question2()

elif answer.lower() == "no":
    bye()
else:
    yes_or_no_answer_only()









