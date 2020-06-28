"""
Write a Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""
def check_string(word):
    if (word[-3:]=='ing'):
        word = word + "ly"
        return word
    elif (len(word)<3):
        return word
    else:
        word=word+'ing'
        return word
if __name__=='__main__':
    input_string=input('Enter the word')
    result=check_string(input_string)
    print(result)
