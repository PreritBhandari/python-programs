"""
Write a Python function that accepts a string and calculate the number of upper case letters 
and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""
def count_up_low(input_string):
    upper_count=0
    lower_count=0
    for each in input_string:
        for i in range(len(each)):
            if each[i].isupper():
                upper_count+=1
            else:
                lower_count+=1
    return f'No. of Upper case characters : {upper_count}\nNo. of Lower case Characters : {lower_count}'
if __name__ == "__main__":
    print(count_up_low(input("Enter sentence").split()))

