import csv

#we create the list that will be used for the dialogues
MainDialogues = []
FlowerPotDialogue = []


with open('assets/Dialogues/MainDialogues.csv') as csvfile: #We open the csv file with the dialogues
    reader = csv.reader(csvfile, delimiter=';')
    for item in reader:
        MainDialogues.append(item) #We add every item from the list into a list

csvfile.close()
MainDialogues = MainDialogues[0]
#end of MainDialogue

with open('assets/Dialogues/Flowerpot.csv') as csvfile: #We open the csv file with the dialogues
    reader = csv.reader(csvfile, delimiter=';')
    for item in reader:
        FlowerPotDialogue.append(item) #We add every item from the list into a list
csvfile.close()
FlowerPotDialogue = FlowerPotDialogue[0]
#end of FlowerPotDialogue

print(MainDialogues)
for i in range(0, len(MainDialogues)):
    print(MainDialogues[i])


for i in range(0, len(FlowerPotDialogue)):
    print(FlowerPotDialogue[i])