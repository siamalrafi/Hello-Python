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
    str1 = string1[0]
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


# Exercise 4: Arrange string characters such that lowercase letters should come first
""" lowerCa = []
upperCa = []

for x in "PyNaTive":
    if x.islower() == True:
        lowerCa.append(x)
    else:
        upperCa.append(x)

newString = ''.join(lowerCa+upperCa)

print(newString) """


# Exercise 5: Count all letters, digits, and special symbols from a given string

""" str1 = "P@#yn26at^&i5ve"

Chars = 0
Digits = 0
Symbol = 0

for x in str1:
    if x.isdigit():
        Digits += 1
    elif x.isalpha():
        Chars += 1
    else:
        Symbol += 1

print("Chars =", Chars)
print("Digits =", Digits)
print("Symbol =", Symbol)
 """


# Exercise 6: Create a mixed String using the following rules

""" 
str1 = "Abc"
str2 = "Xyz"

def newString_FSL(str1, str2):
    newString = ' '
    st1F = str1[0]
    st1S = str1[1]
    st2F = str2[0]
    st2S = str2[1]

    s1L = str1[-1:]
    s2L = str2[-1:]
    newString = st1F + s2L + st1S + st2S + s1L+st2F
    print(newString)
    

newString_FSL(str1, str2) """


# Exercise 7: String characters balance Test

""" def string_balance_test(str1, str2):
    flag = True
    for char in str1:
        if char in str2:
            continue
        else:
            flag = False
    return flag


str1 = "Yn"
str2 = "PYnative"
flag = string_balance_test(str1, str2)
print("str1 and str2 are balanced:", flag)

str1 = "Ynf"
str2 = "PYnative"
flag = string_balance_test(str1, str2)
print("str1 and str2 are balanced:", flag) """



# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case






