"""
Write a Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""
def swap_string(firststr,secondstr):
    append_list=[]
    firstStrList=list(firststr)
    secondStrList=list(secondstr)
    for i in range(2):
        firstStrList[i],secondStrList[i]=secondStrList[i],firstStrList[i]
    append_list.append(''.join(firstStrList))
    append_list.append(''.join(secondStrList))
    return ' '.join(append_list)

if __name__ == '__main__':
    # inputFirstWord,inputSecondWord=input('Enter 2 words').split()
    result=swap_string('abc','xyz')
    print(result)