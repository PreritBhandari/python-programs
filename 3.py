"""
Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""
def change_characters(word):
    first_letter = word[0]
    for i in range(len(word)-1):
        list_word=list(word)
        if i != 0:
                if list_word[i]==first_letter:
                    list_word[i] = '$'
    return ''.join(list_word)

if __name__== '__main__':
    input_word=input('Enter any word')
    result = change_characters(input_word)
    print(result)
