"""
Write a Python program to remove duplicates from a list.
"""

def remove_duplicate(input_list):
    return list(set(input_list))
if __name__ == "__main__":
    print(remove_duplicate(['a','b','a',1,2,1,2,'a','c','d']))