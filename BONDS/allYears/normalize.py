import pandas as pd # import relevant libraries
import csv          # for output purposes

df = pd.read_csv("GameBatterOnDeckOutcome.csv") # Read the csv to be translated
yearColumn = df.Game                            # Game is of Format ANA201004050
eventColumn = df.Outcome                        # Entire play is encoded.
batterColumn = df.Batter                        # Batter
onDeckColumn=df.OnDeck                          # On Deck

#Isolate the year of the game.
def gameYear(yearColumn):                  #translation of events into strings
    #format: ANA201004050
    # 3char for team, yyyymmddg
    year=["Year"]
    for i in range(0,len(yearColumn)):
        year.append(yearColumn[i][3:7])
    return year
def batting(batterColumn):
    batter=["Batter"]
    for i in range(0,len(batterColumn)):
        batter.append(batterColumn[i])
    return batter
def onDeckCircle(onDeckColumn):
    onDeck=["onDeck"]
    for i in range(0,len(onDeckColumn)):
        onDeck.append(onDeckColumn[i])
    return onDeck
def translateOutcome(eventColumn):               #translate entire play into the batter's results
    outcome=["Outcome"]
    for result in eventColumn:
        if "HR" in result:
            outcome.append("HR")
        elif "D" in result:
            outcome.append("Double")
        elif "T" in result:
            outcome.append("Triple")
        elif "SB" in result:
            outcome.append("SB")
        elif "WP" in result or "PB" in result or "PO" in result or "OA" in result:
            outcome.append("baserunning")
        elif "S" in result:
            outcome.append("Single")
        elif "HP" in result or "SH" in result or "FLE" in result:
            outcome.append("NULL")
        elif "IW" in result:
            outcome.append("IBB")
        elif "W" in result:
            outcome.append("BB")
        elif "/BP" in result or "/P" in result or "/G" in result or "/F" in result or "/L" in result or "K" in result or "BG" in result or "BL" in result or "E" in result:
            outcome.append("out")
        else:
            outcome.append("NULL")
    return outcome
f=open("translated.txt", "wb")
f.write("Year,Batter,OnDeck,Event\n")
def isolateYear(years, desiredYear):
    for i in range(1,len(yearColumn)):
        if years[i] == desiredYear:
            f.write(str(years[i])+","+str(batter[i])+","+str(onDeck[i])+","+str(events[i])+"\n")

events = translateOutcome(eventColumn)
batter = batting(batterColumn)
onDeck = onDeckCircle(onDeckColumn)
years=gameYear(yearColumn)
isolateYear(years,"2010")
