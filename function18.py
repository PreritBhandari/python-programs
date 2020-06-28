"""
Write a Python program to check whether a given string is number or not using Lambda.
"""
def check_string(input_string):
    check= lambda x:int(x)
    try:
        if check(input_string):
            return f'The input string {input_string} is a number'
    except ValueError:
        return f'The input is not a integer'

if __name__ == "__main__":
    stringCheck=input('Enter any String:')
    print(check_string(stringCheck))