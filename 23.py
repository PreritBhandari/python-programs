"""
Write a Python program to check a list is empty or not.
"""
def check_empty(input_list):
    if not input_list:
        return "Empty List"
    return "Non Empty List"
    
if __name__ == "__main__":
    print(check_empty([]))
    # print(check_empty([1,2]))