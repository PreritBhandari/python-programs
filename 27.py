"""
Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
"""
def replace_list(list_one,list_two):
    list_one.remove(list_one[-1])
    for each in list_two:
        list_one.append(each)
    return list_one
    
if __name__ == "__main__":
    print(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))