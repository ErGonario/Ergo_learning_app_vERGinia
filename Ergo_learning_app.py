#Learning game about Ergo ecosystem
#Questions about fundamentals 
#Questions about ecosystem

#would love to add:
#Real time calculations of hashrate 
#MarketCap comparison of coins 





#Definizione variabili
layer_1="layer 1"
layer_2="layer 2"
layer_3="layer 3"
pow="prove of work"
pos="prove of stake"
score=0
score=int(score)
VC="yes"
gpu_resistant="gpu resistant"
asic_shitter="asic resistant, f?!#@ craazy tech"



#Inizio programma
print("Hi! this is an Ergo learning app. From now on, you're doomed! Ergo's STASI knows about you!"
print("\nWelcome to vERGinia Sir!!")
print("\nIt's a big pleasure to meet you here!")
print("\nWhat's your name fellow ergonaut?")

ergonaut = input()
print("Please, come in great", ergonaut, "!")

print("\nWhat is your age dear", ergonaut, "?")

age=int(input("I am:"))
if age > 17:
    print("Ok, just a little check to know you a little more ;) Enjoy your game", ergonaut, "!")
else:
    print("I'm so sorry, you're too young to be involved in crypto, but here you can DYOR on Ergo freely. ;) Enjoy your game", ergonaut, "!")

print("\nvERGinia, it's a small island of the Sigmaverse, it's the best place to learn about Ergo!")

print("\nAlright " + ergonaut + ", is not gonna be an easy task, but for sure we'll have some fun!")
print("Let's see if Vlady and Victor will let you pass to the next level...")
print("\nWhat kind of blockchain is the Ergo platform's one?")

while True:
    print("Is it a", layer_1, layer_2,"or a", layer_3, "?")
    answer_1=input("\nTell us, come on:" )
    if answer_1==layer_3:
        print("\nSo sorry, are you even an ergonaut?")
        print("\nAgain")
        score=score-1
    
    if answer_1==layer_2:
        print("\nReally? are you kidding me?")
        print("\nAgain")
        score=score-1
    
    if answer_1==layer_1:
        print("\nGood job! Let's go...")
        score=score+1
        break

#Descrizione argomento
print("\nSo, " + ergonaut + ", looks like you're ready to start your journey")
print("Too many cryptonauts have tried, with no luck, but I think You have what it takes to be a real Ergonaut")
print("\nLet's move on the next...")

#Quiz
while True:
    print("Is Ergo", pow,"or", pos, "?")
    answer_2=input("\nSo type it in:" )
    if answer_2==pos:
        print("\nSo sorry, for sure is not a dog!")
        print("\nTry again")
        score=score-1
    if answer_2==pow:
        print("\nGood job! Let's go...")
        score=score+1
        break

print("\nNice!")
print("You're very good at this, your score is: ", score)

print("\nNext one...")
#Descrizione argomento
print("\n", ergonaut + ", as you already know, we'll always prefer an organic growth over pump and dump schemes.")
print("Growing slowly and naturally will help us to catch the imperfections in time and work on them in the most democratic and decentralized way.")
print("\nIs the initial distribution of a chosen token so important?")

#Quiz
while True:
    print("Was Ergo distributed to venture capitalists", VC,"or not?")
    answer_3=input("\nSo type it in:" )
    if answer_3==VC:
        print("\nSo sorry, maybe you should try etoro! It's nice!")
        print("\nTry again")
        score=score-1
    else:
        print("\nGood job! Let's go...")
        score=score+1
        break

    #Descrizione argomento
print("\nYou're doing good " + ergonaut + ", maybe we should start hanging out together...")
print("\nYou surely know that Ergo was born on a crypto winter, will tell you this any GPU that mined $Erg!")
print("\nWhat's a key point of the Autolikos2 algorithm?")

#Quiz
while True:
    print("Is Autolikos2", gpu_resistant,"or maybe", asic_shitter, "?")

    answer_4=input("\nSo type it in:" )
    if answer_4==gpu_resistant:
        print("\nSo sorry, maybe some coffee? Are you sleeping?")
        print("\nAgain")
        score=score-1
    else:
        print("\nGood job! Let's go...")
        score=score+1
        break

print("\nNice!")
print("You're very good at this, your score is: ", score)

print("\nAlright " + ergonaut + ", if you tell me all the Ergo's NFTs artist I will pay you 100 $Ergs!")
print("so?")
input()
print("Just joking!")      
print("\nNow, tell me, what's Ergo's first NFTs market place?")

while True:
    print("Is it a", sky_harbor, "?", auction_house,"maybe?", "or", amazon, "?")
    answer_5=input("\nTell us, come on:" )
    if answer_5==sky_harbor:
        print("\nSo sorry, tha's the new one, very good anyways...")
        print("\nTry again")
        score=score-1
    
    if answer_5==amazon:
        print("\nReally? are you kidding me?")
        print("\nAgain")
        score=score-1
    
    if answer_5==auction_house:
        print("\nGood job! You are a real Eronaut, Let's go...")
        score=score+1
        break


print("When this bot was born as a python exercise, I couldn't even think of it, now will try to finish it.")
print("\nIt can be a nice learning bot. What do you think?")
print("Any feedback it's appreciated!!") 
print("\nluigi.mra@gmail.com")
