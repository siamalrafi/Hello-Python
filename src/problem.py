# Exercise 1: Print First 10 natural numbers using while loop
"""------------
i = 1
while i < 11:
    print(i)
    i += 1 """


#  Exercise 2: print this pattern
"""------------
 for x in range(1, 6, 1):
    for y in range(1, x+1):
        print(y, end=' ')
    print('')
 """


# Exercise 3: Print all sum of 0 to 10

"""------------
sum = 0
for x in range(11):
    sum += x
print('Total sum:', sum) """

"""------------
sum = 0
num = int(input('Enter a number: '))
for x in range(1, num+1, 1):
    sum += x
print('Total sum:', sum)
 """

"""------------

x = sum(range(1, 11))
print('Total sum:', x)
 """


# Exercise 4: Write a program to print multiplication table of a given number
"""-----------
 for x in range(1, 11):
    print(x*2)
 """


# Exercise 5: Display numbers from a list using loop
"""-----------
 numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)

 """


# Exercise 6: Count the total number of digits in a number
"""----------
number = 75869

counter = 0
while number != 0:
    number = number // 10
    counter += 1
print(counter)
 """


# Exercise 7: Print the following pattern
"""--------
for x in range(1, 11):
    for y in range(1,x+1):
        print(y, end=' ')
    print('')

 """

""" for x in range(0, 10+1):
    for j in range(10-x, 0, -1):
        print(j, end=' ')
    print(' ') """


# Exercise 8: Print list in reverse order using a loop

""" list1 = [10, 20, 30, 40, 50]
list1.reverse()
for x in list1:
    print(x) """

""" list1 = [10, 20, 30, 40, 50]

size = len(list1) - 1
for x in range(size, -1, -1):
    print(list1[x]) """


# Exercise 9: Display numbers from -10 to -1 using for loop

"""
for x in range(-10, 0, 1):
    print(x) """


# Exercise 10: Use else block to display a message “Done” after successful execution of for loop

""" for i in range(5):
    print(i)
print('Done') """


# Exercise 11: Write a program to display all prime numbers within a range

""" for num in range(1, 10):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
 """

# Exercise 12: Display Fibonacci series up to 10 terms
""" num1, num2 = 0, 1

for x in range(10):
    print(num1, end=' ')
    res = num1 + num2

    num1 = num2
    num2 = res
 """

# Exercise 13: Find the factorial of a given number
""" factorial = 1
for x in range(1, 5+1):
    factorial = factorial * x
print(factorial)
 """


# Exercise 14: Reverse a given integer number

""" num = 76542
reverse_number = 0

while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)
 """


# Exercise 15: Use a loop to display elements from a given list present at odd index positions

""" my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# stat from index 1 with step 2( means 1, 3, 5, an so on)
for i in my_list[1::2]:
    print(i, end=" ") """










git add .
git commit -m"This is the python story"
git pugit add .
git commit -m"This is the python stor
