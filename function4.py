"""
 Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
"""
def reverse_string(input_string):
    return ''.join(reversed(input_string))
    
if __name__ == "__main__":
    print(reverse_string(input('Enter any string')))