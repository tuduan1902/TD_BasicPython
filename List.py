'''
List trong Python - một dạng dữ liệu cho phép lưu trữ nhiều kiểu dữ liệu khác nhau trong nó
và chúng ta có thể truy xuất đến các phần tử bên trong nó thông qua vị trí của phần tử đó 
trong list

Ngôn ngữ khác: C/C++, Java, JS, list trong Python = Mảng(array)

'''

'''
1. Creating a list
'''
list_1 = ["banana","apple", "orange", "cherry"]
list_2 = [5, "CodeXplore", False, None]
list_3 = list()

'''
2. Access elements: Truy cập đến các giá trị trong list
'''
my_list = [1,2,'3',True]
len(my_list) # return độ dài phần tử trong list (Result: 4)
print(my_list[2]) # result: 3
print(my_list.index('3')) # result: 2 (vị trí)

my_list1 = [1, 2, 3, 3, 3, '3', '3']
# Hàm count cho biết số lần xuất hiện của phần tử trong list
print(my_list1.count(3)) # Result: 3 

# Truy cập từng phần tử trong list:
for item in my_list:
    print(item) 

# Python built-in enumerate function
presidents = ["Washington", "Adams", "Obama", "Trump"]
for index, president in enumerate(presidents):  # duyệt qua vị trí và giá trị của phần tử trong list
    print(f"President #{index}: {president}")

# Slicing : cắt
#: is called slicing and 
# has the format [start : end : step]

my_list = [1, 2, '3', True]
print(my_list[1:]) #Result: [2, '3', True]

print(my_list[-1]) # -1 cho phép truy cập tới giá trị cuối cùng trong chuỗi

'''
3.List Operations & Useful Methods
    3.1. Add to list

'''
lst = [1, 2, '3', True]  
lst.append() # Để thêm 1 phần tử vào cuối list 
lst.extend([100, "tudaun"]) #Add nhiều giá trị vào list
lst.insert(3,4) # Add 4 vào vị trí thứ 3 của lst

'''
    3.2. Remove from List
'''
lst = [1, 2, '3', True] 
lst.pop() # Xóa phần tử cuối cùng ra khỏi list
lst.pop(1) # Xóa phần tử ở vị trí số 1
lst.remove(2) # Xóa giá trị đầu tiên trong list
del lst[3] # Xóa phần tử ở vị trí số 3
#Hàm clear: xóa hết các phần tử bên trong list
#EX: 
lst = [1, 2, 3]
lst.clear()
print(lst)

'''
    3.3. Sorting
'''
my_list2 = [1, 2, 8, 4 ,5 ,7]
my_list2.sort() # Sắp xếp theo thứ tự tăng dần
my_list2.sort(reverse=True) # Sắp xếp theo thứ tự giảm dần

my_list2.reverse() # Đảo ngược list
sorted(my_list2) # Tạo ra 1 list mới theo thứ tự tăng dần
reverse(my_list2) # Tạo ra 1 object đảo ngược list
# Muốn in reverse()
print(list(reverse(my_list2))) # Chuyển về dạng list mới in được

'''
    3.4. Useful operations
'''
my_list = [1, 2, 8, 4, 5, 7]
range()
# hàm trả về một tập hợp
# EX: rang(1,5) sẽ trả về 1 tập hợp từ 1 tới 4
# thường đi chung với vòng for
# LIST

# Hàm len : Hàm trả về số phần tử có trong list 
# Câu lệnh: len(lst)
# EX: duyệt qua các phần tử trong list
lst = [2, 3, 1]
for i in range(len(lst)):
    print(lst[i])

# Hàm min, max : trả  về phần tử lớn nhất và nhỏ nhất trong list
# Câu lệnh: max(lst) or  min(lst)
# EX: 
    lst = [2, 3, 1]
    print(max(lst))
    print(min(lst))







