"""
Write a Python script that takes input from the user and displays that input back in upper and lower cases.
"""
def convert_string(word):
    upper = word.upper()
    lower = word.lower()
    return f'uppercase:{upper}, lower:{lower}'
    
if __name__ == "__main__":
    inputWord=input("Enter any word")
    result=convert_string(inputWord)
    print(result)