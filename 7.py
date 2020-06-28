"""
Write a Python function that takes a list of words and returns the length of the
longest one.
"""
def longest_string(list_word):
    # max_len=0
    # for each in list_word:
    #     if len(each) > max_len:
    #         max_len=len(each)
    # return max_len
    return len(sorted(list_word,key=len)[-1])       
    
if __name__ == '__main__':
    inputWords=input('Enter Words with space sepration').split()
    result=longest_string(inputWords)
    print(result)

