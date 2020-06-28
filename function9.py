"""
Write a Python function that takes a number as a parameter and check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive
divisors other than 1 and itself
"""
def check_prime(input_number):
    if input_number <0:
        return f'Enter Positive'
    if  input_number==0 and input_number==1:
        return f'Neither Prime Nor Composite'
    check = lambda x: (x % i != 0  for i in range(2,input_number))
    if all(check(input_number)):
        return f'Prime'
    return 'Composite'
    
if __name__ == "__main__":
    print(check_prime(int(input("Enter any No."))))