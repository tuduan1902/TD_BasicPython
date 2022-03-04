'''
Hàm Ẩn Danh - Lambda trong Python
lambda arguments: expression

'''
# A lambda function is a small (one line) anonymous function
# that is defined without a name. 

# a lambda function that adds 69 to the input argument
'''
Custom sorting using a lambda function as key parameter
'''
number_list = [5,3,-2,4,1,-1,-3,4,5]
print(sorted(number_list))
print(sorted(number_list, key = lambda x: abs(x)))

'''
Use lambda for map function
'''
# map(func, seq), transforms each element with the function
list_keyword = ["tuduan1902", "tu duan", "moriaty"]
print(list(map(lambda x: x.title(), list_keyword)))

'''
Use lambda for filter function 
'''
# filter(func, seq), return all elements for which func evaluates to True
list_number = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x%2!=0, list_number)))

'''
Use lambda for reduce function
'''
# reduce(func, seq), repeatedly applies the func to the elements and return a single value
# func takes 2 arguments.

from functools import reduce
sequence = [1,3,5,9,6,2,8]
print(reduce(lambda a,b: a if a > b else b, sequence))