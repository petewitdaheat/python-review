# main function
def main():
    intro()
    eng_word = get_input()
    if_else(eng_word)

# intro
def intro():
    print("Hello! This is an English to French/German translator.")

# get input
def get_input():
    eng_word = input("Please enter an English word.\nI will give you the French and German translations: ")
    return eng_word

# if else statements
def if_else(eng_word):
    if eng_word == "hello":
        print("The French translation is bonjour.\nThe German translation is hallo.")
    elif eng_word == "yes":
        print("The French translation is oui.\nThe German translation is jawohl.")
    elif eng_word == "no":
        print("The French translation is non.\nThe German translation is nein.")    
    elif eng_word == "yellow":
        print("The French translation is jaune.\nThe German translation is gelb.")
    elif eng_word == "dog":
        print("The French translation is chien.\nThe German translation is hund.")
    elif eng_word == "table":
        print("The French translation is table.\nThe German translation is tisch.")
    elif eng_word == "book":
        print("The French translation is livre.\nThe German translation is buchen.")
    else:
        print("The English word %s isn't in my vocabulary!" % (eng_word))



main()

