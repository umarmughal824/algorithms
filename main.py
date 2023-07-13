#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getSubstringCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def groupingExists(string):
    l = []
    l.append(string[0])
    for i in range(1, len(string)):
        if l:
            if string[i] == l[len(l) - 1]:
                l.append(string[i])
            else:
                l.pop()
        else:
            return False
    if len(l) == 0:
        return True
    return False


def getSubstringCount(s):
    # Write your code here
    total = 0
    result = []
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            string = ""
            for k in range(i, j + 1):
                string += s[k]
            result.append(string)
    
    for i in range(len(result)):
        current = result[i]
        
        if groupingExists(current):
            total += 1
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = getSubstringCount(s)

    fptr.write(str(result) + '\n')

    fptr.close()









#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING input_str as parameter.
#

from collections import Counter


def countFrequency(input_str):
    frequencies = dict(Counter(input_str))
    frequencies = dict(sorted(frequencies.items(), key=lambda item: -item[1]))
    # print(frequencies)
    return frequencies


def getString(input_str):
    # Write your code here
    frequencies = countFrequency(input_str)
    key = next(iter(frequencies))
    while frequencies[key] > 1:
        # key processing the string
        input_str = input_str.replace(key, "", 1)
        frequencies = countFrequency(input_str)
        key = next(iter(frequencies))
    print(input_str)
    return input_str
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    input_str = input()

    result = getString(input_str)

    fptr.write(result + '\n')

    fptr.close()


# hi
# four digits
# combination of + - / *
# to make a 100

# */-+

# 001
# 010
# 011
# 100


# example
# 5 5 5 2
# ( 5 + 5 ) * 5 * 2
# 5 + 5 * 5 * 2

def calculate(num1, num2, oper):
    if oper == "+":
        return num1 + num2
    if oper == "-":
        return num1 - num2
    if oper == "*":
        return num1 * num2
    if oper == "/":
        return num1 / num2
        
            # raise ZeroDivisionError

string = input("Enter four number string")
numbers = [int(char) for char in string]



# 5 + 5 + 5 +
# 5 - 5 - 5

operators = ["+", "-", "*", "/"]

for i in range(len(operators)):
    for j in range(len(operators)):
        for k in range(len(operators)):
            # number = numbers[0] operators[i] numbers[1] operators[j] numbers[2] operators[k] numbers[3]
            try:
                number = calculate(numbers[0], numbers[1], operators[i])
                number = calculate(number, numbers[2], operators[j])
                number = calculate(number, numbers[3], operators[k])
            except ZeroDivisionError:
                continue

            if number == 100:
                print(f"{numbers[0]} {operators[i]} {numbers[1]} {operators[j]} {numbers[2]} {operators[k]} {numbers[3]}") 


assert calculate(5, 6, "+") == 11

assert makeCombination("5552") == "5 + 5 * 5 * 2"

import pytest

with pytest.raises(ZeroDivisionError):
    calculate(5, 0, "/")
