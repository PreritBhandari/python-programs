"""
Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

def update_dict(dic1,dic2,dic3):
    d4={}
    for each in (dic1,dic2,dic3):
        d4.update(each)
    return d4
          
if __name__ == "__main__":
    print(update_dict(dic1={1:10, 2:20}, dic2={3:30, 4:40},dic3={5:50,6:60}))