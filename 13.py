"""
13. Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
"""
def sort_csv(csv_list):
    csv_list = sorted(set(csv_list))
    return f"Sorted List is:{','.join(csv_list)}"
    
if __name__ == '__main__':
    inputCsv=input('Enter CSV').split(',')
    result=sort_csv(inputCsv)
    print(result)