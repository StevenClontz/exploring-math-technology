## LEAVE THIS FIRST
with open("dictionary.csv", "r") as words_file:
    words = [word[:-1] for word in words_file.readlines()[:50]]

## UNSCRAMBLE/INDENT THE REST
print(f"The number of vowels in {word} is {num_of_vowels}.")
num_of_vowels = num_of_vowels + word.count(vowel)
for word in words:
for vowel in ["a","e","i","o","u"]:
num_of_vowels = 0
