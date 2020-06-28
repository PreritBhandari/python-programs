"""
Write a Python program to iterate over dictionaries using for loops.
"""
def update_dict(input_dict):
    list_kv=[]
    for k,v in input_dict.items():
        list_kv.append((k,v))
    return list_kv
    
        
          
if __name__ == "__main__":
    print(update_dict({1:10, 2:20, 3:30, 4:40, 5:50}))