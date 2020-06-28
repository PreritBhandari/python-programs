"""
Write a Python function to calculate the factorial of a number (a non-negative
integer). The function accepts the number as an argument.
"""
from functools import reduce
def fact(input_no):
    if input_no > 0:
        return reduce(lambda a,b: a*b,range(1,input_no+1))
    return 'Pass Positive Number'
if __name__ == "__main__":
    print(fact(int(input("Enter any No."))))
