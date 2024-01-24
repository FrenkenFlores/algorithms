with open("sunset.txt", "r") as file:
    lines = file.readlines()

descriptions = [line.strip('\n').split("; ") for line in lines]
common_words = set(descriptions[0]).intersection(set(descriptions[1]))

with open("common.txt", "w") as file:
    for word in common_words:
        print(word.capitalize(), file=file)
