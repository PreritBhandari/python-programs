"""Write a Python program to count the number of characters (character
frequency) in a string. Sample String : google.com
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""
def find_string_count(word):
    dict={}
    for each in set(word):
        dict[each]=word.count(each)
    return dict

if __name__ == '__main__':
    inputWord=input('Enter any Word')
    result=find_string_count(inputWord)
    print(result)
