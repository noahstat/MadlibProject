from madlibFile import madlib
import random

#prompt the user for the feild of input and capture it
def getInput(type):
    prompt = "Enter a "+type+": "
    return input(prompt)

#go through all feilds and find thier indexes to get a count of how many we need
def findAllIndexes(string, keys):
    allIndexes = []#make a list to put the list of indexes in
    for key in keys:
        index = 0
        indexes = []#create a blank list to add each index to
        while True:
            index = string.find(key, index)#find the key starting starting at the last occurrence
            if index == -1: break#if it does not find anything
            indexes.append(index)
            index += len(key)#move the search index to after the current occurrence
        allIndexes.append(indexes)#append the list of indexes to the rest
    return allIndexes

#get the input and replace the corrosponding feild with that input
def getInputAndReplace(types, indexesAll,selectedMadlib):
    i = 0
    for type in types:
        indexes = indexesAll[i]#get the current list of indexes
        for ind in indexes:
            if(type == "Noise"):#if it is noise only get one to make McDonald one less annoying
                inp = getInput(type)
                selectedMadlib = selectedMadlib.replace(type,inp)
                break
            else:
                inp = getInput(type)#get input using the current feild
                selectedMadlib = selectedMadlib.replace(type,inp,1)#repalce the next occurrence of that feild with the input
        i = i + 1#increment the index list
    return selectedMadlib#return the altered file

######## Main program #######
randomIndex = random.randrange(0,(len(madlib)),1)#from index 0 to the length of the madlib list in steps of 1
selectedMadlib = madlib[randomIndex] #randomly select a madlib from the file

#go though and find all the indexes of the keys we need to fill
types = list(["Noun","Adjective","Celebrity","Adverb","Verb","BodyPart","Name","Place","Number","Noise","Animal","Color","PluralNoun"])
#TODO: want to add some sort of queue to preserve the order that they are found in, making it less monotonus 
indexesAll = findAllIndexes(selectedMadlib,types)

#get the users input for each occurrence and replace it with the input
finishedMadlib = getInputAndReplace(types,indexesAll,selectedMadlib)

print("\nDone! Here is your madlib!\n\n")

print(finishedMadlib+"\n")
