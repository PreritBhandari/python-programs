"""
Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""
def add_key(input_key,input_value,final_dict):
    final_dict[input_key]=input_value
    return final_dict

    
if __name__ == "__main__":
    try:
        key=int(input("add integer key"))
        value=int(input("add integer value"))
    except ValueError:
        raise Exception("Only integers allowed")
    key=input("add integer key")
    value=input("add integer value")
    print(add_key(key,value,{0: 10, 1: 20}))


