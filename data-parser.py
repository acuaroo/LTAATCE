import pandas as pd 
import re
import csv

data = pd.read_csv("data/rawdata.txt", header=None, sep=" ", quoting=csv.QUOTE_NONE, on_bad_lines="skip")

to_replace = {
    "false": "\nfalse",
    "true": "\ntrue",
    "%": "\n",
}

for value, replace in to_replace.items():
    drop = True if value == "%" else False

    data[0] = data[0].str.replace(value, replace).str.split("\n")
    data = data.explode(0).reset_index(drop=drop)

previous_is_exploiting = "false"
current_time = 0

data.insert(0, "time", "")
data.insert(1, "is_exploiting", "")
data.insert(3, "x", "")
data.insert(4, "y", "")
data.insert(4, "z", "")

for index, row in data.iterrows():
    modifier = 0

    if "false" in row[0] or "true" in row[0]:
        is_exploiting = 0 if "false" in row[0] else 1

        modifier += 1
        current_time += 1
        
        previous_is_exploiting = is_exploiting
        data.at[index, 0] = data.at[index, 0].replace(f"{is_exploiting},", "")

    data.at[index, "time"] = current_time
    data.at[index, "is_exploiting"] = previous_is_exploiting

    split = row[0].split(",")

    if len(split) >= 3 + modifier:
        data.at[index, "x"] = "{:.2f}".format(float(split[0 + modifier]))
        data.at[index, "y"] = "{:.2f}".format(float(split[1 + modifier]))
        data.at[index, "z"] = "{:.2f}".format(float(split[2 + modifier]))

data = data.drop(columns=["index", "level_0", 0])
data.to_csv("data/data.csv", index=False)

