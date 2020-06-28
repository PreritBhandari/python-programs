"""
Write a Python program to remove the nth index character from a nonempty string.
"""
def find_string_count(word,remove_index):
    try:
        word_to_list=list(word)
        print(f"Removing index {remove_index} i.e {word_to_list[remove_index]} from the string")
        word_to_list.remove(word[remove_index])
        final_string = ''.join(word_to_list)
        return f"Your New List is {final_string}" 
    except IndexError:
        print('your index is out of range')

if __name__ == '__main__':
    inputWord=input('Enter any Word')
    removeIndex=int(input('Enter the index you want to remove'))
    if inputWord:
        result=find_string_count(inputWord,removeIndex)
    else:
        print("Empty String")
    print(result)