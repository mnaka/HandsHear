import pandas as pd # import relevant libraries
import csv          # for output purposes

def toList(column, name):
    answer=[name]
    for i in range(len(column)):
        answer.append(column[i])
    return answer

df = pd.read_csv("translated.txt")              #Read the csv to be translated
year = toList(df.Year, "Year")            # Should only be 1 year by now
outcome = toList(df.Event, "Outcome")     # Entire play is encoded.
batter = toList(df.Batter, "Batter")      # Batter
onDeck=toList(df.OnDeck, "OnDeck")        # On Deck

lahmanDF = pd.read_csv("2010BALahman.csv")      # Database #2
playerID = toList(lahmanDF.playerID, "playerID")
BA = toList(lahmanDF.BA, "BA")

def atbat():
    answer = []
    answer.append([batter[1],[onDeck[1],outcome[1]]])

    for i in range(2, len(batter)):
        if i%1000 == 0:
            print "Sorting Row ", i
        # unique batter
        if batter[i] != batter[i-1]:
            answer.append([batter[i],[onDeck[i],outcome[i]]])
        # not unique batter
        else:
            uniqueOnDeck=True
            #not uniqueOnDeck batter:
            for faced in range(0,len(answer[-1])):
                if onDeck[i] == answer[-1][faced][0]:
                    answer[-1][faced].append(outcome[i])
                    uniqueOnDeck=False
            #unique ondeck batter
            if uniqueOnDeck==True:
                answer[-1].append([onDeck[i], outcome[i]])
    return answer
def baSolver(H,AB):
    if AB==0:
        return -1
    else:
        return H/AB
def statSolver():
    database = atbat()
    answer = []
    for uniqueBatter in range(0,len(database)):
        answer.append([database[uniqueBatter][0]])
        for uniqueOnDeck in range(1,len(database[uniqueBatter])):
            answer[uniqueBatter].append([database[uniqueBatter][uniqueOnDeck][0]])
            H=0.
            AB = 0.
            for outcomes in database[uniqueBatter][uniqueOnDeck]:
                if outcomes == "HR":
                    H=H+1
                    AB = AB + 1
                elif outcomes == "Triple":
                    H=H+1
                    AB = AB + 1
                elif outcomes == "Double":
                    AB = AB + 1
                    H=H+1
                elif outcomes == "Single":
                    AB = AB + 1
                    H=H+1
                # elif outcomes == "BB" or outcomes =="IBB":
                    # BB = BB + 1
                elif outcomes == "out":
                    AB = AB + 1
            if AB > 100:
                #for RC
                # answer[uniqueBatter][uniqueOnDeck].append(wRCSolver(H,BB,TB,AB))
                # for BA
                answer[uniqueBatter][uniqueOnDeck].append(baSolver(H,AB))
            else:
                answer[uniqueBatter][uniqueOnDeck].append(-1)
    return answer
def nameChangeLtoR(name):
    end = name[-4:]
    first = name[:4]
    return first+end[0]+"0"+end[2:]

def normalizeName(name):
    answer =name.lower()
    answer = answer.replace(".","")
    answer= answer.replace(" ","")
    if answer == "stantonmike":
        return "stantongiancarlo"
    elif answer == "chacinjhoulis":
        return "chacinjhoulys"
    elif answer == "bushdavid":
        return "bushdave"
    elif answer == "hanrahanjoel":
        return answer
    return answer

def formatter(l):
    answer=[]
    f=open("ba2010.txt","wb")
    f.write("Batter,OnDeck,Stat,BatterBA,OnDeckBA\n")
    for batter in range(0, len(l)):
        i = 1
        while (i < len(playerID) and normalizeName(playerID[i]) != normalizeName(l[batter][0])):
            i +=1
        if i >= len(playerID):
            yearBatterBA="NULL"
        else:
            yearBatterBA=BA[i]
        for onDeck in range(1, len(l[batter])):
            j=1
            while (j < len(playerID) and normalizeName(playerID[j]) != normalizeName(l[batter][onDeck][0])):
                j +=1
                if j >= len(playerID):
                    yearOnDeckBA="NULL"
                else:
                    yearOnDeckBA=BA[j]
            if l[batter][onDeck][1] != -1:
                f.write(str(l[batter][0]) + "," + str(l[batter][onDeck][0]) + "," + str(l[batter][onDeck][1]) + "," + str(yearBatterBA)+ "," + str(yearOnDeckBA)+"\n")
    f.close()
formatter(statSolver())
