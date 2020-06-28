"""
Write a Python script to check whether a given key already exists in a dictionary.
"""
def check_key(get_key,rec):
    if get_key in rec:
        return True
    return False
    
          
if __name__ == "__main__":
    inputKey=input('Enter Key you wnat to check')
    print(check_key(inputKey,{'a':1,'b':2,'c':3}))