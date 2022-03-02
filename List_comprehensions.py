'''
4. List Comprehension

List Comprehension giúp bạn viết code ngắn gọn (đặc biệt khi đang ở trong một vòng lặp)
dễ đọc, repair code hơn.
'''
# new_list [<action> for <item> in <iteration> if <some condition>]

word = "Hello World"
print([char for char in word])

even_numbers = [i for i in range(0,10) if i % 2 == 0]
print(even_numbers) #Ressult: [0, 2, 4, 6, 8]

transactions = [100, 200, 300, 150, 80]
TAX_RATE = 0.08
SERVICE_CHARE = 0.07

def get_price_tax_servive(bill):
    return bill*(1 + TAX_RATE + SERVICE_CHARE)
final_prices = [get_price_tax_servive(bill) for bill in transactions]
print(final_prices) 

#Advanced Functions

#list() --> convert strings => list
my_strings = "Moriaty"
list_of_chars = list(my_strings)
print(list_of_chars)

# zip() : looping through two list simultaneously
wizards = ['Harry Potter', 'Ron', 'Hermione']

pets = ['Hedwig', 'Scabber', 'Crookshank']

for index, (wiz, pet) in enumerate(zip(wizards, pets)):
    print(f'{index + 1}. {wiz} has {pet}')

# sorted()
sorted_by_second = sorted(
    ['hi', 'hello', 'you', 'Moriaty'], key = lambda el: el[1])
print(sorted_by_second)

sorted_by_key = sorted([{'name': 'tudaun', 'age' : '21'}, 
{'name': 'Moriaty', 'age' : '17'}], key=lambda el: el['name'])
print(sorted_by_key)

'''
5. 2D Array/List = Matrix: Mảng 2 chiều
'''
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[1][2]) #Result: 6

# Lọc các phần tử trong mảng 2 chiều
list_converted = [matrix[row][col]  
                    for row in range(len(matrix)) for col in range(len(matrix))]
print(list_converted)

#Combine columns with zip and *:
[x for x in zip(*matrix)] #Result: [(1,4,7), (2,5,8), (3,6,9)]


