from madlibFile import madlib
import random

selectedMadlib = "Name, get that Adjective Noun Adverb Verb of my Celebreity BodyPart"

def getInput(type):
    prompt = "Enter a "+type+": "
    answer = input(prompt)
    return answer

def findAllIndexes(string, keys):
    allIndexes = []
    for key in keys:
        index = 0
        indexes = []
        while True:
            index = string.find(key, index)
            if index == -1: break
            indexes.append(index)
            index += len(key)
        allIndexes.append(indexes)
    return allIndexes

def getInputAndReplace(types, indexesAll,selectedMadlib):
    i = 0
    for type in types:
        indexes = indexesAll[i]
        for ind in indexes:
            if(type == "Noise"):
                inp = getInput(type)
                selectedMadlib = selectedMadlib.replace(type,inp)
                break
            else:
                inp = getInput(type)
                selectedMadlib = selectedMadlib.replace(type,inp,1)
        i = i + 1
    return selectedMadlib

######## Main program #######
randomIndex = random.randrange(0,(len(madlib)),1)#from index 0 to the length of the madlib list in steps of 1
selectedMadlib = madlib[randomIndex] #randomly select a madlib from the file

#go though and find all the indexes of the keys we need to fill
types = list(["Noun","Adjective","Celebrity","Adverb","Verb","BodyPart","Name","Place","Number","Noise","Animal","Color","PluralNoun"])
indexesAll = findAllIndexes(selectedMadlib,types)
print(indexesAll)

#get the users input for each occurrence and replace it with the input
selectedMadlib = getInputAndReplace(types,indexesAll,selectedMadlib)

print("\nDone! Here is your madlib!\n\n")

print(selectedMadlib+"\n")
