"""
Write a Python program to get a string made of the first 2 and the last 2 chars
from a given a string. If the string length is less than 2, return instead of the
empty string.
Sample String : 'Python'
Expected Result : 'Pyon'
Sample String : 'Py'
Expected Result : 'PyPy'
Sample String : ' w'
Expected Result : Empty String
"""
def construct_new_string(word):

    if len(word)>2:
        a=[]
        a.append(word[0])
        a.append(word[1])
        a.append(word[-2])
        a.append(word[-1])
        return ''.join(a)
    elif len(word)<2:
        return "Empty String"
    else:
        return 2*word

if __name__=='__main__':
    input_string=input('Enter the word')
    result=construct_new_string(input_string)
    print(result)


