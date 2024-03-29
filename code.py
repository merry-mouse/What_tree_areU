from PIL import Image
import time


name = []
# answer = []
# creating an empty list where we going to store all the personality choices
personality_choices = []


# asking a user for her/his name and greeting
def ask_name():
    user_name = input("What is your name? (please print your name):\n")
    name.append(user_name)
    print("Hi {}! Nice to meet you!".format(user_name))
    # asking if the user wants to play
    user_answer = input("This small Python program will show you \nwhat tree you could be according to your features.\nWould "
                "you like to play?\n(print yes/no)\n")
    # answer.append(user_answer)
    if user_answer == "yes":
        game_start_question1()
        question2()
    elif user_answer == "no":
        print("Oh, {}, you are such a baobab!".format(user_name))
        image = Image.open('baobab.jpg')
        image.show()

    else:
        yes_or_no_answer_only()

    
def bye():
    # this function will be used if the user doesn't want to play
    # it will finish the game and show a funny picture of the baobab
    print("Oh, {}, you are such a baobab!".format(name[0]))
    image = Image.open('baobab.jpg')
    image.show()
    
    # PIL needs time to open the image
    # time.sleep(5)


def clean_personality_choices():
    # cleaning the list with all the personality choices made by the user if she/he decides to start the game from
    # the beginning. If the list is already clean, the function does nothing
    if len(personality_choices) == 0:
        pass
    else:
        personality_choices.clear()


def yes_or_no_answer_only():
    # this function called if user put anything else as input when he/she needs to answer "yes" or "no" only
    # it will ask if the user wants to try again and if yes, redirect to the first answer
    print("Please answer 'yes' or 'no'.")
    try_again = str(input("Would you like to try again?\n"))
    if try_again.lower == "yes":
        game_start_question1()
    else:
        bye()


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
            quit()
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
                print("Dear, {}, you could be a great oak tree!".format(name[0]))
                print("You can find some interesting facts about oak trees at this webpage:\n"
                      "https://www.thefactsite.com/oak-tree-facts/")
                oak_image = Image.open('oak_tree.png')
                oak_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful and strong Siberian Pine (Cedar)!".format(name[0]))
                print("You can find some interesting facts about Siberian Pine Tree at this webpage:\n"
                      "https://www.goldenoils.co.uk/amazing-facts-about-siberian-pine-tree/")
                siberian_pine = Image.open('siberian_pine.jpg')
                siberian_pine.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Birch!".format(name[0]))
                print("You can find some interesting facts about Birch Tree at this webpage:\n"
                      "http://justfunfacts.com/interesting-facts-about-birch-trees/")
                birch_tree = Image.open('birch.jpg')
                birch_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Willow!".format(name[0]))
                print("You can find some interesting facts about Willow at this webpage:\n"
                      "https://garden.lovetoknow.com/wiki/Weeping_Willow_Tree_Facts")
                willow = Image.open('willow.jpg')
                willow.show()
                # PIL needs time to open the image
                # time.sleep(5)
        # if likes SPRING
        elif personality_choices[2] == 2:
            # if bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Walnut tree!".format(name[0]))
                print("You can find some interesting facts about oak trees at this webpage:\n"
                      "https://www.softschools.com/facts/plants/walnut_tree_facts/614/")
                walnut_image = Image.open('walnut_tree.jpg')
                walnut_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Beech (long eeeXD) tree!".format(name[0]))
                print("You can find some interesting facts about Beech Tree at this webpage:\n"
                      "http://justfunfacts.com/interesting-facts-beech-trees/")
                beech = Image.open('beech_tree.jpg')
                beech.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Sycamore tree!".format(name[0]))
                print("You can find some interesting facts about Sycamore Tree at this webpage:\n"
                      "https://www.softschools.com/facts/plants/sycamore_tree_facts/1209/#:~:text=Interesting%20Sycamore%20tree%20Facts%3A,pieces%20represent%20exfoliating%2C%20old%20bark.")
                sycamore_tree = Image.open('sycamore.jpg')
                sycamore_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Cupressus cashmeriana!".format(name[0]))
                print("You can find some interesting facts about Willow at this webpage:\n"
                      "https://en.wikipedia.org/wiki/Cupressus_cashmeriana")
                cacshmeriana = Image.open('Cupressus.jpg')
                cacshmeriana.show()
                # PIL needs time to open the image
                # time.sleep(5)
        # if likes SUMMER
        elif personality_choices[2] == 3:
            # if bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Giant Red Cedar!".format(name[0]))
                print("You can find some interesting facts about Giant Red Cedar at this webpage:\n"
                        "https://www.encyclopedia.com/plants-and-animals/plants/plants/red-cedar")
                GiantRedCedar_image = Image.open('giantRedCedar.jpg')
                GiantRedCedar_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Acacia tree!".format(name[0]))
                print("You can find some interesting facts about Acacia at this webpage:\n"
                        "https://www.softschools.com/facts/plants/acacia_facts/1047/#:~:text=Acacia%20usually%20grows%20to%20the,impression%20of%20a%20giant%20fern.")
                acacia_image = Image.open('acacia.jpg')
                acacia_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Ceiba (Kapok) tree!".format(name[0]))
                print("You can find some interesting facts about Ceiba Tree at this webpage:\n"
                        "https://www.rainforest-alliance.org/species/kapok-tree")
                ceiba_tree = Image.open('ceiba_tree.jpg')
                ceiba_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Cathedral (Curtain) Fig!".format(name[0]))
                print("You can find some interesting facts about Cathedral Fig at this webpage:\n"
                        "https://en.wikipedia.org/wiki/Curtain_Fig_Tree")
                cathedral_tree = Image.open('cathedral_fig.jpg')
                cathedral_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
        # if likes AUTUMN
        elif personality_choices[2] == 4:
            # if bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Buckeye tree!".format(name[0]))
                print("You can find some interesting facts about Buckeye at this webpage:\n"
                        "https://homeguides.sfgate.com/buckeye-tree-40387.html")
                buckeye_image = Image.open('buckeye.png')
                buckeye_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Black cherry tree!".format(name[0]))
                print("You can find some interesting facts about Black cherry at this webpage:\n"
                        "https://the-natural-web.org/2016/06/03/black-cherry-for-wildlife-and-people-too/")
                black_cherry_image = Image.open('black_cherry.jpg')
                black_cherry_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Sourwood tree!".format(name[0]))
                print("You can find some interesting facts about Sourwood at this webpage:\n"
                        "https://www.arborday.org/trees/treeguide/TreeDetail.cfm?ItemID=921")
                sourwood_tree = Image.open('sourwood.jpg')
                sourwood_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Hornbeam tree!".format(name[0]))
                print("You can find some interesting facts about Hornbeam at this webpage:\n"
                        "https://www.britannica.com/plant/hornbeam")
                hornbeam_tree = Image.open('hornbeam.jpg')
                hornbeam_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)

    # if the user is TALL and EASYGOING
    elif personality_choices[1] == 2:
        # if she likes WINTER
        if personality_choices[2] == 1:
            # if BOLD
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Gmelin larch tree!".format(name[0]))
                print("You can find some interesting facts about Gmelin larch at this webpage:\n"
                      "https://en.wikipedia.org/wiki/Larix_gmelinii")
                gmelin_image = Image.open('larix_gmelini.jpg')
                gmelin_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful and strong Ash tree!".format(name[0]))
                print("You can find some interesting facts about Ash Tree at this webpage:\n"
                      "https://www.softschools.com/facts/plants/ash_tree_facts/672/#:~:text=Ash%20tree%20is%20deciduous%20tree,that%20provide%20enough%20direct%20sunlight.")
                ash = Image.open('ash_tree.jpg')
                ash.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Birch!".format(name[0]))
                print("You can find some interesting facts about Birch Tree at this webpage:\n"
                      "http://justfunfacts.com/interesting-facts-about-birch-trees/")
                birch_tree = Image.open('birch.jpg')
                birch_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Willow!".format(name[0]))
                print("You can find some interesting facts about Willow at this webpage:\n"
                      "https://garden.lovetoknow.com/wiki/Weeping_Willow_Tree_Facts")
                willow = Image.open('willow.jpg')
                willow.show()
                # PIL needs time to open the image
                # time.sleep(5)
        # if likes SPRING
        elif personality_choices[2] == 2:
            # if bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Walnut tree!".format(name[0]))
                print("You can find some interesting facts about oak trees at this webpage:\n"
                      "https://www.softschools.com/facts/plants/walnut_tree_facts/614/")
                walnut_image = Image.open('walnut_tree.jpg')
                walnut_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Apple tree!".format(name[0]))
                print("You can find some interesting facts about Apple trees at this webpage:\n"
                      "https://web.extension.illinois.edu/apples/facts.cfm")
                apple = Image.open('apple_tree.jpg')
                apple.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful Peach tree!".format(name[0]))
                print("You can find some interesting facts about Peach Tree at this webpage:\n"
                      "https://en.wikipedia.org/wiki/Peach")
                peach_tree = Image.open('peach_tree.jpg')
                peach_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Weeping Silver Birch!".format(name[0]))
                print("You can find some interesting facts about Weeping Silver Birch\n"
                      "https://www.paramountplants.co.uk/blog/index.php/weeping-birch-trees/")
                weeping_birch = Image.open('weeping_birch.jpg')
                weeping_birch.show()
                # PIL needs time to open the image
                # time.sleep(5)
        # if likes SUMMER
        elif personality_choices[2] == 3:
            # if bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great and strong Coast Redwood!".format(name[0]))
                print("You can find some interesting facts about Coast Redwood at this webpage:\n"
                        "https://www.treehugger.com/facts-about-coast-redwoods-worlds-tallest-trees-4858758")
                coast_redwood_image = Image.open('redwood.jpg')
                coast_redwood_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Eucalyptus tree!".format(name[0]))
                print("You can find some interesting facts about Eucalyptus at this webpage:\n"
                        "https://www.ambientbp.com/blog/7-facts-eucalyptus-trees")
                eucalyptus_image = Image.open('Eucaliptus.jpg')
                eucalyptus_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Ceiba (Kapok) tree!".format(name[0]))
                print("You can find some interesting facts about Ceiba Tree at this webpage:\n"
                        "https://www.rainforest-alliance.org/species/kapok-tree")
                ceiba_tree = Image.open('ceiba_tree.jpg')
                ceiba_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Cathedral (Curtain) Fig!".format(name[0]))
                print("You can find some interesting facts about Cathedral Fig at this webpage:\n"
                        "https://en.wikipedia.org/wiki/Curtain_Fig_Tree")
                cathedral_tree = Image.open('cathedral_fig.jpg')
                cathedral_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
        # if likes AUTUMN
        elif personality_choices[2] == 4:
            # if bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Poplar tree!".format(name[0]))
                print("You can find some interesting facts about Poplar at this webpage:\n"
                        "https://www.softschools.com/facts/plants/poplar_tree_facts/600/#:~:text=It%20can%20grow%20from%2050,even%20on%20the%20slightest%20breeze.")
                poplar_image = Image.open('poplar_tree.jpg')
                poplar_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Populus Aigeiros tree!".format(name[0]))
                print("You can find some interesting facts about Populus Aigeiros at this webpage:\n"
                        "https://en.wikipedia.org/wiki/Populus_sect._Aigeiros")
                Populus_Aigeiros_image = Image.open('Populus_Aigerous.jpg')
                Populus_Aigeiros_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Acer rubrum tree!".format(name[0]))
                print("You can find some interesting facts about Acer rubrumat this webpage:\n"
                        "https://en.wikipedia.org/wiki/Acer_rubrum")
                acer_rubrum_tree = Image.open('acer_rubrum.jpg')
                acer_rubrum_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Camperdown Elm tree!".format(name[0]))
                print("You can find some interesting facts about Camperdown Elm at this webpage:\n"
                        "http://newlangsyne.com/articles/trees/camperdown.htm")
                elm_tree = Image.open('camperdown_elm.jpg')
                elm_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)


def small():
    # if the user is Small and Tough/Both
    # cause it is always nicer to guess that the person is stronger and tougher =)
    if personality_choices[1] == 1 or personality_choices[1] == 3:
        # if she likes WINTER
        if personality_choices[2] == 1:
            # if Bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a Goat Willow also known as Pussy Willow!".format(name[0]))
                print("You can find some interesting facts about Goat Willow at this webpage:\n"
                      "https://www.woodlandtrust.org.uk/trees-woods-and-wildlife/british-trees/a-z-of-british-trees/goat-willow/")
                goat_willow_image = Image.open('goat_willow.jpg')
                goat_willow_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful and strong Juniper tree!".format(name[0]))
                print("You can find some interesting facts about Juniper tree at this webpage:\n"
                      "https://www.goldenoils.co.uk/amazing-facts-about-siberian-pine-tree/")
                juniper_image = Image.open('juniper.jpg')
                juniper_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful Holy tree!".format(name[0]))
                print("You can find some interesting facts about Holy Tree at this webpage:\n"
                      "https://tree2mydoor.com/pages/information-trees-tree-directory-holly-trees")
                holy_tree = Image.open('holy_tree.jpg')
                holy_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Juniperus virginiana commonly known as Eastern Red Cedar!".format(name[0]))
                print("You can find some interesting facts about Eastern Red Cedar at this webpage:\n"
                      "https://en.wikipedia.org/wiki/Juniperus_virginiana")
                eastern_red_image = Image.open('eastern_red_cedar.jpg')
                eastern_red_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
        # if likes SPRING
        elif personality_choices[2] == 2:
            # if Bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Arrayan tree (Luma apiculata)!".format(name[0]))
                print("You can find some interesting facts about Arrayan trees at this webpage:\n"
                      "https://en.wikipedia.org/wiki/Luma_apiculata")
                arrayan_image = Image.open('arrayan.jpg')
                arrayan_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Brush box (Lophostemon confertus) tree!".format(name[0]))
                print("You can find some interesting facts about Brush box at this webpage:\n"
                      "https://en.wikipedia.org/wiki/Lophostemon_confertus")
                brush_image = Image.open('brush_box.jpg')
                brush_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Alder!".format(name[0]))
                print("You can find some interesting facts about Alder Tree at this webpage:\n"
                      "https://treesforlife.org.uk/into-the-forest/trees-plants-animals/trees/alder/alder-facts/")
                alder_tree = Image.open('alder.jpg')
                alder_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful  Podocarpaceae!".format(name[0]))
                print("You can find some interesting facts about Podocarpaceae at this webpage:\n"
                      "https://en.wikipedia.org/wiki/Podocarpaceae")
                podocarpaceae_image = Image.open('podocarpus_mutadae.jpg')
                podocarpaceae_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
        # if likes SUMMER
        elif personality_choices[2] == 3:
            # if bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Rubber tree!".format(name[0]))
                print("You can find some interesting facts about Rubber Tree at this webpage:\n"
                        "https://www.rainforest-alliance.org/species/rubber-tree")
                rubber_image = Image.open('rubber_tree.jpeg')
                rubber_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Ramón Nut Tree!".format(name[0]))
                print("You can find some interesting facts about Ramón Tree at this webpage:\n"
                        "https://www.rainforest-alliance.org/species/ramon-tree")
                ramon_image = Image.open('ramon_tree.jpg')
                ramon_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Cecropia tree!".format(name[0]))
                print("You can find some interesting facts about Cecropia at this webpage:\n"
                        "https://www.thesurvivalgardener.com/oh-useful-cecropia-tree/")
                cecropia_tree = Image.open('cecropia.jpg')
                cecropia_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Strangler Fig!".format(name[0]))
                print("You can find some interesting facts about Strangler Fig at this webpage:\n"
                        "https://candidegardening.com/GB/stories/f0c05166-4a3e-4788-9aa9-d32b3384ca16")
                strangler_tree = Image.open('strangler_fig.jpeg')
                strangler_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
# if likes AUTUMN
        elif personality_choices[2] == 4:
            # if Bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Sub-Antarctic Daisy tree!".format(name[0]))
                print("It is a very rare tree and unfortunately there isn't a lot of info about this tree"
                      "But you can find some at this webpage:\n"
                        "https://en.wikipedia.org/wiki/Olearia_lyallii")
                subant_image = Image.open('subant_daisy_tree.jpg')
                subant_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if Short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Olive tree!".format(name[0]))
                print("You can find some interesting facts about Olive trees at this webpage:\n"
                        "https://fincahermosa.com/hermosa/en/11-amazing-interesting-facts-olive-trees-know/")
                olive_image = Image.open('olive.jpg')
                olive_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if Shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Pohutukawa (New Zeland christmas) tree!".format(name[0]))
                print("You can find some interesting facts about Pohutukawa at this webpage:\n"
                        "https://en.wikipedia.org/wiki/Metrosideros_excelsa")
                pohutukawa_tree = Image.open('Pohutukawa.jpg')
                pohutukawa_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if Long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Hazelnut tree!".format(name[0]))
                print("You can find some interesting facts about Hazelnut trees at this webpage:\n"
                        "http://justfunfacts.com/interesting-facts-about-hazelnuts/")
                hazelnut_tree = Image.open('hazelnut.jpg')
                hazelnut_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
# if the user is SMALL and EASYGOING
    elif personality_choices[1] == 2:
        # if likes WINTER
        if personality_choices[2] == 1:
            # if BOLD
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Windmill Palm!".format(name[0]))
                print("You can find some interesting facts about Windmill Palm at this webpage:\n"
                      "https://en.wikipedia.org/wiki/Trachycarpus_fortunei")
                windmill_palm_image = Image.open('bulgaria_windmill_palm.jpg')
                windmill_palm_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful and strong Himalayan Birch!".format(name[0]))
                print("You can find some interesting facts about Himalayan Birch at this webpage:\n"
                      "https://en.wikipedia.org/wiki/Betula_utilis")
                himalayan_birch_image = Image.open('himalayan_birch.png')
                himalayan_birch_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Canadian Hemlock!".format(name[0]))
                print("You can find some interesting facts about Canadian Hemlock at this webpage:\n"
                      "https://www.arborday.org/trees/treeguide/TreeDetail.cfm?ItemID=849")
                can_hemlock_tree = Image.open('canadian_hemlock.jpg')
                can_hemlock_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Norway Spruce!".format(name[0]))
                print("You can find some interesting facts about Norway Spruce at this webpage:\n"
                      "https://www.gardenia.net/plant/picea-abies-inversa")
                norway_spruce_image = Image.open('inversa_norway_spruce.jpg')
                norway_spruce_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
        # if likes SPRING
        elif personality_choices[2] == 2:
            # if bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Higan Chrry tree!".format(name[0]))
                print("You can find some interesting facts about Higan Cherry at this webpage:\n"
                      "https://www.gardenia.net/plant-variety/prunus-x-subhirtella-higan-cherry")
                higan_cherry_image = Image.open('higan_cherry.jpg')
                higan_cherry_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Dogwood tree!".format(name[0]))
                print("You can find some interesting facts about Dogwood at this webpage:\n"
                      "https://en.wikipedia.org/wiki/Cornus")
                dogwood = Image.open('dogwood_tree.jpg')
                dogwood.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful Japanese Snowball tree!".format(name[0]))
                print("You can find some interesting facts about Japanese Snowball at this webpage:\n"
                      "https://www.hortmag.com/plants-we-love-2/japanese-snowball")
                jap_snowball_tree = Image.open('japanese_snowball.png')
                jap_snowball_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful Pear!".format(name[0]))
                print("You can find some interesting facts about Pear Teee here:\n"
                      "https://wikifarmer.com/pear-tree-information/")
                pear_image = Image.open('pear.jpg')
                pear_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
        # if likes SUMMER
        elif personality_choices[2] == 3:
            # if Bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Avocado tree!".format(name[0]))
                print("You can find some interesting facts about Avocado tree at this webpage:\n"
                        "https://owlcation.com/stem/Avocado-Trees-and-Fruits-Botanical-and-Historical-Facts")
                avocado_image = Image.open('avocado.jpeg')
                avocado_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Lime Tree!".format(name[0]))
                print("You can find some interesting facts about lime Tree at this webpage:\n"
                        "https://www.britannica.com/plant/lime")
                lime_image = Image.open('lime.jpg')
                lime_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful Apricot tree!".format(name[0]))
                print("You can find some interesting facts about Apricot trees at this webpage:\n"
                        "http://justfunfacts.com/interesting-facts-about-apricots/")
                apricot_tree = Image.open('apricot.jpg')
                apricot_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Jacaranda Mimosifolia!".format(name[0]))
                print("You can find some interesting facts about Jacaranda Mimosifolia at this webpage:\n"
                        "https://en.wikipedia.org/wiki/Jacaranda_mimosifolia")
                jacaranda_tree = Image.open('jacaranda.jpg')
                jacaranda_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
        # if likes AUTUMN
        elif personality_choices[2] == 4:
            # if Bold
            if personality_choices[3] == 1:
                print("Dear, {}, you could be a great Weeping Japanese Maple Tree!".format(name[0]))
                print("You can find more information about Japanese maple at this webpage:\n"
                        "https://www.monrovia.com/be-inspired/10-facts-every-japanese-maple-lover-needs-to-know.html")
                jap_maple_image = Image.open('japanese_maple.jpg')
                jap_maple_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if Short hair
            elif personality_choices[3] == 2:
                print("{}, your tree is a beautiful Spindle tree!".format(name[0]))
                print("You can find some interesting facts about Spindle trees at this webpage:\n"
                        "https://www.woodlandtrust.org.uk/trees-woods-and-wildlife/british-trees/a-z-of-british-trees/spindle/#:~:text=Spindle%20is%20a%20deciduous%20native,which%20have%20bright%20orange%20seeds.")
                spindle_image = Image.open('spindle.jpg')
                spindle_image.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if Shoulder-length hair
            elif personality_choices[3] == 3:
                print("{}, your tree is a beautiful and strong Paperbark Maple tree!".format(name[0]))
                print("You can find some interesting facts about Paperbark at this webpage:\n"
                        "https://www.thespruce.com/growing-the-paperbark-maple-acer-griseum-3269319")
                paperbark_tree = Image.open('paperbark_maple.jpg')
                paperbark_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
            # if Long hair
            elif personality_choices[3] == 4:
                print("{}, your tree is a beautiful and strong Golden Curls Willow!".format(name[0]))
                print("You can find some interesting facts about Golden Curls Willow at this webpage:\n"
                        "https://mikesbackyardnursery.com/2012/03/golden-curls-willow/")
                golden_willow_tree = Image.open('golden_willow.jpg')
                golden_willow_tree.show()
                # PIL needs time to open the image
                # time.sleep(5)
 
ask_name()








