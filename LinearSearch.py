#! /usr/bin/python3

array=[]

try:
    Input_element= int(input("Enter the element you want to search:  "))

    array_size = int(input("Enter size of First array: ")) # getting size of array
    for i in range(0, array_size): # iterating to get the elements of array
        elements = int(input("Enter "+ str(i+1) + " element:  " ))
        array.append(elements)

except (ValueError, NameError) as e:
     print( " Please Enter interget values only ")





def linearSearch(array,element):
    for i in array:
        if element==i:
            return array.index(i)
            break




result=linearSearch(array,Input_element)
if result== None:
    print("Element is not present in array")
else:
    print("Element match at " + str(result) + " index.")
