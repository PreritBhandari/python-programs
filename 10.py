"""
Write a Python program to remove the characters which have odd index values of a given string.
"""
def convert_string(word):
    return word[1:len(word):2]

if __name__ == "__main__":
    inputWord=input("Enter any word")
    result=convert_string(inputWord)
    print(result)