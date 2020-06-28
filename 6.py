"""
Write a Python program to find the first appearance of the substring 'not' and
'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""
def find_string_count(sentence):
    if 'not' in sentence and 'poor' in sentence:
        list_word=sentence.split()
        index_of_not=list_word.index('not')
        list_without_not=list_word[0:index_of_not]
        final_list=list_without_not+['good!']
        return ' '.join(final_list)
    else:
        return sentence

if __name__ == '__main__':
    inputWords=input('Enter Sentence')
    result=find_string_count(inputWords)
    print(result)