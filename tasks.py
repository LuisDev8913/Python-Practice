# program to count the number of vowels in the String
#
# sentence = input("Enter the String: ") vowels = 0 for i in sentence: if i == "a" or i == "e" or i == "i" or i ==
# "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U": vowels += 1
#
# print("There are", vowels, "vowels in your String")

# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# Consider use range(#begin, #end) method
#
# list1 = []
# for i in range(2000, 3201):
#     if (i % 7 == 0) and (i % 5 != 0):
#         list1.append(i)
#
# print(list1)
#
#
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
# =========CODE============
#
# def fact(x):
#     """ this function calculates the factorial of the input number"""
#     if x == 0:
#         return 1
#     else:
#         return x * fact(x - 1)
#
#
# x = int(input("Enter any number: "))
# if x != 0:
#     print("The factorial of", x, "is", fact(x))
# else:
#     print("The factorial of 0 is 1")
#
# Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that
# is an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose
# the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25,
# 6: 36, 7: 49, 8: 64}
#
# =======CODE==========
# n = int(input("Enter any number: "))
# dictionary = {}
#
# for i in range(1, n + 1):
#     dictionary[i] = i * i
#
# print(dictionary)
#
#
# Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and
# a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,
# 98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
#
# ===========CODE================
#
# values = input("Enter the values: ")
# result = values.split(",")
# t = tuple(result)
# print(result)
# print(t)
#
#


# Question:
# write a program which takes imput of the marks of the subjects and prompt the grade to the user

# sub1 = int(input("Enter marks in Chemistry: "))
#
# sub2 = int(input("Enter marks in Physics: "))
#
# sub3 = int(input("Enter marks in Maths: "))
#
# sub4 = int(input("Enter marks in Comp Sci: "))
#
# sub5 = int(input("Enter marks in Urdu: "))
#
#
# per = ((sub1 + sub2 + sub3 + sub4 + sub5) / 500) * 100
#
# print("Your percentage is: ", per)
#
# print("Your grade is: ", end="")
#
# if per <= 100 and per >= 80:
#     print("A1")
#
# elif per < 80 and per >= 70:
#     print("A")
#
# elif per < 70 and per >= 60:
#     print("B")
#
# elif per < 60 and per >= 50:
#     print("C")
#
# elif per < 50:
#     print("Fail")

# Let's learn about list comprehensions! You are given three integers X, Y and Z representing the dimensions of a
# cuboid along with an integer N. You have to print a list of all possible coordinates given by (i, j, k) on a 3D
# grid where the sum of i + j + k  is not equal to N. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z
#
# Input Format
# Four integers X, Y, Z and N each on four separate lines, respectively.
#
# Constraints
# Print the list in lexicographic increasing order.
#
# Sample Input
# 1
# 1
# 1
# 2
#
# Sample Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
#
#
# Enter your code here. Read input from STDIN. Print output to STDOUT

# x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#
# result = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != n]
# print(result)


# n = int(input())
#     arr = map(int, input().split())
#
#     print(sorted(list(set(arr)))[-2])

# the guessing game

# import random
#
# comp_choice = random.randint(1, 20)
# print(comp_choice)
#
# my_guess = int(input("Guess the number chosen by the computer: "))
#
# if my_guess > comp_choice:
#     print("Your guess was too high")
#
# elif my_guess < comp_choice:
#     print("Your number is too low")
#
# elif my_guess == comp_choice:
#     print("You guessed the correct number!!")

# program to calculate the square root of positive and complex numbers

# import math
#
# num = int(input("Enter any positive number: "))
# if num < 0:
#     print("Please enter a positive number")
#
# print("The sqaure root of", num, "is: "math.sqrt(num))

# import cmath
#
# num = complex(input("Enter any complex number: "))
#
# print("The square root of complex number", num, "is: ", cmath.sqrt(num))

# program to calculate the area of a triangle
#
# import math
#
# a = float(input("Enter the first side of triangle: "))
# b = float(input("Enter the second side of triangle: "))
# c = float(input("Enter the third side of triangle: "))
#
#
# def para():
#     """ calculates the value of parameter of the triangle """
#     parameter = (a + b + c) / 2
#     return parameter
#
#
# def area(parameter):
#     """ Calculates the area of a triangle """
#     answer = math.sqrt(parameter * (parameter - a) * (parameter - b) * (parameter - c))
#     return "The area of the triangle is %0.2f " % answer
#
#
# print(area(para()))

# program to solve the find out the root if quadratic equation

# import math
#
# print("Solve the quadratic equation ax^2 + bx + c = 0")
# a = int(input("Enter the value of coefficient of x^2: "))
# b = int(input("Enter the value of coefficient of x: "))
# c = int(input("Enter the constant value: "))
#
#
# def discrim():
#     """ Calculates the discriminant of the equation """
#     discriminant = math.sqrt((b**2) - (4 * a * c))
#     return discriminant
#
#
# def roots(discriminant):
#     """ Calculates the roots of the equation """
#     x1 = (-b + discriminant) / 2 * a
#     x2 = (-b - discriminant) / 2 * a
#     return "The roots of equation {}x^2 + {}x + {} are: ".format(a, b, c), x1,  x2
#
#
# print(roots(discrim()))

# swapping the value of 2 variables

# x = 22
# y = 33
#
# x, y = y, x
#
# print("The value of x after swapping is: ", x)
# print("The value of y after swapping is: ", y)


# write a program to calculate the armstrong number
#
# num = int(input("Enter any number: "))
#
# # this is value in which the total of cubes of number will be added
# sum = 0
#
# num2 = num # initializing another variable so we could the num value with sum...
#
# while num2 > 0:
#     num3 = num2 % 10  # this operation gives us each number for making cube separately
#
#     sum += num3 ** 3  # adding the cube of single number from num to sum variable
#     # print(sum)
#     num2 //= 10   # this is going to remove the last number from the num value
#
# if num == sum:
#     print("The number {} is an Armstrong number".format(num))
#
# else:
#     print("The number {} is not Armstrong number".format(num))


# write a program to generate the square of the numbers


# n = int(input("Enter the range of the numbers: "))
# for i in range(1, n + 1):
#     print("The square of", i, "is",  i ** 2)

# now making a function which calculate the square of the numbers

# def sq(n):
#
#     for i in range(1, n + 1):
#         print("The square of", i, "is", i ** 2)
#
# sq(10)
#
# lst = [[x for x in range(3)] for y in range(3)]
#
# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 == 0:
#             print("#")


# tup = (1, 2, 4, 8)
# tup = tup[-2: -1]
# print(tup)
# tup = tup[-1]
# print(tup)

# lst = [1, 2]
#
# for v in range(2):
#     lst.insert(-1, lst[v])
#
# print(lst)

# d = {"1": "0", "0": "1"}
#
# for x in d.values():
#     print(x, end="")

# def fun(a, b):
#     return b ** a
#
# print(fun(b = 2, 2))

# list = [x * x for x in range(5)]
# print(list)

# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y - 1)
#
# print(fun(0, 3))

# def fun1(a):
#     return None
#
# def fun2(a):
#     return fun1(a) * fun1(a)
#
# print(fun2(2))
# i = 0
# while i < i + 2:
#     i += 1
#     print("*")
# else:
#     print("*")


# Write a program to convert kilometers into miles
# 1 kilometer = 0.621371 miles

# print("1. Convert kilometer into miles.")
# print("2. Convert miles into kilometers.")
#
# x = int(input("Enter number of which conversion you want: "))
#
# con_factor = 0.621371  # since 1 kilometer is = 0.621371 miles
#
# if x == 1:
#     print("=========Kilometers into miles conversion=========")
#
#     km = float(input("Enter value you want to covert in miles: "))
#
#
#     def ktm():
#         miles = km * con_factor
#         return "%2f" % miles
#
#
#     print(km, "kilometers are equal to:", ktm()+" miles")
#
# elif x == 2:
#     print("=======Miles into kilometer conversion======")
#
#     mil = float(input("Enter the value to convert into kilometers: "))
#
#
#     def mile():
#         kilometers = mil / con_factor
#         return "%2f" % kilometers
#
#
#     print(mil, "miles are equals to:", mile()+" kilometers")
#
# else:
#     print("Invalid choice, Please enter correct choice number.")


# write a program to convert celsius into fahrenheit and vice versa
#
# print("Please select one choice.")
# print("1. Convert Celsius into Fahrenheit.")
# print("2. Convert Fahrenheit into Celsius.")
#
# choice = int(input("Enter your choice of conversion: "))
#
# if choice == 1:
#     print("===========Celsius to Fahrenheit conversion==========")
#     cel = float(input("Enter the value you want to convert in Fahrenheit: "))
#
#     def fah():
#         fahrenheit = (cel * 1.8) + 32
#         return "%0.2f" % fahrenheit
#     print(cel, "Celsius is equals to: ", fah()+" fahrenheits")
#
# elif choice == 2:
#     print("==========Fahrenheit to Celsius conversion============")
#
#     far = float(input("Enter the value you want to convert in Celsius: "))
#
#     def cel():
#         celsius = (far - 32)/1.8
#         return "%0.2f" % celsius
#     print(far, "Fahrenheits are equal to: ", cel()+" celsius")
#
# else:
#     print("Invalid choice, Please enter correct choice number.")


# program to check whether the year is leap year or not condition 1 = if year is divisible by 4 then...it should be
# divisible by 100 and if its true then it should be divisible by 400 also...if not...then year is not the leap year


# year = int(input("Enter the year: "))
#
#
# def isleap(year):
#     if year % 4 == 0:
#         if year % 100 != 0 or year % 400 == 0:
#             print("{} is a leap year".format(year))
#         else:
#             print("{} is not a leap year".format(year))
#     else:
#         print("{} is not leap year".format(year))
#
#
# isleap(year)


# Program to find whether a number is prime number or not...and if not...then explain how...by showing the factors of it
# prime number is that number which do not have any factors except itself


# num = int(input("Enter any number: "))

# we have to write a code by which we can check whether the factors of number exist or not
#
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number.")
#             print(i, "times", num // i, "is", num)
#             break
#     else:
#         print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")


# program to find out the factors of a given number

# num = int(input("Enter any number: "))
#
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i, "times", num // i, "is", num)


# program to print the prime numbers in a interval

# lower = int(input("Enter the upper limit: "))
# upper = int(input("Enter the lower limit: "))
#
# print("Prime numbers in the interval", lower, "and", upper, "are:")
# count = 0
# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)
#             count += 1
#
# print("There are", count, "prime numbers in interval", lower, "and", upper)

# write a program to print the factorial of the any number

# num = int(input("Enter any number: "))
# factorial = 1
# if num < 0:
#     print("The factorial of negative number does not exist.")
#
# elif num == 0 or num == 1:
#     print("The factorial of", num, "is 1")
#
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print("This factorial of {} is".format(num), factorial)

# program to print the multiplication table

# num = int(input("Enter any number: "))
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# program to print the fibonacci series 0, 1, 2, 3, 5, 8 ....

# first the number of terms you want to get in certain fibonacci series

# n_terms = int(input("Enter the number of terms you want in the fibonacci series: "))
#
# first_num = 0
# sec_num = 1
#
# counter = 0
# if n_terms == 0 or n_terms == 1:
#     print(first_num)
#
# elif n_terms < 0:
#     print("Please enter a positive number.")
#
# else:
#     print("The fibonacci series is: ", end="")
#     while counter < n_terms:
#         print(first_num, end=", ")
#         nth = first_num + sec_num
#
#         first_num = sec_num
#         sec_num = nth
#         counter += 1


# write a function to count number of integer in a number

# num = int(input("Enter any number to find out it's length: "))
#
#
# def num_counter(any_num):
#     """ function to count the number of int in a number """
#     counter = 0
#     while any_num > 0:
#         any_num = any_num // 10
#         counter += 1
#     return counter
#
# write a program to check what number is repeated in the list

# num = int(input("Enter the range of your list: "))
#
# my_inp_list = []
#
# for i in range(num):
#     x = int(input("Enter numbers you want to include in your list: "))
#     my_inp_list.append(x)
#
# print("Your list is: ", my_inp_list)
#
# repeated_values = []
#
#
# def check_repeated(my_list):
#     for i in range(len(my_list)):
#         for j in range(i + 1, len(my_list)):
#             if my_list[i] == my_list[j] and my_list[i] not in repeated_values:
#                 repeated_values.append(my_list[i])
#     return repeated_values
#
#
# print(""" Enter your choice:
# 1. if you want to check which number is repeated in the list
# 2. Exit """)
#
# choice = int(input("Enter any choice: "))
#
# if choice == 1:
#     print("The values repeated in the list are: ", check_repeated(my_inp_list))
# else:
#     print("Thank You")

# write a program which converts decimal into binary number

# num = 333
#
# total = ""
# while num > 1:
#     remainder = num % 2
#     total = str(remainder) + total
#
#     num //= 2
#     if num == 1:
#         total = str(1) + total
#
# print(total)
#

# code for making the four bits
# num = input("Enter any number: ")
#
# length = len(num)
# print(length)
# modulus = length % 4
# num2 = ""
# if modulus != 0:
#     for i in range(modulus * 4):
#         num2 = i * str(0) + str(num)
#         if len(num2) == modulus + length:
#             break
# else:
#     print(num)
#
# print(num2)

# program to convert binary to hexa

# num = '00110110010000001110'  # the number from here should be in string format...if not then program will show
# error if number # starts with zero length = len(str(num))
#
# range1 = 0
# range2 = 4
#
# final = []
# while length >= 0:
#     total = 0
#     num2 = str(num)[range1:range2]
#     # print(num2)
#     for i in range(len(num2)):
#         if num2[0] == str(1):
#             total += 8
#         elif num2[0] == str(0):
#             total += 0
#         if num2[1] == str(1):
#             total += 4
#         elif num2[1] == str(0):
#             total += 0
#         if num2[2] == str(1):
#             total += 2
#         elif num2[2] == str(0):
#             total += 0
#         if num2[3] == str(1):
#             total += 1
#         elif num2[3] == str(0):
#             total += 0
#         if total <= 16:
#             break
#     if total >= 0 and total != 10 and total != 11 and total != 12 and total != 13 and total != 14 and total != 15:
#         final.append(total)
#     if total > 0 and total == 10:
#         final.append("A")
#     if total > 0 and total == 11:
#         final.append("B")
#     if total > 0 and total == 12:
#         final.append("C")
#     if total > 0 and total == 13:
#         final.append("D")
#     if total > 0 and total == 14:
#         final.append("E")
#     if total > 0 and total == 15:
#         final.append("F")
#     range1 += 4
#     range2 += 5
#     length -= 4
#     num2 = ""
# final_answer = "".join(str(element) for element in final)
# print("Your", num, "in Hex Decimal is equal to", final_answer)

# Alhumdullilah <3

# print("Please think a word in your mind.")
# len_user = int(input("Enter how many letters your word has: "))
#
# print("Please enter the column number of your letter from the list below: ")
# print("""
# 1\t2\t3\t4
# -------------
# A\tB\tC\tD
# E\tF\tG\tH
# I\tJ\tK\tL
# M\tN\tO\tP
# Q\tR\tS\tT
# U\tV\tW\tX
# Y\tZ
# """)
#
# col_list = []
# for i in range(1, len_user + 1):
#     col = int(input("Enter the column number for {} letter of your word:".format(i)))
#     col_list.append(col)
# print(col_list)
#
# print("Now please enter the column in which your letters appear from the list below: ")
# num = "1\t2\t3\t4\t5\t6\t7"
# print(num)
# print("---------------------")
#
# last_list = []
# conj_col1 = ["A", "E", "I", "M", "Q", "U", "Y"]
# conj_col2 = ["B", "F", "J", "N", "R", "V", "Z"]
# conj_col3 = ["C", "G", "K", "O", "S", "W"]
# conj_col4 = ["D", "H", "L", "P", "T", "X"]
# for j in col_list:
#     if j == 1:
#         print("A\tE\tI\tM\tQ\tU\tY")
#         last_list.append(conj_col1)
#     if j == 2:
#         print("B\tF\tJ\tN\tR\tV\tZ")
#         last_list.append(conj_col2)
#     if j == 3:
#         print("C\tG\tK\tO\tS\tW")
#         last_list.append(conj_col3)
#     if j == 4:
#         print("D\tH\tL\tP\tT\tX")
#         last_list.append(conj_col4)
#
# final_list = []
# ls = []
# for letter_choice in range(1, len(col_list) + 1):
#     letter_choosen = int(input("Enter the column number of the {} letter from word: ".format(letter_choice)))
#     final_list.append(letter_choosen - 1)
# # print(final_list)
#
# # print(last_list)
# word = []
# for a in range(len(final_list)):
#     var = last_list[a]
#     index = final_list[a]
#     # print(index)
#     # print(var)
#     word.append(var[index])
#
#
# final_word = "".join(word)
# print("Your word is:", final_word)

# num = "12"
# for i in range(len(num) * 4):
#     num = str(0) + num
#     if len(num) % 4 == 0:
#         break
# print(num)
#
# num = "00110110010000001110"
# # print(len(num))
# r1 = 0
# r2 = 4
# length = len(num)
# hex_list = []
#
# while length >= 1:
#     num2 = num[r1:r2]
#     # print(num2)
#     total = 0
#     if num2[0] == str(1):
#         total += 8
#     elif num2[0] == str(0):
#         total += 0
#     if num2[1] == str(1):
#         total += 4
#     elif num2[1] == str(0):
#         total += 0
#     if num2[2] == str(1):
#         total += 2
#     elif num2[2] == str(0):
#         total += 0
#     if num2[3] == str(1):
#         total += 1
#     elif num2[3] == str(0):
#         total += 0
#     if total >= 16:
#         break
#
#     if total == 0 or total > 0 and total != 10 and total != 11 and total != 12 and total != 13 and total != 14 and total != 15:
#         hex_list.append(total)
#     if total == 10:
#         hex_list.append("A")
#     if total == 11:
#         hex_list.append("B")
#     if total == 12:
#         hex_list.append("C")
#     if total == 13:
#         hex_list.append("D")
#     if total == 14:
#         hex_list.append("E")
#     if total == 15:
#         hex_list.append("F")
#     r1 += 4
#     r2 += 4
#     length -= 4
#
# answer = "".join(str(element) for element in hex_list)
# print(answer)

# program using lambda function
# lambda function are also called as anonymous functions...in these functions you don't have to write the def keyword

# double = lambda x: x ** 2
# print(double(5))

# lst = [1, 2, 3, 4, 5, 6]
# my_lst = list(filter(lambda x: (x % 2 == 0), lst))
# print(my_lst)

# lst = [1, 2, 3, 4, 5]
#
# new_lst = list(map(lambda x: x * 2, lst))
# print(new_lst)

# how to print the nested index in tuples
# n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
#
# # nested index
# print(n_tuple[0][3])
# print(n_tuple[1][1])

# num = int(input("Enter any number: "))

# dic1 = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
# dic2 = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
# dic3 = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 100: "Hundred"}
#
# num = int(input("Enter any number: "))
# # print(num)
#
# word = ""
# length = len(str(num))
# last = int(str(num)[-1])
# # print(last)
# last_two = int(str(num)[length - 2: length])
# # print(last_two)
#
# if last_two not in dic2:
#     # for units
#     val1 = num % 10
#     # print(val1)
#     if val1 != str(0):
#         units = dic1.get(val1)
#         word += " " + str(units) + "."
#
# # else:
# #     word = str(dic1.get(last))
# # print(word)
# # num //= 10
#
# if last_two not in dic2:
#     # for tens
#
#     val2 = num % 10
#     if str(val2) == str(0):
#         val_2 = val2
#     elif str(val2) != str(0):
#         val_2 = str(val2) + str(0)
#         # print(val_2)
#         tens = dic3.get(int(val_2))
#         # print(tens)
#         word = str(tens) + word
#         # print(word)
#
#
# elif last_two in dic2:
#     tens = dic2.get(int(last_two))
#
#     word = str(tens) + word
#
#
# num //= 10
#
# # for hundreds
#
# val3 = num % 10
# if str(val3) != str(0):
#     hundreds = dic1.get(val3)
#     word = str(hundreds) + " Hundreds and " + word
#     # print(word)
#
# num //= 10
#
# # for thousands
#
# val4 = num % 10
# if str(val4) != str(0):
#     thousands = dic1.get(val4)
#     word = str(thousands) + " Thousands " + word
#     print(word)

# program to swap the elements of two lists without using a temporary variable

# list1 = [[1, 2, 3], 2, 3, 4, 6]
# list2 = ["a", "b", 77]
# #
# length_list1 = len(list1)
# length_list2 = len(list2)
# # print(length_list1)
# # print(length_list2)
# for a in list2:
#     list1.insert(0, a)
#
# for b in list1:
#     popped_value = list1.pop(length_list2)
#     list2.insert(0, popped_value)
#
# for c in list1:
#     if c in list2:
#         list2.remove(c)
#
# list1.reverse()
# list2.reverse()
# print(list1)
# print(list2)

# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9]
# list3 = []
# for i in list1:
#     list3.append(i)
#     list1.remove(i)
# for a in list2:
#     list1.append(a)
#     list2.remove(a)
#
# for b in list3:
#     list2.append(b)
#
# print(list1)
# print(list2)

# from msvcrt import getch
# from getch import getch
# string = 'Please predict the answer'
# y = ""
# counter = 0
# for i in range(len(string)):
#     x = getch()
#     if x.decode() != "/":
#         print(x.decode())
#     elif x.decode() == "/":
#         print(string[counter])
#         counter += 1
#         while x.decode() == "/":
#             z = getch()
#             counter += 1
#             print(string[counter - 1])
#             if z.decode() == "/":
#                 break
#             else:
#                 y = y + z.decode()
#
# print(y)

# list1 = []
# list2 = []
# print("For first list")
# for a in range(4):
#     num = int(input("Enter any number to add in first list: "))
#     list1.append(num)
# print("For second list")
# for b in range(4):
#     num2 = int(input("Enter any number to add in second list: "))
#     list2.append(num2)
#
# for i in range(len(list1)):
#     list1[i] = list1[i] + list2[i]
#     list2[i] = list1[i] - list2[i]
#     list1[i] = list1[i] - list2[i]
#
# print(list1)
# print(list2)

# list1 = []
# for i in range(1, 6):
#     num = int(input("Enter the {} number: ".format(i)))
#     list1.append(num)
# sorted_list = []
# for i in range(len(list1)):
#     x = list1[0]
#     for j in range(1, len(list1)):
#         if list1[j] < x:
#             x = list1[j]
#     sorted_list.append(x)
#     list1.remove(x)
# print(sorted_list)

# ascending order
# list1 = []
# list_length = int(input("Enter the length for your list: "))
# for i in range(list_length):
#     x = int(input("Enter the number to add in your list: "))
#     list1.append(x)
# print("Before swap", list1)
# for i in range(len(list1)):
#     for j in range(i, len(list1)):
#         if list1[j] < list1[i]:
#             list1[i] = list1[i] + list1[j]
#             list1[j] = list1[i] - list1[j]
#             list1[i] = list1[i] - list1[j]
#
# print("After swap", list1)


# for descending order
# list1 = []
# list_length = int(input("Enter the length for your list: "))
# for i in range(list_length):
#     x = int(input("Enter the number to add in your list: "))
#     list1.append(x)
# print("Before swap", list1)
# for i in range(len(list1)):
#     for j in range(i, len(list1)):
#         if list1[j] > list1[i]:
#             list1[i] = list1[i] + list1[j]
#             list1[j] = list1[i] - list1[j]
#             list1[i] = list1[i] - list1[j]
#
# print("After swap", list1)

# lst = [1, 2, 3, 4, 5]
# max_value = max(lst)
# min_value = min(lst)
# min_count = 0
# max_count = 0

# if max_value != min_value:
#     for i in lst:
#         if i != min_value:
#             max_count += i
#     for j in lst:
#         if j != max_value:
#             min_count += j
# if max_value == min_value:
#     for i in range(len(lst) - 1):
#         min_count += lst[i]
#         max_count += lst[i]
# print(max_count)
# print(min_count)

# heights = [3, 3, 2, 1]
# highest_candles = 0
# maxi = max(heights)
# for i in heights:
#     if i == maxi:
#         highest_candles += 1
# print(highest_candles)

# s = "12:05:45AM"
#
#
# def timeConversion(s):
#     part = s[8:]
#     hours = int(s[0:2])
#     total = hours + 12
#     if part == "PM":
#         if total != 24:
#             return str(total) + s[2:8]
#         elif total == 24:
#             return s[:8]
#     elif part == "AM":
#         if total != 24:
#             return s[:8]
#         elif total == 24:
#             return "00" + s[2:8]
#

# def gradingStudents(grades):
#     round_off = []
#     for i in grades:
#         five_multiple = ((i // 5) + 1) * 5
#         if i >= 38 and (five_multiple - i) < 3:
#             round_off.append(five_multiple)
#         elif i >= 38 and (five_multiple - i) >= 3:
#             round_off.append(i)
#         elif i < 38:
#             round_off.append(i)
#     return round_off

# tup = ()
# tup_list = list(tup)
# for i in range(1, int(input("Enter length of tuple: ")) + 1):
#     x = int(input("Enter {} element to add in tuple: ".format(i)))
#     tup_list.append(x)
# tup = tuple(tup_list)
# mini = tup[0]
# maxi = tup[0]
# for i in tup:
#     if i < mini:
#         mini = i
#     elif i > maxi:
#         maxi = i
#
# print("The minimum value is: ", mini)
# print("The maximum value is: ", maxi)

# dic = {}
# word = input("Enter any word: ")
# for i in range(len(word)):
#     if word[i] != " ":
#         dic[word[i]] = 0
#     for j in range(len(word)):
#         if word[i] == word[j]:
#             dic[word[i]] += 1
#
# print(dic)

# dic = {}
# word = input("Enter any word or sentence: ")
# dic["Spaces"] = 0
# for i in range(len(word)):
#     x = word[i]
#     if x != " ":
#         dic[x] = 0
#         for j in range(len(word)):
#             if x == word[j] and x != " ":
#                 dic[x] += 1
#     elif x == " ":
#         dic["Spaces"] += 1
#
#
# print(dic)

# s = 7
# t = 11
# a = 5
# b = 15
# m = 3
# n = 2
#
# apple = [-2, 2, 1]
# orange = [5, -6]
# apple_count = 0
# orange_count = 0
# for i in apple:
#     z = i + a
#     if z >= s and z <= t:
#         apple_count += 1
# for j in orange:
#     y = j + b
#     if y >= s and y <= t:
#         orange_count += 1
#
# print(apple_count)
# print(orange_count)

# def kangaroo(x1, v1, x2, v2):
#     if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
#         return "YES"
#     else:
#         return "NO"

# a = [2, 6]
# b = [24, 36]
# counter = 0
# for i in range(a[-1], b[0] + 1):
#     cond1 = 0
#     for x in a:
#         if i % x != 0:
#             cond1 = 1
#             break
#     cond2 = 0
#     for y in b:
#         if y % i != 0:
#             cond2 = 1
#             break
#     if cond1 == 0 and cond2 == 0:
#         counter += 1
#
# print(counter)

# scores = [10]
# highest_record = 0
# lowest_record = 0
# high = scores[0]
# low = scores[0]
# for i in scores:
#     if i > high:
#         high = i
#         highest_record += 1
#     elif i < low:
#         low = i
#         lowest_record += 1
# print(highest_record)
# print(lowest_record)

# num = int(input("Enter any number: "))
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(str(i), "\t*\t", str(num // i), "\t=\t", num)


# data = 50
#
# try:
#     data = data / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero", end="")
# else:
#     print("Division successful", end="")
#
# try:
#     data = data / 5
# except:
#     print("Inside except block", end="")
# else:
#     print("GFG", end="")

# In this code....first...the try block executes and since the number can't be divided by zero than the except block
# executed and printed cannot divide by zero
# Since the try block don't ran properly else part doesn't executed

# in the second try block...data is divisible by 5 so that the try block run...no exception raised....then it goes
# straight to the else block and print GFC

# Since end="" is used in the exception block, so line doesn't terminate and GFC is printed in the same line

# code 2

# value = [1, 2, 3, 4]
# data = 0
#
# try:
#     data = value[3]
# except IndexError:
#     print("CSIT Index Error", end="")
# except:
#     print('NEDUET IndexError ', end='')
# finally:
#     print('Python IndexError ', end='')
#
# data = 10
# try:
#     data = data/0
# except ZeroDivisionError:
#     print('CSIT ZeroDivisionError ', end='')
# finally:
#     print('Python ZeroDivisionError ')

# since there is not error in the try block then the exception will not be raised...then the finally block will print
# after that since the data is not divisible by zero than it will raise exception and print the line in exception block
# after that finally block will be executed
# since the end="" is used after every print...so line will not be terminated


# create a program to find the inverse of 2 x 2 matrix

# matrix = []
# for i in range(1, 3):
#     mat = []
#     for j in range(1, 3):
#         x = int(input("Enter numbers to add in {} row: ".format(i)))
#         mat.append(x)
#     matrix.append(mat)
# print("Your Matrix is: ", matrix)
# determinant = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
# print("The determinant of the matrix is: ", determinant)
#
# if determinant == 0:
#     print("The Inverse of Singular matrix is not possible.")
# else:
#     # for the adjoin
#     matrix[0][0], matrix[1][1] = matrix[1][1], matrix[0][0]
#     # print(matrix)
#
#     matrix[0][1] = matrix[0][1] * -1
#     matrix[1][0] = matrix[1][0] * -1
#     print("The Adjoint of your matrix is: ", matrix)
#
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             # matrix[i][j] = str(matrix[i][j]) +  "/" + str(determinant)
#             matrix[i][j] = matrix[i][j] / determinant
#     print(matrix)

# s = "DDUUDDUDUUUD"
# count = 0
# sea_level = 0
# for i in s:
#
#     if i == "U":
#         sea_level += 1
#     elif i == "D":
#         sea_level -= 1
#     if sea_level == 0 and i == "U":
#         count += 1
# print(count)

# b = 5
# maxi = -1
# keyboard = [4]
# drives = [5]
#
# for i in keyboard:
#     for j in drives:
#         if i + j <= b:
#             maxi = max(maxi, i + j)
#
# print(maxi)

# def det2x2(matrix):
#     """ This functions returns the determinant of 2 x 2 matrix """
#     det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
#     return det
#
#
# mat = []
# for x in range(1, 4):
#     mat1 = []
#     for y in range(1, 4):
#         z = int(input("Enter number of {} row {} element: ".format(x, y)))
#         mat1.append(z)
#     mat.append(mat1)
# print(mat)
#
# a = [i[1:] for i in mat[1:]]
#
# b = [j[::2] for j in mat[1:]]
# c = [k[:2] for k in mat[1:]]
#
# determinant = (mat[0][0] * det2x2(a)) - (mat[0][1] * det2x2(b)) + (mat[0][2] * det2x2(c))
#
# if determinant == 0:
#     print("The inverse of singular matrix is not possible")
# else:
#     print("The determinant of matrix is: ", determinant)
#
# adjoint = []
# first = []
# second = []
# third = []
# for e in range(3):
#     for f in range(3):
#         element = 1
#         if e == 0 and f == 0:
#             element *= det2x2([h[1:] for h in mat[1:]]) * 1
#             first.append(element)
#         elif e == 0 and f == 1:
#             element *= det2x2([h[::2] for h in mat[1:]]) * (-1)
#             first.append(element)
#         elif e == 0 and f == 2:
#             element *= det2x2([h[:2] for h in mat[1:]]) * 1
#             first.append(element)
#         elif e == 1 and f == 0:
#             element *= det2x2([h[1:] for h in mat[::2]]) * (-1)
#             second.append(element)
#         elif e == 1 and f == 1:
#             element *= det2x2([h[::2] for h in mat[::2]]) * 1
#             second.append(element)
#         elif e == 1 and f == 2:
#             element *= det2x2([h[:2] for h in mat[::2]]) * (-1)
#             second.append(element)
#         elif e == 2 and f == 0:
#             element *= det2x2([h[:2] for h in mat[:2]]) * 1
#             third.append(element)
#         elif e == 2 and f == 1:
#             element *= det2x2([h[::2] for h in mat[:2]]) * (-1)
#             third.append(element)
#         elif e == 2 and f == 2:
#             element *= det2x2([h[:2] for h in mat[:2]]) * 1
#             third.append(element)
#
# adjoint.append(first)
# adjoint.append(second)
# adjoint.append(third)
# print("The adjoint of matrix is:", adjoint)
# for i in range(3):
#     for j in range(3):
#         adjoint[i][j] = adjoint[i][j] / determinant
# print("The inverse of matrix is: ", adjoint)

# important commands for the installation of mysql
# you ahve to install libssl with command sudo apt-get install libssl-dev
# then use in the terminal of virtual project pip install mysql
# then use the command pip install mysql-connector
# this will work Insha Allah

# i will make a program to find out the magic square for n terms in range

# mat = [[4, 5, 8], [2, 4, 1], [1, 9, 7]]
# ans = 0
# for i in range(3):
#     num = abs(sum(mat[i]) - 15)
#     ans += num
#
# print(ans)

# try:
#     user = int(input("Enter the range of the square: "))
#     if user % 2 == 0:
#         raise Exception
#
# except Exception:
#     print("Please Enter a Odd number.")
#
# else:
#     mat = []
#     for a in range(user):
#         mat1 = []
#         for b in range(user):
#             mat1.append(0)
#         mat.append(mat1)
#
#     ith_list = [0, 0]
#     jth_list = [0, 0]
#     for i in range(1, (user ** 2) + 1):
#         if i == 1:
#             ith = user // 2
#             jth = user - 1
#             mat[ith][jth] += i
#             ith_list.append(ith)
#             jth_list.append(jth)
#         else:
#             ith = ith_list[i] - 1
#             jth = jth_list[i] + 1
#             if ith == -1 and jth == user:
#                 ith = 0
#                 jth = user - 2
#                 if mat[ith][jth] == 0:
#                     mat[ith][jth] += i
#                     ith_list.append(ith)
#                     jth_list.append(jth)
#                 else:
#                     ith = ith + 1
#                     jth = j - 2
#                     mat[ith][jth] += i
#                     ith_list.append(ith)
#                     jth_list.append(jth)
#             elif ith != -1 and jth != user:
#                 if mat[ith][jth] == 0:
#                     mat[ith][jth] += i
#                     ith_list.append(ith)
#                     jth_list.append(jth)
#                 elif mat[ith][jth] != 0:
#                     ith = ith + 1
#                     jth = jth - 2
#                     mat[ith][jth] += i
#                     ith_list.append(ith)
#                     jth_list.append(jth)
#             else:
#                 if ith == -1:
#                     ith = user - 1
#                     if mat[ith][jth] == 0:
#                         mat[ith][jth] += i
#                         ith_list.append(ith)
#                         jth_list.append(jth)
#                     elif mat[ith][jth] != 0:
#                         ith = ith + 1
#                         # print(ith, jth)
#                         mat[ith][jth] += i
#                         ith_list.append(ith)
#                         jth_list.append(jth)
#                 elif jth == user:
#                     jth = 0
#                     if mat[ith][jth] == 0:
#                         mat[ith][jth] += i
#                         ith_list.append(ith)
#                         jth_list.append(jth)
#                     elif mat[ith][jth] != 0:
#                         jth = jth - 2
#                         mat[ith][jth] += i
#                         ith_list.append(ith)
#                         jth_list.append(jth)
#
#     # print(jth_list[2:])
#     # print(ith_list[2:])
#
#     const = sum(mat[0])
#     ans = ""
#     for i in range(user):
#         ans += str(mat[i])
#         ans += "\n"
#     print("Your magic matrix is as follows: ")
#     print(ans)
#     print("The sum for rows columns and diagonals of above matrix is: ", const)

# user = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
#
# conditions = [
#     [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
#     [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
#     [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
#     [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
#     [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
#     [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
#     [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
#     [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
# ]
# list1 = []
# for i in conditions:
#     sum1 = 0
#     for j, k in zip(i, user):
#         for z in range(3):
#             list1.append(abs(j[z] - k[z]))
# total = []
# r1 = 0
# r2 = 9
# length = len(list1)
# while True:
#     sum2 = sum(list1[r1: r2])
#     total.append(sum2)
#     r1 += 9
#     r2 += 9
#     length -= 9
#     if length == 0:
#         break
# print("Time Minimum code will be: ", min(total))

a = [1, 1, 2, 2, 4, 4, 5, 5, 5]

