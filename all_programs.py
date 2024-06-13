# lst = [1,2,4,3,6,8,7]
# n = len(lst)
# new = []
# count = 0
# for x in range(n):
#     count += 1
#     if count not in lst:
#         print(count)



# 1. Reverse String By many method.  (5 methods)

# Inbuilt function
# s = 'ravi is python developer'
# a = "".join(reversed(s))
# print(a)

# Slicing
# s = 'ravi is python developer'
# print(s[::-1])

# for loop
# s = 'ravi is python developer'
# reverse = ''
# for x in s:
#     reverse = x + reverse
#
# print(reverse)


# s = "Ravi Is python developer"
# for x in s[::-1]:
#     print(x, end="")


# while loop
# s = 'python developer'
# reverse_str = ''
# count = len(s)
#
# while count > 0:
#     reverse_str += s[count - 1]
#     count = count - 1
# print(reverse_str)

# ---------------------------------------------------------------------------------------
# Reverse List using many method.

# lst = [12,34,56,7,89,2,'ravi','lipne']
# a = lst[::-1]
# print(a)

# lst = [12,34,56,7,89,2,'ravi','lipne']
# lst.reverse()
# print(lst)

# using while looop
# lst = [12,34,56,7,89,2]
# count = len(lst)
# lst1 = []
# while count > 0:
#     lst1.append(lst[count - 1])
#     count = count - 1
# print(lst1)


# using for loop
# lst = [12,34,56,7,89,2]
# lst1 = []
#
# for x in lst[::-1]:
#     lst1.append(x)
# print(lst1)


# lst = [12,34,56,7,89,2]
# count = 0
# lst1 = []
#
# while count < len(lst):
#     if lst[count] > 50:
#         print('you need insurance')
#         count = count + 1
#
#     else:
#         print(lst[count])
#         count = count + 1
# print(lst1)

# ---------------------------------------------------------------
# String manupulation.

# s = "aabbcccddessggtt"
# n = len(s)
# newStr = ""
# count = 1
#
# for i in range(n - 1):
#     if s[i] == s[i + 1]:
#         count += 1
#     else:
#         newStr = newStr + s[i] + str(count)
#         count = 1
# newStr = newStr + s[n-1] + str(count)
# print(newStr)

# -------------------------------------------------------------------
# find pair of elements which match to target.

# new = []
# def pairof(lst, k):
#     while lst:
#         num = lst.pop()
#         diff = k - num
#         if diff in lst:
#             new.append((num,diff))
#     return new
#l
# lst = [1, 2, 5, 7, 8, 4, 10]
# k = 12
# a = pairof(lst, k)
# print(a)

# -------------------------------------------------------------------------
# s = "Ravi_Is_Python_Developer"
# # op: "rAVI.iS.pYTHON.dVELOPER"
# new_str = ""
#
# def str_manu(s):
#     l = []
#     lst = s.split("_")
#     for x in lst: # Ravi
#         l.append(x[0].lower() + x[1:].upper())
#     print(l)
#     strr = ".".join(l)
#     return strr
#
# a = str_manu(s)
# print(a)


# s = "Ravi_Is_Python_Developer"
# # op: "rAVI.iS.pYTHON.dVELOPER"
#
# def str_manu(s):
#     new_str = ""
#     lst = s.split("_")
#     for x in lst: # Ravi rAVI.
#         new_str = new_str + x[0].lower() + x[1:].upper() + "."
#     return new_str[:-1]
# a = str_manu(s)
# print(a)


# s = "Ravi_Is_Python_Developer"
# # op: "rAVI.iS.pYTHON.dVELOPER"
#
# def str_manu(s):
#     new_lst = []
#     lst = s.split("_")
#     for x in lst:
#         new_lst.append(x.swapcase())
#     return ".".join(new_lst)
# a = str_manu(s)
# print(a)

# ------------------------------------------------------------
# Remove consecutive elements from string..

# s = "RRRTFFGWWWHHBWFFF"
# # op: RTFGWHBWF
# n = len(s)
# newStr = ""
# for i in range(n - 1):
#     if s[i] != s[i + 1]:
#         newStr = newStr + s[i]
# newStr = newStr + s[n - 1]
# print(newStr)


# import string
# s = "the quick brown fox jumps over the lazy dog"
# a = string.ascii_lowercase
# for x in s:
#     if x not in a and x != " ":
#         print("Not Palligram")
#         break
# else:
#     print("It is Palligrame")


# -------------------------------------------------------------------------
# 2. check string is pallindrome or not = 4 ways
# s = 'ABCS'
# a = "".join(reversed(s))
# if s == a:
#     print('It is Pallindrome')
# else:
#     print('Not Pallindrome')

#
# s = "ABWA"
# n = len(s)
# x = 0
# for i in range(n):
#     if s[i] != s[n - i - 1]:
#         x = 1
#         break
# if x == 0:
#     print("Its pallindrome")
# else:
#     print("Not")

#
# a = 10
# b = 20
# temp = a
# a = b
# b = temp
# print(a)
# print(b)



# def pallind(s):
#     count = len(s)
#     first = 0
#     last = count - 1
#     while first <= last:
#         if s[first] != s[last]:
#             return False
#         first = first + 1
#         last = last - 1
#     else:
#         return True
# s = "ABA"
# a = pallind(s)
#
# if (a):
#     print("Palll")
# else:
#     print("Not")


# check string word is palli or not...

# s = "My name NITIN Lipne"
# a = s.split()
# sp = a[2]
# if sp == sp[::-1]:
#     print("Yes")
# else:
#     print("No")


# -------------------------------------------------------------------------------
# 3.Check Prime number or not.

# n = int(input('enter num'))
# if n > 1:
#     for x in range(2,n):
#         if n % x == 0:
#             print('Not prime')
#             break
#     else:
#         print('Prime')
# else:
#     print("Not prime number")


# check all prime num in 100 to 200.
# lst = []
# for num in range(100,200):
#     for x in range(2,num):
#         if num % x == 0:
#             break
#     else:
#         lst.append(num)
# print(lst)
# print(len(lst))

# --------------------------------------------------------------------------
# 4.Fabbonasi series (3 methods)

# when we want first 10 fibbanci element

# def fab(n):
#     a = 0
#     b = 1
#     print(a)
#     print(b)
#
#     for i in range(2,n):
#         c = a + b
#         a = b
#         b = c
#         print(c)
# fab(10)


# when we want genearte fibboncci till only 10 then

# def fab(n):
#     a,b = 0, 1
#     print(a)
#
#     while b < n:
#         print(b)
#         c = a + b
#         a = b
#         b = c
# fab(10)


# using recursive function.

# def fibbonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return (fibbonacci(n-1)) + fibbonacci((n-2))
# n = 10
# if n <= 0:
#     print("Invalid Input")
# for x in range(n):
#     print(fibbonacci(x))

# ----------------------------------------------------------------------
# sort dictionary

# dic = {123:"ravi", 43:"Komal", 65: "parth"}
# a = sorted(dic)
# dic1 = {}
#
# for i in a:
#     dic1[i] = dic[i]
# print(dic1)
# -------------------------------------------------------------------
# find max value without using inbuild method.

# lst = [1,2,35,4,5,6]
# def maxvalue(lst):
#     a = 0
#     for x in lst:
#         if x > a:
#             a = x
#     print(a)
# maxvalue(lst)

# using reduce function
# from functools import reduce
# lst = [1,2,35,4,5,6]
# print(reduce(lambda a, b: a if a > b else b, lst))


# using inbuilt functon
# test_list = [12, 67, 98, 34]
# test_list.sort()
# print(test_list[-1])


# test_list = [12, 67, 98, 34]
# test_list.sort(reverse=True)
# print(test_list[0])
#
# test_list = [12, 67, 98, 34]
# a = max(test_list)
# print(a)


# Addition all elem in list
# from functools import reduce
# lst = [1,2,3,4,5,6,7,8]
# a = reduce(lambda x,y: x + y, lst)
# print(a)


# --------------------------------------------------------------------
# 5. Factorial of number using recursive method.

# def fact(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * fact(num - 1)
# a = fact(5)
# print(a)

# Factorial of number using iterative method.
# def fact(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1)
#     return fac
# a = fact(6)
# print(a)


# using while loop...
# def factorial(n):
#     if n < 0:
#         return 0
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         fact = 1
#         while n > 1:
#             fact *= n
#             n = n - 1
#         return fact
# a = factorial(10)
# print(a)

# ---------------------------------------------------------------------------
# 6. Permutation of string.

# from itertools import permutations
# s = 'ABA'
# allperm = permutations(s)
#
# for x in list(allperm):
#     print("".join(x))

# -----------------------------------------------------------------------------
# 7.Reverse words in string. (4 methods)

# s = 'ravi is python developer'
# a = s.split()
# lst = " ".join(reversed(a))
# print(lst)

# import re
# s = 'ravi is python developer'
# a = re.findall('\w+', s)
# print(" ".join(reversed(a)))

##### # Using without inbult function

# s = "ravi is python developer"
# def splitw(s, sp = " "):
#     return [s[:s.index(sp)]] + splitw(s[s.index(sp) + 1:]) if sp in s else [s]
# a = splitw(s)
# print(" ".join(reversed(a)))


# s = "ravi is python developer"
# new = []
# sp = " "
# def split(s):
#     for x in s:
#         if x == " ":
#             new.append(s[:s.index(sp)])
#             s = s[s.index(sp) + 1:]
#     else:
#         new.append(s)
# split(s)
# op = " ".join(reversed(new))
# print(op)

# ---------------------------------------------------------------------------------
# Create a dictionary like.. { 11:[‘Manas’,’Pranjal’], 1:....}

# lst = [(11,"Manas"), (11,"Pranjal"),(1,"Parth"), (2,"Lokesh"),(2,"Purvish"), (4,"Jay")]
# dic = {}
# lst1 = []
# for key, value in lst:  # (11,"Manas")
#     if key not in dic:
#         dic[key] = [value]
#     else:
#         dic[key] += [value]
# print(dic)


# currency_prices =[‘EUR 34.5’, ‘EUR 78.5’, ‘EUR 78.4’,’EUR 56.9’]
# lst =[34.5, 78.5, 78.4,56.9]
# new = []
# for x in lst:
#     new.append("EUR " + str(x))
# print(new)


# ---------------------------------------------------------------------------------
# 8.Remove vowels from string.

# s = 'ravi is python developer'
# vowels = ('a','e','i','o','u')
#
# for x in s:
#     if x in vowels:
#         s = s.replace(x,'')
# print(s)

# --------------------------------------------------------------

# def valid_num(grid, row, col, num):
#     # Check if the number is not present in the row.
#     if num in grid[row]:
#         return False
    
#     # Check if the number is not present in the column.
#     for i in range(9):
#         if grid[i][col] == num:
#             return False
    
#     # Check if the number is not present in the 3x3 subgrid.
#     start_row, start_col = 3 * (row // 3), 3 * (col // 3)
#     for i in range(3):
#         for j in range(3):
#             if grid[i + start_row][j + start_col] == num:
#                 return False
    
#     return True

# def solve_sudoku(grid):
#     # Find empty cell
#     for i in range(9):
#         for j in range(9):
#             if grid[i][j] == 0:
#                 for num in range(1, 10):
#                     if valid_num(grid, i, j, num):
#                         grid[i][j] = num
#                         if solve_sudoku(grid):
#                             return True
#                         grid[i][j] = 0
#                 return False
#     return True

# def print_grid(grid):
#     for row in grid:
#         print(" ".join(str(cell) for cell in row))


# grid = [
#     [0, 0, 0, 2, 0, 0, 0, 6, 3],
#     [3, 0, 0, 0, 0, 5, 4, 0, 0],
#     [0, 0, 1, 0, 0, 3, 9, 8, 0],
#     [0, 0, 0, 3, 1, 0, 0, 0, 8],
#     [9, 0, 0, 0, 8, 0, 0, 0, 5],
#     [8, 0, 0, 0, 0, 6, 0, 0, 0],
#     [0, 7, 8, 9, 0, 0, 1, 0, 0],
#     [0, 0, 6, 4, 0, 0, 0, 0, 9],
#     [2, 1, 0, 0, 0, 8, 0, 0, 0]
# ]


# if solve_sudoku(grid):
#     print("Sudoku Solved:")
#     print_grid(grid)
# else:
#     print("No solution exists.")

# ---------------------------------------------------------------
# Replace char in string

# s = "ravi si python developer"
# a = s.replace("r", "A")
# print(a)
#
#
# s = "ravi si python developer"
# def repla(s, old, new):
#     newStr = ""
#     for x in s:
#         if x == old:
#             newStr += new
#         else:
#             newStr = newStr + x
#     return newStr
#
# old = "r"
# new = "A"
# a = repla(s, old, new)
# print(a)

# -----------------------------------------------------------------------------
# 9.print even number word in string.

# s = 'ravi is python developer'
# lst = s.split()
# for x in lst:
#     if len(x) % 2 == 0:
#         print(x)

# -------------------------------------------------------------------------
# 10.Find the length of string.

# s = 'ravi is python developer'
# a = len(s)
# print(a)

# s = 'ravi is python developer'
# count = 0
# for x in s:
#     count = count + 1
# print(count)

# s = 'ravi is python developer'
# count = 0
# for count, x in enumerate(s):
#     pass
# print(count + 1)


# def wish(name):
#     if name == '':
#         return 0
#     else:
#         return 1 + wish(name[1:])
#
# a = wish('ravi')
# print(a)

# -----------------------------------------------------------------
# Check armstrong number or not - sum of all specific number equal to that number

# n = int(input("enter num"))
# def armstrong(n):
#     count = 0
#     for x in str(n):
#         count = count + int(x) ** 3
#
#     return count
# a = armstrong(n)
# if a == n:
#     print("Yes it is armstrong")
# else:
#     print("Not Armstrong")


# n = int(input("enter num"))
# count = 0
# temp = n
# while temp > 0:
#     digit = temp % 10
#     count = count + (digit**3)
#     temp = temp // 10
#
# if count == n:
#     print("It is armstrong")
# else:
#     print("It in not armstrong")


# -------------------------------------------------------------------------------
# calculate number of digits and character in string.
# import string
# str = 'ravi is 23 pyt@hon! deve656loper'
# digit = {}
# char = {}
# sp = []
# specialChar = string.punctuation
#
# for x in str:
#     if x.isalpha():
#         if x in char:
#             char[x] += 1
#         else:
#             char[x] = 1
#     elif x in specialChar:
#             sp.append(x)
#     else:
#         if x in digit:
#             digit[x] += 1
#         else:
#             digit[x] = 1
#
# print(digit)
# print(char)
# print(sp)


# print only duplicate char in string
# str = 'ravi is 23 python deve656loper'
# new_str = ''
#
# for x in str:
#     if str.count(x) > 1:
#         if x not in new_str:
#             new_str = new_str + x
# print(new_str)

# Remove duplicate in list
# lst = [1,2,3,2,7,3,8,4,3,0]
# for x in lst:
#     if lst.count(x) > 1:
#         lst.remove(x)
# print(lst)

# ---------------------------------------------------------------------------
#  Check Spaces In string.

# s = 'ravi is python developer'
# count = 0
# for x in s:
#     if x == ' ':
#         count = count + 1
# print(count)

# How to avoid spaces in string....
# s = 'ravi is python developer'
# for x in s:
#     if x == ' ':
#         s = s.replace(x,'_')
# print(s)

# --------------------------------------------------------------------------
# check frequency of string.

# using dict comprehensions
# s = "ravi is python develloppppper"
# dic = {x:s.count(x) for x in s}
# print(dic)
# print(max(dic, key=dic.get))


# s = 'ravi is python developer'
# dic = {}
# for x in s:
#     if x in dic:
#         dic[x] += 1
#     else:
#         dic[x] = 1
# print(dic)


# maximum frequency charcter in string.....
# s = 'meet me in the meeting hall'
# dic = {}
# count = 0
#
# for x in s:
#     if x in dic:
#         dic[x] += 1
#     else:
#         dic[x] = 1
#
# res = max(dic,key=dic.get)
# print(res)


# using inbuilt function
# from collections import Counter
# s = "tutorial point"
# a = Counter(s)
# print(a)
# print(max(a, key=a.get))


# ---------------------------------------------------------------------------
# check frequency of words in string

# s = "Ravi is python developer and My name is Ravi and Working on python"
# lst = []
# dic = {}
#
# def frew(s, sp=" "):
#     for x in s:
#         if x == sp:
#             lst.append(s[:s.index(sp)])
#             s = s[s.index(sp) + 1:]
#     else:
#         lst.append(s)
#
#     for y in lst:
#         if y in dic:
#             dic[y] += 1
#         else:
#             dic[y] = 1
#     return dic
# a = frew(s)
# print(a)
# --------------------------------------------------------------
# upper to lower and lower to upper string.

# s = 'rAvi is pYthon DeveLopeR'
# a  = s.swapcase()
# print(a)

# s = 'rAvi is pYthon DeveLopeR'
# for x in s:
#     if x.islower():
#         print(x.upper(),end='')
#     else:
#         print(x.lower(),end='')


# s = 'rAvi is pYthon DeveLopeR'
# new_str = ''
# for x in s:
#     if x.islower():
#         new_str = new_str + x.upper()
#     else:
#         new_str = new_str + x.lower()
# print(new_str)

# -------------------------------------------------------------------
# find duplicate char in string.
#
# string = "tutorialspoint"
# duplicates = []
# for x in string:
#     if string.count(x) > 1:
#         if x not in duplicates:
#             duplicates.append(x)
#
# print(duplicates)

# ---------------------------------------------------------------------------
# interchange element in list

# lst = [1,2,3,4,5,6,7]
# lst[0],lst[-1] = lst[-1],lst[0]
# print(lst)


# lst = [1,2,3,4,5,6,7]
# size = len(lst)

# temp = lst[0]
# lst[0] = lst[size - 1]
# lst[size - 1] = temp
#
# print(lst)

# ----------------------------------------------------------------------------
# Leap Year.

# year = 2009
# if (year % 400 == 0) and (year % 100 == 0):
#     print("leap year")
# elif (year % 4 ==0) and (year % 100 != 0):
#     print("leap year")
# else:
#     print("not leap year")


# -----------------------------------------------------------------------
# find second last max value in list.

# s = [1,2,43,23,54,12,76,54,123,43,54]
# a = sorted(s)
# print(a[-2])

# s = [1,2,43,23,54,12,76,54,123,43,54]
# a = [x for x in s if x < max(s)]
# print(max(a))


# Python program to find smallest.
# list1 = [10, 20, 4, 45, 99]
# list1.sort()
# print("Smallest element is:",list1[0])
# --------------------------------------------------------------------
# find duck number or not

# num = int(input("Enter num"))
# s = str(num)
#
# if '0' in s and s[0] != 0:
#     print("Duck number")
# else:
#     print("Not duck number")

# ------------------------------------------------------------------------
# Print even number in list
# lst = [1,12,3,4,23,43,54,65,76,12,31]
# even = []
# odd = []
# for x in lst:
#     if x % 2 == 0:
#         even.append(x)
#     else:
#         odd.append(x)
#
# print(even)
 # print(odd)


# lst = [1,2,3,4,23,43,54,65,76,12,31]
# even = []
# odd = []
# count = 0
#
# while count < len(lst):
#     if lst[count] % 2 == 0:
#         eve n.append(lst[count])
#         count = count + 1
#     else:
#         odd.append(lst[count])
#         count = count + 1
# print(even)
# print(odd)

#
# lst = [1,2,3,4,23,43,54,65,76,12,31,45,65,66]
# count = 0
# greter10 = []
# less10 = []
#
# while count < len(lst):
#     if lst[count] > 10:
#         greter10.append(lst[count])
#         count += 1
#     else:
#         less10.append(lst[count])
#         count += 1
#
# print(greter10)
# print(less10)


# List comperhension.
# list1 = [10, 21, 4, 45, 66, 93]
# even_nos = [num for num in list1 if num % 2 == 0]
# print("Even numbers in the list: ", even_nos)


# list1 = [10, 21, 4, 45, 66, 93]
# a = [x*2 for x in list1]
# print(a)

# ---------------------------------------------------------------------

# pickling ----------

# import pickle
# favorite_foods = ['pizza', 'burger', 'sushi']
# with open('favorite_foods.pkl', 'wb') as file:
#     pickle.dump(favorite_foods, file)

# Unpickling --------------
# import pickle
# with open('favorite_foods.pkl', 'rb') as file:
#     retrieved_foods = pickle.load(file)
# print(retrieved_foods)


# ---------------------------------------------------------------------------
# Replace dic value and key.

# dic1  = {'name':'Ravi','class':12,'age':27,'desg':'Python Developer'}
# dic1 = {value:key for key,value in dic1.items()}
# print(dic1)

# ------------------------------------------
# check string present or not
# test_list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']
# s = "Geek"
# a = [x for x in test_list if s in x]
# print(a)

# -------------------------------------------------------------------------
# make dictionary using two tuples

# tup = ("name", "class", "rollNo")
# tup1 = ("Ravi", 12, 453)
# dic = {}
# for key in tup:
#     for value in tup1:
#         dic[key] = value
#         lst = list(tup1)
#         lst.remove(value)
#         tup1 = lst
#         break
# print(dic)


# make dictionary using two list

# tup =["name", "class", "rollNo"]
# tup1 = ["Ravi",12, 453]
# dic = {}
# for key in tup:
#     for value in tup1:
#         dic[key] = value
#         tup1.remove(value)
#         break
# print(dic)

# ---------------------------------------------------------------------------
# Add Counter to value using enumerate
# lst = ['ravi','lipne','python','java']
#
# for x, counter in enumerate(lst):
#     print(x,counter)

# ----------------------------------------------------------------------
# ascending list  (3 methods)

# lst = [23,21,54,76,43,12,56,34,76]
# lst.sort()
# print(lst)


# ascending order list
# lst = [12,5,4,9,7,20,55,32,41]
# new_lst = []
# while lst:
#     minimum = lst[0]
#     for x in lst:
#         if x < minimum:
#             minimum = x
#
#     new_lst.append(minimum)
#     lst.remove(minimum)
# print(new_lst)


# lst = [1,4,6,23,21,54,76,43,12,56,34,76,22]
# n = len(lst)
# for i in range(n):
#     for j in range(i + 1, n):
#         if lst[i] > lst[j]:
#             lst[i],lst[j] = lst[j],lst[i]
# print(lst)


# -----------------------------------------------------------------------
# descending order list   - (3 methods)

# lst = [23,21,54,76,43,12,56,34,76]
# lst.sort(reverse=True)
# print(lst)


# lst = [12,5,4,9,7,20,55,32,41]
# new_lst = []
# while lst:
#     minimum = lst[0]
#     for x in lst:
#         if x > minimum:
#             minimum = x
#
#     new_lst.append(minimum)
#     lst.remove(minimum)
# print(new_lst)


# lst = [23,21,54,76,43,12,56,34,76,22]
# n = len(lst)
# for i in range(n):
#     for j in range(i + 1, n):
#         if lst[i] > lst[j]:
#             lst[i],lst[j] = lst[j],lst[i]
# print(lst)


# ----------------------------------------------------------------------------
# find unique elements in list.

# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# lst = []
# for x in input_list:
#     if x not in lst:
#         lst.append(x)
# print(lst)


# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# a = set(input_list)
# print(len(a))

# ------------------------------------------------------------------------------------
# Method Overriding on abstract method..

# class A:
#     def sides(self):       # Abstract Method.
#         pass
#
# class triangle:
#     def sides(self):            # Overriding abstract method
#         print('I have 3 sides')
#
# class square:
#     def sides(self):               # Overriding abstract method
#         print('I have 4 sides')
#
# class polygon:                      # Overriding abstract method
#     def sides(self):
#         print('I have 6 sides')
#
#
# T = triangle()
# T.sides()
#
# s = square()
# s.sides()
#
# p = polygon()
# p.sides()


# python does not support method overloading. it run latest method only.
# def product(a, b):
#     p = a * b
#     print(p)

# def product(a, b, c):
#     p = a * b * c
#     print(p)

# def product(a, b, c):
#     p = a + b + c + 10
#     print(p)

# product(4, 5, 5)


# def add(datatype,*args):
#
#     if datatype == 'int':
#         result = 0
#     if datatype == 'str':
#         result = ''
#
#     for x in args:
#         result = result + x
#
#     print(result)
#
# add('str','Hii', ' Hello')
# add('int',2,4)

# -------------------------------------------------------------------------------------
# Decorators in python

# def add(func1):
#     def inner():
#         print('Before Execution')
#         func1()
#         print('After execution')
#     return inner

# @add
# def Hello():
#     print('I am another function')

# Hello()
# ---------------------------------------------------------------------------------------
# Dict Comprehension

# keys = ['a','b','c','d','e']
# values = [1, 2,3,4,5]
# dic = {k:v for k,v in zip(keys,values)}
# print(dic)
#
#
# myDict = {x**2 for x in [1,2,3,4,5,6]}
# print(myDict)
#
#
# dict1 = {x.upper(): x*3 for x in 'coding'}
# print(dict1)

# list comprhension
# a = 10
# b = 20
#
# c = ['a is greater' if a > b else 'b is greater']
# print(c)
# --------------------------------------------------------------------------------------
# class method and static method in python.

# class A:
#     grade = 20
#
#     def __init__(self, name, school):
#         self.Name = name
#         self.School = school
#
#     def update(self):
#         print(self.Name, self.School, self.grade)
#
#     @classmethod
#     def up(cls, grade):
#         cls.grade = grade
#
# A.up(45)
#
# a = A("ravi", "dyp")
# b = A("Rahul", "nutan")
#
# a.update()
# b.update()


# --------------------------------------------------------------------------------
# Shallow copy :
#
# lst = [1,2,3,4]
# lst1 = lst

# lst1[1] = 20000

# print(lst)
# print(lst1)

# print(id(lst))
# print(id(lst1))

#
# # Deep Copy
#
# # Simple example of Deep Copy.
# import copy
# lst = [1,2,3,4]
# lst1 = copy.deepcopy(lst)
#
# lst1[1] = 20000
#
# print(lst)
# print(lst1)
# print(id(lst1))
# print(id(lst))

# ----------------------------------------------------------------------------------------------
# Use *args :
# def add(*nums):
#     c = 0
#     for x in nums:
#         c = c + x
#     print(c)
#
# add(1,2,3,4)


# def Add(**intro):
#
#     for key,values in intro.items():
#         print(key,values)
#
# Add(Name='Ravi',SurName='Lipne',Age = 27)
# Add(Name='Kailsh',SurName='Shinde',Age = 34)

# ------------------------------------------------------------------------------
# Self varible in python..

# class car():
#
#      # init method or constructor
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
#     def show(self):
#         print("Model is", self.model)
#         print("color is", self.color)
#
# a = car("audi a4", "blue")
# a.show()  # same output as car.show(audi)

# --------------------------------------------------------------------------------
# try:
#     a = int(input('Enter a'))
#     b = int(input('Enter b'))
#
#     c = a/b
#     print(c)
#
# except ZeroDivisionError:
#     print('you can not divide by zero')
#
# except ValueError:
#     print('please print number')
#
# finally:
#     print('Good Bye')

# ===========================================================================
# Generate 5 random numbers between 10 and 30
# a = random.sample(range(10,30), 5)
# print(a)

# from random import *
# for x in range(5):
#     print(random())

# for x in range(10):
#     print(randint(10, 30))

# for x in range(12):
#     print(uniform(10,30))


# ==========================================================
# lambda functions: A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# x = lambda a : a + 10
# print(x(5))

# x = lambda  a: a + b
# print(x(10))


# a = 20
# b = 10
# add = lambda x,y: (x+y, x - y, x // y)          # we can use multiple statement with in bracket
# print(add(a,b))


# def myfunc(n):
#   return lambda a : a * n

# a = myfunc(2)
# print(a(11))


# =======================================================================================================
# map() function in python

# lst = [1,2,3,4,5,6,7]
# a = list(map(float, lst))
# print(a)


# def sq(nums):
#     return nums ** 2
# nums = [2, 3, 4, 5, 6, 7]
# a = list(map(sq, nums))
# print(a)

# nums = [1,2,3,4,5,6]
# a = list(map(lambda nums: nums**2, nums))
# print(a)

# ============================================================================
# filter function()

# lst = [1,2,3,4,5,6,7,8,9]
# def new_filter(a):
#     return a > 4
# filter = list(filter(new_filter, lst))
# print(filter)


# lst = [13,45,23,78,45,32]
# a = list(filter(lambda x: x % 2 == 0, lst))
# print(a)

# ====================================================================
# Reduce() function
#
# from functools import reduce
# lst = [2,3,4,5,6,7,8]
# a = reduce(lambda x,y: x + y, lst)
# print(a)
#

# from functools import reduce
# lst = [0,2,35,4,5,96,231,43,563,756,3456]
# maxval = reduce(lambda a,b: a if a > b else b, lst)
# print(maxval)

# =============================================================

# s = 4.5
# if type(s) == str:
#     print("Its String")
# elif type(s) == int:
#     print("Its Integer")
# elif type(s) == float:
#     print("Its Float")
# else:
#     print("Null")

# =============================================================================
# how to read txt file in python
#
# file = open("testfile.txt")
# print(file.read())
# file.close()
#
# file = open("testfile.txt", 'r')
# for line in file:
#     print(line)
#
# file = open("testfile.txt", 'r')
# a = file.read(10)
# print(a)

# ===========================================================================
# Make 0 at the end of the list

# lst = [2,3,0,4,1,6,0,45,34,0]
#
# for x in lst:
#     if x == 0:
#         lst.remove(x)
#         lst.append(x)
# print(lst)

# =============================================================================
# create file with write operation

##### read operation
# file = open("createFile.txt", 'w')
# file.write("Hello i am creating new file with write function")
# file.close()
#
# readFile = open("createFile.txt", 'r')
# print(readFile.read())

# f = open("hello.txt", "r")
# print(f.readline())
# print(f.readline())


# f = open("createFile.txt", "r")
# file = len(f.readlines())
# print(file)


# Open file and fecth some specific chracter

# file = open("hello.txt", "r")
# target_name = "jim"
# lst = []
# for line in file:
#     line = line.strip().lower()
#     if target_name.lower() in line:
#         print("It is prsent")
#         lst.append(target_name)
#         break
# else:
#     print("it is not present")
# print(lst)


# merge two file data into third file

# f = open("hello.txt", 'r')
# first = f.read()
# t = open("testfile.txt", 'r')
# second = t.read()
# first += "\n"
# first += second
# #
# a = open("testfile.txt", 'w')
# a.write(first)
# a.close()


###### write operation

# file = open("createFile.txt", 'w')             # it will remove all code and write
# file.write("xjfkgfdhg")
# file.close()
#
# file = open("createFile.txt", 'a')             # it will add new code end of existing content in file
# file.write("Hello i am append function")
# file.close()
#
# file = open("newCreateFile.txt", 'x')           # to create new file
# file.close()

##### remove file

# import os
# os.remove("newCreateFile.txt")   # to remove or delete file


# import os
# if os.path.exists("newCreateFile.txt"):          # check file is present or not
#   os.remove("newCreateFile.txt")
# else:
#   print("The file does not exist")

#
# import os
# os.rmdir("for loop folder")               # to delete entire folder


# read how many lines present in text file.

# file = open("hello.txt", 'r')
# count = 0
# for x in enumerate(file):
#     count = count + 1
# print(count)

# =========================================================================================
# reverse number

# n = int(input("Enter number: "))
# reverse = 0
# while (n > 0):
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
# print(reverse)


# num = 1232434
# s = str(num)
# a = s[::-1]
# print(int(a))


# def palli(num):
#     rev = 0
#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num = num // 10
#     print(rev)
#
# palli(45564)
# =====================================================
# import  copy
# c = [1,2,3,4,5]
# d = copy.copy(c)
# print(id(c) == id(d))  # False - d is now a new object
# print(id(c[0]) == id(d[0]))  # True - d[0] is the same object as c[0]


# lst = [1,2,3,4,5,6,7]
# a = list(map(lambda x: x**2, lst))
# print(a)

#
# t = [13,45,23,78,45,32]
# a = list(filter(lambda x: x % 2 == 0, t))
# print(a)

# from functools import reduce
# # lst = [2,3,4,65,6,7,8]
# # a = (filter(lambda x,y: x if x > y else y, lst))
# # print(a)


# =-===============================================================================================

# ===========================================================================
# open csv file

# import pandas as pd
# A = pd.read_csv("fruits_names.csv")
# A.loc[7, "Weight"] = 250
# print(A)


# A = pd.read_csv("fruits_names. csv")
# A["Weight"] = A["Weight"].replace({250:2500})
# print(A)


# A = pd.read_csv("fruits_names.csv")
# a = A.loc[7][1]
# print(a)

# A = pd.read_csv("fruits_names.csv")
# A.loc[5, "Fruits"] = "Chiku"
# print(A)

# lst = ["A","B","C","D","E"]
# A = pd.read_csv("fruits_names.csv")
# A.rename(columns= {"Fruits":"A"})
# print(A)


# A = pd.read_csv("fruits_names.csv")
# a = A.isna()
# print(a)
# b = A.dropna(axis=1)
# print(b)

# A = pd.read_csv("fruits_names.csv")
# a = A.duplicated()
# print(a)
# b = A.drop_duplicates()
# print(b)


# A = pd.read_csv("fruits_names.csv")
# a = A.isna().sum()
# print(a)
#
# meanVal = A["price"].mean()
# print("mean of price", meanVal)
#
# A.fillna(value = meanVal, inplace=True)
# print(A)


# A = pd.read_csv("fruits_names.csv")
# a = A.query("price > 190" and "price < 210")
# print(a)

# A = pd.read_csv("fruits_names.csv")
# a = A.nunique()
# b = A["Fruits"].unique()
# print(a)
# print(b)

# A = pd.read_csv("fruits_names.csv")
# A.sort_values("Fruits", inplace=True)
# print(A)
#
# A = pd.read_csv("fruits_names.csv")
# A.sort_values("Fruits", ascending=False, inplace=True)
# print(A)

# ------------------------------------------------------------------------------------------------
# use multiple decorators in two functions

# def lowerf(fun2):
#     a = fun2()
#     lowe = a.lower()
#     return lowe
#
# def upperf(fun1):
#     b = fun1
#     upp = b.upper()
#     return upp
#
# @upperf         # here we have to use fun1 as varible like fun1 = "hello ravi"
# @lowerf      #firstly we have to run this method and use decorator function like fun2(), it return string to upperf()
# def stringf():
#     return "hello RaVI"
#
# print(stringf)


# st1 = {'A', 'B', 'C'}
# st2 = {'B', 'C', 'D'}
# print(st2 ^ st1)

# lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# temp = [x for num in lst for x in num]
# print(temp)

# lst = [[1, 2, 3],  [4, 5], [6, 7, 8, 9]]
# a = [x for num in lst for x in num]
# print(sum(a))
# -------------------------------------------------------------------------------------------------
# Fetch specific data from nested dictionary.
# Dep= [
#     {'Purchase': ['John', 'Avery', 'Obama'], 'Sales': ['Orea', 'Stark']},
#                        {'Purchase': [2000, 4000, 10000], 'Sales': [2344, 32442]}]

# a = Dep[0]["Sales"][0]
# print(a)

# dic = {"name":"ravi", "sur":"lipne", "class":12}
# print(dic["class"])

# ------------------------------------------------------------------
# We can use another .py file data using import them.

# import interviews
# def fun1():
#     print("Hello Ravi")
#     interviews.msg()
#     print("Good morning")
# fun1()

# --------------------------------------------------------------------
# * How to iterate multiple string simultaneously.
#
# name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
# animal = ['Cat', 'Dog', 'Fish', 'Goat']
# age = [1, 2, 2, 6]
#
# z = zip(name,animal,age)
#
# for x,y,z in z:
#     print(x,y,z)

# ----------------------------------------------------------------------------
# 4. calculate simple interest.

# P = int(input('enter principlee amount'))
# T = int(input('enter time'))
# R = int(input('enter rate '))
#
# def simpleInt(P,T,R):
#
#     si = (P * T * R)/ 100
#     print(si)
#
# simpleInt(P,T,R)

# --------------------------------------------------------------------
# find area of circle
# radius = int(input("Entre radius"))
#
# def areAOfCircle(radius):
#     pi = 3.142
#     return pi * (radius**2)
#
# a = areAOfCircle(radius)
# print(a)

# ----------------------------------------------------------------------------
# * Implicit type conversion.

# a = 10
# b = 2.5
# c = a + b
# print(type(a))
# print(type(b))
#
# c = a + b
# print(c)
# print(type(c))

# * Explicit type conversion.

# a = 150
# b = '350'
# c = int(b)
# print(type(c))
#
# print(a+c)

# -----------------------------------------------------------------------------
# Check value data types
#
# year = 1 + 2J
#
# if type(year) == int:
#     print("integer")
# elif type(year) == str:
#     print("String")
# elif type(year) == float:
#     print("Its Float")
# elif type(year) == bool:
#     print("its boolean value")
# elif type(year) == complex:
#     print("its complex value")
# else:
#     print("all correct")


# -------------------------------------------------------------------------
# Generate random number

# from random import *

# random(): used to generate random number below 0.
# a = random()
# print(a)

# for x in range(10):
#     print(random())


# randint(): used to generate random number from one value to another.
# a = randint(1,10)
# print(a)

# for x in range(10):
#     print(randint(1,100))


# uniform(): used to generate float value between two value
# a = uniform(1,10)
# print(a)

# for x in range(10):
#     print(uniform(10,50))


# generate random char in string
# import random
# s = "ravi is python developer"
# a = random.choice(s)
# print(a)

# fetch only limited numbers as per our requirements
# import string
# import random
# a = string.printable
# print("".join(random.sample(a, 5)))

# ---------------------------------------------------------------------
# Super() function

# class A:
#     def msg(self):
#         print("I am msg function")
#
# class B(A):
#     def wish(self):
#         print("I am wish function")
#         super().msg()
#
# x = B()
# x.wish()

# -------------------------------------------------------------------------------
# Addition of element present in the list.

# lst = ['123','456','789']
# count = 0
# for x in lst:
#     for y in x:
#         count = count + int(y)
# print(count)


# lst = ['123','456','789']
# a = [int(y) for x in lst for y in x]
# print(sum(a))
# ---------------------------------------------------------------
# generate rando password

# import string
# import random
#
# a = string.ascii_lowercase          # All Lower case charcters
# b = string.ascii_uppercase          # All upper case charcters
# c = string.punctuation              # All Special symbols
# d = string.ascii_letters            # fetch All upper and lower case char
# e = string.digits                   # fetch only numbers  ( 0123456789 )
# p = string.printable                # to fetch all lowercase, upper case, number(0,9) , special symbols
#
# passw = "".join(random.choice(p) for x in range(12))
# print(passw)


# import string
# import random
# s = string.printable
# a = "".join(random.sample(s, 5))
# print(a)


# find special char is present in string or not.
# import string
# s = "ravi is python developer"
# a = string.punctuation
#
# for x in s:
#     if x in a:
#         print("Yes special char is present")
#         break
# else:
#     print("not present")


# import string
# import random
#
# a = string.ascii_lowercase
# b = string.ascii_uppercase
# sec = "".join(random.choice(b) for y in range(1))
# first = "".join(random.choice(a) for x in range(9))
#
# passw = sec + first
# print(passw)


# ------------------------------------------------------------
# Remove punctuation in string

# import string
# s = "ravi& is py$thon De@velope!r"
# a = string.punctuation
# for x in s:
#     if x in a:
#         s = s.replace(x, "")
# print(s)


# ==========================================================================
# ==========================================================================
# ==========================================================================
# ==========================================================================
# ==========================================================================
# ==========================================================================

# def pye(n):
#     for i in range(n):
#         for j in range(i+1):
#             print("* ", end="")
#         print("\r")
# pye(5)


# for x in range(5):
#     print("*" * (x + 1))
# print("\r")


# def pye(n):
#     for i in range(0, n):
#         print("* " * (i + 1), end="")
#         print("\r")
# pye(5)


# def pye(n):
#     for i in range(n):
#         print("* " * (n), end="")
#         n = n - 1
#         print("\r")
# pye(5)


# Function to demonstrate printing pattern triangle
# def triangle(n):
#     k = n - 1
#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0, i + 1):
#             print("* ", end="")
#         print("\r")
# n = 10
# triangle(n)

# practice questions

# # sum of element 12 = 3, 67 = 13
# test_list = [12, 67, 98, 34]
# lst = []
# count = 0
# for x in test_list:
#     for y in str(x):
#         count += int(y)
#     lst.append(count)
#     count = 0
# print(lst)




# =============================================================================================
# Working on API

# get api data and change in fields
# import requests
# responce = requests.get("https://jsonplaceholder.typicode.com/users")
# data = responce.json()
#
# lst = []
# for item in data:
#     item['address']['zipcode'] = item['address']['zipcode'].replace("-", "")
#
# for item in data:
#     lst.append(item)
# print(lst)



# import requests
# import json
#
# # Define the API endpoint URL for creating a new to-do item
# api_url = "https://example.com/api/todos"
#
# # Create a Python dictionary with the data for the new to-do item
# data_to_post = {
#     "title": "Buy groceries",
#     "completed": False
# }
#
# # Convert the dictionary to a JSON string
# json_data = json.dumps(data_to_post)
#
# # Define headers if needed (e.g., for authentication or specifying content type)
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "Bearer YOUR_ACCESS_TOKEN"
# }
#
# try:
#     # Send an HTTP POST request to create a new to-do item
#     response = requests.post(api_url, data=json_data, headers=headers)
#
#     # Check if the request was successful (status code 200 or 201 for most APIs)
#     if response.status_code == 200 or response.status_code == 201:
#         response_data = response.json()
#         print("New to-do item created:", response_data)
#     else:
#         print(f"Error: Failed to create a new to-do item. Status Code: {response.status_code}")
# except Exception as e:
#     print(f"An error occurred: {str(e)}")



# ------------------------------------------------------------------------
# convert dic  data into json using dump functon

# import json 
# dict1 ={ 
# 	"emp1": { 
# 		"name": "Lisa", 
# 		"designation": "programmer", 
# 		"age": "34", 
# 		"salary": "54000"
# 	}, 
# 	"emp2": { 
# 		"name": "Elis", 
# 		"designation": "Trainee", 
# 		"age": "24", 
# 		"salary": "40000"
# 	}, 
# } 

# # the json file where the output must be stored 
# out_file = open("myfile.json", "w") 

# json.dump(dict1, out_file, indent = 6) 

# out_file.close() 





# OOPS Concept practical coding question
# ========================================================================================================



# ************* Abstarct class and method ***********

# from abc import ABC, abstractmethod
# class A(ABC):
#     @abstractmethod
#     def size(self):
#         pass

# class triangle(A):
#     def size(self):
#         print("I have 2 sides")

# class square(A):
#     def size(self):
#         print("I have 4 side")

# c = triangle()
# c.size()

# d = square()
# d.size()




# from abc import ABC, abstractmethod
# class Vahicle(ABC):

#     def __init__(self, name, model):
#         self.Name = name
#         self.Model = model

#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class CAR(Vahicle):

#     def start(self):
#         print(self.Name ,"is starting")

#     def stop(self):
#         print(self.Name, "is going to stop")    
    
# class Mororcycle(Vahicle):

#     def start(self):
#         print(self.Name, "is starting")

#     def stop(self):
#         print(self.Name, "is going to stop") 

# car = CAR("Hyundai", "i10")
# car.start()
# car.stop()

# bike = Mororcycle("shine", "125")
# bike.start()
# bike.stop()



# ************* static methods ************
# board = [[7, 9, 2, 1, 5, 4, 3, 8, 6], 
#         [6, 4, 3, 8, 2, 7, 1, 5, 9],
#         [8, 5, 1, 3, 9, 6, 7, 2, 4],
#         [2, 6, 5, 9, 7, 3, 8, 4, 1],
#         [4, 8, 9, 5, 6, 1, 2, 7, 3],
#         [3, 1, 7, 4, 8, 2, 9, 6, 5],
#         [1, 3, 6, 7, 4, 8, 5, 9, 2],
#         [9, 7, 4, 2, 1, 5, 6, 3, 8],
#         [5, 2, 8, 6, 3, 9, 4, 1, 7]]


# def is_valid_sudoku(board):
#     for row in board:
#         if len(set(row)) != len(row):
#             return False

#     for col in zip(*board):
#         if len(set(col)) != len(col):
#             return False

#     for i in range(0, 9, 3):
#         for j in range(0, 9, 3):
#             sub_matrix = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
#             if len(set(sub_matrix)) != len(sub_matrix):
#                 return False

#     return True

# if is_valid_sudoku(board):
#     print("Valid")
# else:
#     print("Not valid")




# def pairOf(lst):
#     new = []
#     while lst:
#         num = lst.pop()
#         diff = k - num
#         if diff in lst:
#             new.append((num, diff))

#     return new

# k = 12
# lst = [1, 2, 5, 7, 8, 4, 10]
# a = pairOf(lst)
# print(a)
