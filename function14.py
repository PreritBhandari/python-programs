"""
Write a Python program to sort a list of dictionaries using Lambda.
"""
def sort_dict(input_dict):
    check = lambda x:sorted(x)
    return dict(check(input_dict.items()))
if __name__ == "__main__":
    print(sort_dict({2:20,1:10,4:40,5:50,3:30}))