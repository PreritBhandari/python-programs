"""
Write a Python program to check whether all dictionaries in a list are empty or not.
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False
"""
def check_empty(input_list):
    for each in input_list:
        if each:
            return False
    return True
if __name__ == "__main__":
    print(check_empty([{},{},{}]))
    print(check_empty([{1,2},{},{}]))
    