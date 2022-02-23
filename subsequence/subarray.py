#! /usr/bin/python3

def findsubarray(array,subarray):

    matched=0
    j=0 # to track the element of comparsion of first array


    if len(array)<len(subarray):
        return False
    else:
        for i in range(0,len(subarray)): # find the subsequence
            for j in range(j,len(array)):
                if array[j]==subarray[i]:
                    matched=matched+1 # calculating number of matched element
                    j=j+1 # if the element gets match to start comparsion from next index of matched elemtent
                    break # if element gets match beak the loop
                j=j+1
            i=i+1
        if matched==len(subarray) :  # array of matched elements should be equal to subarray size
                return True
        else:
                return False


"""
def inputarray():
    array=[]
    subarray=[]


    array_size = int(input("Enter size of First array: ")) # getting size of array
    for i in range(0, array_size): # iterating to get the elements of array
        elements = int(input("Enter "+ str(i+1) + " element:  " ))
        array.append(elements)

    subarray_size = int(input("Enter size of Second array : ")) # getting size of subarray
    for i in range(0, subarray_size): # iterating to get the elements of array
        elements = int(input( "Enter "+ str(i+1) + " element:  " ))
        subarray.append(elements)

    return array,subarray


Firstarray,Secondarray = inputarray()
"""
first_array = [1, 2, 3]
second_array = [2,3]

result=findsubarray(first_array,second_array)#call function
print(result)
