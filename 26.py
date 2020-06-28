"""
Write a Python program to insert a given string at the beginning of all items in a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
"""
def string_input(input_list,insert_str):
    for i in range(len(input_list)):
        input_list[i]=insert_str + str(input_list[i])
    return input_list

if __name__ == "__main__":
    print(string_input([1,2,3,4],'emp'))
    