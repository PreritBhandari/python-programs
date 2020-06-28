"""
Write a Python program to multiplies all the items in a list.
"""
from functools import reduce
def mul_all(ip_list):
    return reduce(lambda a,b:a*b , ip_list)


if __name__ == "__main__":
    print(mul_all([1,2,3]))