"""
Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
"""
def insert_sting_middle(initial_string,text):
    if len(initial_string) % 2 != 0:
        raise Exception ("Cant Decide middle point in string having odd length")
    else:
        mid_locaiton=len(initial_string)//2   
        list_string=list(initial_string)
        list_string.insert(mid_locaiton,text)
        return ''.join(list_string)

if __name__ == "__main__":
    print(insert_sting_middle ('[[]]<<>>','Python'))
    print(insert_sting_middle ('{{}}','PHP'))
    