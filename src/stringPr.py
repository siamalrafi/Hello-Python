# Exercise 1A: Create a string made of the first, middle and last character


""" string = 'nmenw'

firstC = string[0]
middleC = string[int(len(string) / 2)]
lastC = string[-1:]

newWord = firstC+middleC+lastC

print('New word: ' + newWord) """


# Exercise 1B: Create a string made of the middle three characters
def get_middle_three_chars(str1):
    midleC = int(len(str1) / 2)
    newString = str1[midleC-1:midleC+2]
    print(newString.capitalize())

get_middle_three_chars("Mr.Modern")
