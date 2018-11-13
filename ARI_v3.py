###My lists###
Text = []
Titles = []
KeyWords = []
TempList = []
ARIlist = []


import re

print("###WARNING### if you quit without saving all added information will not save to the text files")
print(" ")

###pulling down the information from the text files so they can be used for the user when they request it###

with open('Textf.txt', 'r') as f:
    Text = f.readlines()

with open('Titlesf.txt', 'r') as f:
    Titles = f.readlines()

with open('KeyWordsf.txt', 'r') as f:
    KeyWords = f.readlines()

with open('ARIListf.txt', 'r') as f:
    ARIlist = f.readlines()


def Start():

    ###the hub that you come back to after you done one of the options so you can pick what you want to do next###

    print("(1.) For searching with key words \n(2.) Add a text, key words and a title \n(3.) ARI Calculation \n(4.) For searching with ARI \n(5.) To save and exit")
    print(" ")
    Askfirst = input("What do you want to do? ")

    if Askfirst == "1":
        FindFunc()

    if Askfirst == "2":
        AddKWandText()

    if Askfirst == "3":
        ARI()

    if Askfirst == "4":
        ARIsearch()

    if Askfirst == "5":

        ###########################
        ##adding the filled lists##
        ##to the text files      ##
        ##when the user quits    ##
        ###########################

        with open('Textf.txt', 'w') as f:
            for item in Text:
                f.write("%s \n" % item)

        with open('Titlesf.txt', 'w') as f:
            for item in Titles:
                f.write("%s \n" % item)

        with open('KeyWordsf.txt', 'w') as f:
            for item in KeyWords:
                f.write("%s \n" % item)

        with open('ARIListf.txt', 'w') as f:
            for item in ARIlist:
                f.write("%s \n" % item)

        print("Goodbye!")


###Defeniton to find a title and its text through a key word###

def FindFunc():

    Ask = input("Enter a key word: ")

    AskLow = Ask.lower()

    number = 0

    calc = False

    try:
        for len in Titles: ###loop the same ammount of times there are strings in the Tiltes list to make sure you loop cand check through every one###
            while calc == False:
                if AskLow in KeyWords[number]:
                    if True:
                        ###Visual feedback###
                        print("############################")
                        print(" ")
                        print("The recommended title is:", Titles[number])
                        print(" ")
                        print("The recommended text is:", Text[number])
                        print(" ")
                        print("This has an ARI of", ARIlist[number])
                        print("############################")
                        calc = True
                else:
                    number = number + 1
                    if AskLow in KeyWords[number]:
                        if True:
                            ###Visual feedback###
                            print("############################")
                            print(" ")
                            print("The recommended title is:", Titles[number])
                            print(" ")
                            print("The recommended text is:", Text[number])
                            print(" ")
                            print("This has an ARI of", ARIlist[number])
                            print("############################")
                            calc = True
            else:
                if calc == False:
                    print("Error! Key word not found!")
                    print(" ")
                else:
                    print(" ")

    except IndexError:
        print("Error! Key word not found!")

    Start()

################################################
##This is a defentition to add Key words, Text##
##ARI and a title to the lists for future use ##
################################################

def AddKWandText():
    Correct = False

    print(" ")

    while Correct == False:

        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' #This is to differ puncuation from the text for calcultaions
        print("Warning! your sentence should have atleast 100 words to be accurate")
        print(" ")
        text = input("Enter a sentence you would like to save: ")
        if len(text) < 100:
            print(" ")
            print("Your sentence has less that 100 words and wouldn't give an accurate calculation. ")
            textAsk = input("Are you sure you want to continue? ")
            print(" ")
            textAskl = textAsk.lower()
            if textAskl == "yes":
                Text.append(text)
                no_punct=""
                for char in text:
                    if char not in punctuation:
                        no_punct = no_punct+char #taking away punctuation from the ammount of character calculation so you dont add the punctuation in with it

                characters = (len(no_punct))-no_punct.count(' ')#to work out the amount of characters
                words = len(re.findall(r'\w+', no_punct))
                sentenceend = re.compile(r"\.\.\.|\.|\!|\?")#we use sentence endings to calculate the ammount of sentences are in the text
                sentenceend.findall(text)
                ['!', '?', '...', '.']
                sentences = sum(1 for _ in sentenceend.finditer(text))

                ##############################
                ##This is to append Titles  ##
                ##and key words to the lists##
                ##############################

                keywordasktitle = input("Enter a title: ")
                Titles.append(keywordasktitle)
                keywordask1 = input("Enter key word one: ")
                TempList.append(keywordask1)
                keywordask2 = input("Enter key word two: ")
                TempList.append(keywordask2)
                keywordask3 = input("Enter key word three: ")
                TempList.append(keywordask3) ###############################################################################
                KeyWords.append(TempList[:]) ##adding everything to a temporary list first so that the key words can go in##
                TempList.clear()             ##at sections which will corespond to each title, text and ARI               ##
                ###############################################################################

                ##############################
                ##This is to check that the ##
                ##calcultation can be made  ##
                ##############################

                correct1 = 0

                if words == 0:
                    print("ERROR You have not entered any words")
                else:
                    correct1 = correct1 + 1

                if characters == 0:
                    print("ERROR You have not entered any characters")
                else:
                    correct1 = correct1 + 1

                if sentences == 0:
                    print("ERROR Please input a valid sentence including punctuation")
                else:
                    correct1 = correct1 + 1

                if correct1 == 3:
                    Correct = True
                    ARIcalc1 = (characters/words)
                    ARIcalc2 = (words/sentences)

                    ARI = 4.71*ARIcalc1+0.5*ARIcalc2-21.43

                    roundARI = (round ((ARI+5),1))

                    stringedARI = str(roundARI)

                    ARIlist.append(stringedARI)

                    ###########################################
                    ##Giving visual feedback to              ##
                    ##the user so they know the calculations ##
                    ###########################################

                    print("############################")
                    print(" ")
                    print (characters, "characters")
                    print (words, "words")
                    print (sentences, "sentences")
                    print ((round (ARI,1)), "is the American grade, suitable for this text.")
                    print((round ((ARI+5),1)), "is the reading age of this text")
                    print(" ")
                    print("############################")
                    print(" ")

                    break
            else:
                print("Returning back to menue...")
                Start()
    Start()


###Defenition for the ARI Calculation###

###This is the same code as before just doesnt add anything###

def ARI():
    Correct = False

    print(" ")

    while Correct == False:

        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        text = input("Enter your sentence: ")
        Text.append(text)
        no_punct=""
        for char in text:
            if char not in punctuation:
                no_punct = no_punct+char

        characters = (len(no_punct))-no_punct.count(' ')
        print (characters, "characters")
        words = len(re.findall(r'\w+', no_punct))
        print (words, "words")
        sentenceend = re.compile(r"\.\.\.|\.|\!|\?")
        sentenceend.findall(text)
        ['!', '?', '...', '.']
        sentences = sum(1 for _ in sentenceend.finditer(text))
        print (sentences, "sentences")

        correct1 = 0

        if words == 0:
            print("ERROR You have not entered any words")
        else:
            correct1 = correct1 + 1

        if characters == 0:
            print("ERROR You have not entered any characters")
        else:
            correct1 = correct1 + 1

        if sentences == 0:
            print("ERROR Please input a valid sentence including punctuation")
        else:
            correct1 = correct1 + 1

        if correct1 == 3:
            Correct = True
            ARIcalc1 = (characters/words)
            ARIcalc2 = (words/sentences)

            ARI = 4.71*ARIcalc1+0.5*ARIcalc2-21.43

            print("############################")
            print(" ")
            print ((round (ARI,1)), "is the American grade, suitable for this text.")
            print((round ((ARI+5),1)), "is the reading age of this text")
            print(" ")
            print("############################")

            break
    Start()

def ARIsearch():

    AskARI = input("Enter an ARI to search with: ")

    if AskARI in ARIlist:
        pos = ARIlist.index(AskARI) #getting the index of the searched ARI so you can get the same index in the other lists
        print("############################")
        print(" ")
        print("The title with this ARI is:", Titles[pos])
        print(" ")
        print("The text with this ARI is:", Text[pos])
        print(" ")
        print("############################")
    else:
        print("Error! Cannot find text with that ARI.")
        print(" ")

    Start()


Start()
