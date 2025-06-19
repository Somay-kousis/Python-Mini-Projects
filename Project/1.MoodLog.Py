# Q1: Mood Logger (OOP + File Handling + JSON)
# Create a CLI-based Python program where the user can log their daily mood with an optional note. 
# Each entry should be saved to a JSON file with the timestamp, and the program should support:
# Adding a new entry
# Viewing all past entries
# Viewing only entries with a specific mood (e.g., “happy”)

from datetime import datetime
import json
import os
import numpy as np
import pandas as pd

if os.path.exists("1.json"):
    with open("1.json", "r") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
else:
    df = pd.DataFrame(columns=["Date", "Mood", "Note"])

class MoodLog:
    i = len(df)
    def __init__(self, mood, note=np.nan):     
        self.mood = mood
        self.note = note
        
        df.at[MoodLog.i,"Mood"] = mood
        df.at[MoodLog.i,"Date"] = datetime.now().strftime("%Y-%m-%d")
        df.at[MoodLog.i,"Note"] = note
        MoodLog.i+=1
        
    def view (self):
        print(df.head(MoodLog.i)) # shows only filled rows

print("So! How about me start with your today's mood")
mood = input()
print("Any extra note? About your mood")
note = input()

Log = MoodLog(mood,note)     

print("If you wanna see past logs type 'yes'")
Asking_For_Past_Logs = input()
Asking_For_Past_Logs = str.lower(Asking_For_Past_Logs).strip()

if Asking_For_Past_Logs == "yes":
    Log.view()
    
print("Which mood detail do you need?")
detail_of = input()
detail_of = detail_of.lower()

Query = df[df["Mood"].str.lower() == detail_of]
print(Query)


with open("1.json","w") as f:
   f.write(df.dropna(subset=["Mood"]).to_json(orient="records"))
       



        
