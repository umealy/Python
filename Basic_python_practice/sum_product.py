#Given two integer numbers, write a Python code to return their product only if the product 'is equal to or lower than 1000. Otherwise, return their sum

first_num=int(input("Enter first number = "))
sec_num=int(input("Enter second number = "))
product=first_num*sec_num
if product<=1000:
    print( "The result is  " + str( product) )
else:
   print( "The result is  " + str(first_num+sec_num ))  