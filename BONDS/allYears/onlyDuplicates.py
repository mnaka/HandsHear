import pandas as pd # import relevant libraries
import csv          # for output purposes
def toList(column, name):
    answer=[name]
    for i in range(len(column)):
        answer.append(column[i])
    return answer

df = pd.read_csv("ba2010.txt")              #Read the csv to be translated
Batter = toList(df.Batter, "Batter")
OnDeck = toList(df.OnDeck, "OnDeck")
Stat = toList(df.Stat, "Stat")
BatterBA = toList(df.BatterBA, "BatterBA")
OnDeckBA = toList(df.OnDeckBA, "OnDeckBA")

def removeSingletons():
    f=open("onlyRepeats.txt","wb")
    f.write("Batter,OnDeck,Stat,BatterBA,OnDeckBA\n")
    for i in range(1,len(Batter)):
        if Batter[i] == Batter[i-1]:
            f.write(str(Batter[i-1])+","+str(OnDeck[i-1])+","+str(Stat[i-1])+","+str(BatterBA[i-1])+","+str(OnDeckBA[i-1])+"\n")
            f.write(str(Batter[i])+","+str(OnDeck[i])+","+str(Stat[i])+","+str(BatterBA[i])+","+str(OnDeckBA[i])+"\n")
    f.close()
removeSingletons()
