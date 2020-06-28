"""
Write a Python program to count the occurrences of each word in a given sentence.
"""

def find_string_count(sentence):
    dict={}
    for each in set(sentence):
        dict[each]=sentence.count(each)
    return dict

if __name__ == '__main__':
    inputSentence=input('Enter any Sentence').split()
    result=find_string_count(inputSentence)
    print(result)