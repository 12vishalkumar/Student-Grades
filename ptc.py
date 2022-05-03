import math
import os
import random
import re
import sys

# Complete the 'gradingStudents' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
def gradingStudents(grades):
    # Write your code here
    for i in grades:
        if(i <= 35):
            print(i)
        elif(i%5 == 0):
            print(i)
        elif((5-i%5)>=3):
            print(i)
        elif((5-i%5)<3):
            print((i+(5-i%5)))
        
if __name__ == '__main__':
    n = int(input())
    grades = []
    for i in range(n):
        grades.append(int(input()))
    gradingStudents(grades)