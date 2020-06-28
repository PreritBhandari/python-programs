"""
Write a Python program to sort a list of tuples using Lambda.
"""
def sort_tuple(input_tuple):
    check = lambda x:sorted(x)
    return tuple(check(input_tuple))
if __name__ == "__main__":
    print(sort_tuple((6,2,3,7,8,1,4,5)))