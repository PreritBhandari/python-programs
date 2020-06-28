"""
 Write a Python program to find intersection of two given arrays using Lambda.
"""
def intersect_array(arr1,arr2):
    intersect=[]
    check = lambda x: x in arr2
    for each in arr1:
        if check(each):
            intersect.append(each)
    return list(map(int,intersect))
    # return set(arr1).intersection(set(arr2))


if __name__ == "__main__":
    arrayOne=input('Enter any Elemnts in array1 using space:').split()
    arrayTwo=input('Enter any Elemnts in array2 using space:').split()
    print(intersect_array(arrayOne,arrayTwo))