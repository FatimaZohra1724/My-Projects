word_list = []
with open("words.txt","r") as file:
    word_list = [line.strip() for line in file]

print(word_list)


