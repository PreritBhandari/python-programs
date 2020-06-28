"""
Write a Python program to get the largest number from a list.
"""
def largest_num(ip_list):
    return sorted(ip_list)[-1]

if __name__ == "__main__":
    print(largest_num([1,2,3,100,111,10]))