import os
import re
import pandas as pd

# THIS DATASET IS AI GENERATED

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