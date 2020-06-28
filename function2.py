"""
. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""
def sum_list(*args):
    return(sum(args))
    
if __name__ == "__main__":
    print(sum_list(8, 2, 3, 0, 7))
