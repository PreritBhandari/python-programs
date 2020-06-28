"""
Write a Python program to create a lambda function that adds 15 to a given
number passed in as an argument, also create a lambda function that multiplies
argument x with argument y and print the result
"""
def  add_num(input_number):
    sum_no= lambda x: x+15
    return sum_no(input_number)
def  mul_nums(num1,num2):
    mul= lambda x,y: x*y
    return mul(num1,num2)
if __name__ == "__main__":
    print(add_num(3))
    print(mul_nums(5,3))