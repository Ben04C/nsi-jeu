import csv
def dialogue():
    #we create the list that will be used for the dialogues
    global MainDialogues
    global FlowerPotDialogue
    global StopSignDialogue
    global Policeman_After_Bush_Dialogue
    global Policeman_Before_Bush_Dialogue
    MainDialogues = []
    FlowerPotDialogue = []
    StopSignDialogue = []
    Policeman_After_Bush_Dialogue = []
    Policeman_Before_Bush_Dialogue = []


    with open('assets/Dialogues/MainDialogues.csv', "r" , encoding='UTF-8') as csvfile: #We open the csv file with the dialogues
        reader = csv.reader(csvfile, delimiter=',')
        for item in reader:
            MainDialogues.append(item) #We add every item from the list into a list

    csvfile.close()
    MainDialogues = MainDialogues[0]
    #end of MainDialogue

    with open('assets/Dialogues/Flowerpot.csv', "r" , encoding='UTF-8') as csvfile: #We open the csv file with the dialogues
        reader = csv.reader(csvfile, delimiter=',')
        print(reader)
        for item in reader:
            print(item)
            FlowerPotDialogue.append(item) #We add every item from the list into a list

    csvfile.close()
    FlowerPotDialogue = FlowerPotDialogue[0]
    #end of FlowerPotDialogue

    with open('assets/Dialogues/Stopsign.csv', "r" , encoding='UTF-8') as csvfile: #We open the csv file with the dialogues
        reader = csv.reader(csvfile, delimiter=',')
        for item in reader:
            StopSignDialogue.append(item) #We add every item from the list into a list
    csvfile.close()
    StopSignDialogue = StopSignDialogue[0]
    #end of StopSignDialogue

    with open('assets/Dialogues/Policeman_Before_Bush_Inspect.csv', "r" , encoding='UTF-8') as csvfile: #We open the csv file with the dialogues
        reader = csv.reader(csvfile, delimiter=',')
        for item in reader:
            Policeman_Before_Bush_Dialogue.append(item) #We add every item from the list into a list
    csvfile.close()
    Policeman_Before_Bush_Dialogue = Policeman_Before_Bush_Dialogue[0]
    #end of Policeman_Before_Bush_Dialogue

    with open('assets/Dialogues/Policeman_After_Bush_Inspect.csv', "r" , encoding='UTF-8') as csvfile: #We open the csv file with the dialogues
        reader = csv.reader(csvfile, delimiter=',')
        for item in reader:
            Policeman_After_Bush_Dialogue.append(item) #We add every item from the list into a list
    csvfile.close()
    Policeman_After_Bush_Dialogue = Policeman_After_Bush_Dialogue[0]
    #end of Policeman_After_Bush_Dialogue


dialogue()