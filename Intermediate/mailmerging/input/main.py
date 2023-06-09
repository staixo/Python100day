def import_letter():
    print("import letter")
    with open("Letters/starting_letter.txt") as f:
        return f.read()

def importname():
    print("import name")
    with open("Name/invited_name.txt") as f:
        return f.read().splitlines()

def replace_name(letter, names):
    for name in names:
        new_letter = letter.replace("[name]", name)
        print(new_letter)
        with open(f"../output/letter_for_{name}.txt", "w+t", encoding="utf-8", errors="ignore") as f:
            f.write(new_letter)

letter = import_letter()
names = importname()
replace_name(letter, names)
