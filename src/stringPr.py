# Exercise 1A: Create a string made of the first, middle and last character


""" string = 'nmenw'

firstC = string[0]
middleC = string[int(len(string) / 2)]
lastC = string[-1:]

newWord = firstC+middleC+lastC

print('New word: ' + newWord) """


# Exercise 1B: Create a string made of the middle three characters
""" def get_middle_three_chars(str1):
    midleC = int(len(str1) / 2)
    newString = str1[midleC-1:midleC+2]
    print(newString.capitalize())
get_middle_three_chars("Mr.Modern")
 """


# Exercise 2: Append new string in the middle of a given string

""" str1 = "Ault"
str2 = "Kelly"


def Append_new_string(str1, str2):
    mid = int(len(str1) / 2)
    newString = str1[:mid:]
    newString = newString + str2
    newString = newString + str1[mid:]
    print('New string: ', newString.capitalize())


Append_new_string(str1, str2) """


# Exercise 3: Create a new string made of the first, middle, and last characters of each input string

""" string1 = "America"
string2 = "Japan"
def first_mid_last(string1, string2):
    s1 = string1[0]
    s2 = string2[0]
    newF = s1+s2

    x = int(len(string1)/2)
    str1_f = string1[x:x+1]

    y = int(len(string2)/2)
    str2_f = string2[y:y+1]
    newM = str1_f + str2_f

    newL = string1[-1]+string2[-1]

    print("New Word: ", newF+newM+newL)


first_mid_last(string1, string2) """











