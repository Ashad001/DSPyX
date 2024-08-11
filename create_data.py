import os
import re
import pandas as pd

# THESE DATASETS ARE AI GENERATED and PRONE TO ERRORS

DATA = "WATER_QA" # OR "SKIN_QA"

if DATA == "WATER_QA":
    with open("./input_data/water_qa.txt", "r") as f:
        lines = f.readlines()

    data = []
    # read 2 lines 
    for i in range(0, len(lines), 2):
        question = lines[i].strip().replace("Question: ", "")
        answer = lines[i+1].strip().replace("Answer: ", "")
        if question and answer:
            data.append([question, answer])

    df = pd.DataFrame(data, columns=["question", "answer"])
    df.to_csv("./input_data/water_qa.csv", index=False)
    print("Data created successfully!")
    print(df["answer"].unique())

else:
    with open("./input_data/skin_qa.txt", "r") as f:
        lines = f.readlines()
        
    data = []
    for line in lines:
        line = line.strip()
        if line:
            question = re.search(r"Question: (.*) Answer:", line).group(1)
            answer = re.search(r"Answer: (.*)", line).group(1)
            if question and answer:
                data.append([question, answer])
        
    df = pd.DataFrame(data, columns=["question", "answer"])

    df.to_csv("./input_data/skin_qa.csv", index=False)

    print("Data created successfully!")

    # print unique answers
    print(df["answer"].unique())