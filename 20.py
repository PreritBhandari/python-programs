"""
Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list of
strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""

def string_count(input_list):
    count = 0
    for each in input_list:
        check = lambda each:each[0]==each[-1]
        if check(each):
            count += 1
    return count
if __name__ == "__main__":
    print(string_count(['abc', 'xyz', 'aba', '1221']))