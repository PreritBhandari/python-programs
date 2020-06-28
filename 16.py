"""
Write a Python program to sum all the items in a list.
"""
from functools import reduce
def sum_all(ip_list):
    return reduce(lambda a,b:a+b , ip_list)

if __name__ == "__main__":
    print(sum_all([1,2,3,4,5]))