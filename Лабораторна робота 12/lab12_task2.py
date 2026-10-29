import random

def get_unique_words(filename):
    f = open(filename, "r")
    words = []
    for line in f:
        for word in line.split():
            if word not in words:
                words.append(word)
    f.close()
    return words

unique_words = get_unique_words("text.txt")

print("Унікальних слів у файлі:", len(unique_words))

N = int(input("Скільки випадкових слів вивести? "))

for i in range(N):
    word = random.choice(unique_words)
    print(word)