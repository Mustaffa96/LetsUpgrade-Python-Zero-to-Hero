# using randint()
import random

# open file
with open("guessIt.txt", "r") as file:
    data = file.read()
    words = data.split()

    # Generating a random number for word position
    word_pos = random.randint(0, len(words) - 1)
    print("Position:", word_pos)
    print("Word at position:", words[word_pos])
