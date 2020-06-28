"""
Write a Python program to get the smallest number from a list.
"""
def smallest_num(ip_list):
    return sorted(ip_list)[0]

if __name__ == "__main__":
    print(smallest_num([100,3,12,101,111,10]))