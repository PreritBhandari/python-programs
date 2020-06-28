"""
Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
"""
from functools import reduce 
def mul_list(*args):
    return reduce(lambda a,b: a*b,args)
    
if __name__ == "__main__":
    print(mul_list(8, 2, 3, -1, 7))
