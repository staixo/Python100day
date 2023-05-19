import pandas as pd

name = "Henri aime Emeline"
nato = pd.read_csv("Python100day/Intermediate/ListComprehension/nato_phonetic_alphabet.csv")
nameinNato = {row.letter: row.code for (index, row) in nato.iterrows()}
nameinNato[" "] = " "
nameList = [nameinNato[letter.upper()] for letter in name]
print(nameList)
