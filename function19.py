"""
Write a Python program to create Fibonacci series upto n using Lambda.
"""
from functools import reduce
def fibo(n):
    pattern=(0,1)
    for _ in range(n-2):
        pattern += (reduce(lambda a,b:a+b,pattern[-2:]),) #IF YOU START WITH 0 IT WILL allways give sum of 1st two element
    return pattern
        
if __name__ == "__main__":
    termsNo=int(input("Enter the no. of terms"))
    print(fibo(termsNo))