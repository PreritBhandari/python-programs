"""
Write a Python program to change a given string to a new string where the first
and last chars have been exchanged.
"""
def convert_string(word):
    list_word=list(word)
    list_word[0],list_word[-1]=list_word[-1],list_word[0]
    return ''.join(list_word)

if __name__ == "__main__":
    inputWord=input("Enter any word")
    result=convert_string(inputWord)
    print(result)