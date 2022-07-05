import json
from random import randint

def StUp():
    global start
    xs =0
    start=input("want to start wordle (yes or no):")
    while xs==0:
        if start =="yes":
            xs=1
        elif start == "no":
            xs=1
        else:
            start=input("want to start wordle (yes or no):")
    return start

def WordGen():
    global word
    with open ("words.json","r")as openfile:
        data =json.load(openfile)
        num = randint(0,200)
        snum=str(num)
        word =data[snum]
        word=word.lower()


def WordPrint():
    latter=randint(0,4)
    for num in range(0,latter):
        print("_",end=" ")
    print(word[latter], end=" ")
    endlatter = 4 -latter
    for num in range(0, endlatter):
        print("_", end=" ")
    print(" ")

def WordCheck():
    x=0
    quit = 0
    while (quit == 0):
        wrongid=0
        out2=[]
        guess =input("geuss latters for blanks:")
        while len(guess) != 5:
            print("Please enter FIVE latter word:")
            guess =input("geuss latters for blanks:")
        for num in range(0,5):
            if word[num] == guess[num]:
                out2.append(guess[num])
            else:
                out2.append("_")
                wrongid +=1
        print("you guess", 5-wrongid, " latters correct")
        print("try to guess", wrongid, "more latters")
        if wrongid == 0:
            print("")
            print("")
            print("")
            print("weldone you guess the word")
            print("--------------------------")
            print("the word was",word.upper())
            print("--------------------------")
            quit = 1
        else:
            print("*****")
            print("_____")
            print("".join(out2))
            print("_____")
            print("*****")
            tryA=input("want to try again yes or no:")
            while x==0:
                if tryA =="no":
                    print("thanks for playing")
                    quit =1
                    x=1
                elif tryA == "yes":
                    x=1
                else:
                    tryA=input("want to try again yes or no:")




