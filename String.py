# CHUỖI
# Hàm len(): trả về độ dài của chuỗi
s = "abc"
print(len(s))
s = "abcd"
print(len(s))

# Phương thức lower(): chuyển 1 chuỗi về dạng in thường
s = "CODELEARN123"
print(s.lower())

# Phương thức islower() : kiểm tra xem 1 kí tự có phải là in thường

#Phương thức upper():chuyển 1 chuỗi về dạng in hoa
s = "codelearn123"
print(s.upper())

#Phương thức isupper() : kiểm tra xem 1 kí tự có phải là in hoa

#Phương thức isalnum(): kiểm tra xem một xâu có chỉ chứa các ký tự chữ và số hay không
s = "codelearn2020"
print(s.isalnum())
s = "codelearn2020.io"
# Kết quả sẽ là False do chuỗi s chứa ký tự .
print(s.isalnum())

#Phương thức isnumeric():một xâu có chứa toàn các ký tự số hay không
s = "2020"
print(s.isnumeric())
s = "c2020"
print(s.isnumeric())

#Phương thức split(): cắt một chuỗi ra thành list các chuỗi khác 
# dựa trên một phần tử trong chuỗi đầu vào
s = "Welcome to Codelearn.io!"
print(s.split(" "))
s = "A1B1C1D1E1"
print(s.split("1"))
# Result:
"""['Welcome', 'to', 'Codelearn.io!']
['A', 'B', 'C', 'D', 'E', ''] """

#Phương thức join():nối một tập hợp thành một chuỗi sử dụng kí tự cho trước
lst = ["Welcome", "to", "Codelearn.io!"]
print(" ".join(lst))
lst = ["A", "B", "C"]
print("-".join(lst))
#Result:
'''Welcome to Codelearn.io!
A-B-C ''' 

#Use split() and join() để loại bỏ các khoảng trắng thừa trong chuỗi
message = "   Welcome  to Codelearn.io!   "
print(" ".join(message.split()))
#Result: Welcome to Codelearn.io!

#Phương thức replace(): thay thế các chuỗi con tìm thấy thành chuỗi con mới
name = "Cod3l3arn"
print(name.replace("3", "e"))
#Result: Codelearn

s = 'Python String'
# s[0] là phần tử đầu tiên trong chuỗi
print(s[0])
# s[-1] là phần tử đầu cuối cùng trong chuỗi
print(s[-1])
# s[-2] là phần tử đứng trước phần tử cuối cùng trong chuỗi
print(s[-2])
# Các toán tử trong string (Python)
# [] : Slice - Trả về kí tự trong chuỗi
x="Python"
print(x[1])

# [:] : Range slice-Trả về dãy kí tự trong chuỗi
x="Python"
print(x[1:3])

# in : Kiểm tra xem một chuỗi 
# có nằm trong chuỗi khác không
x="Python"
print("u" in x)

# not in : Kiểm tra xem một chuỗi 
# có không nằm trong chuỗi khác không
x="Python"
print("l" not in x)

# % : hỗ trợ định dạng chuỗi 
x = 12.3456789
print("The value of x is %3.2f" %x)

# + : Cộng hai chuỗi bất kì
x="Code"
y="Learn"
print(x+y)

# * : Lặp lại chuỗi bất kì cho trước
x="CodeLearn"
print(x*2)

# Basic & Useful Function (Hàm cơ bản và hữu ích)

# Hàm count trả về số lần xuất hiện của kí tự trong chuỗi
my_string = 'ok, I am fine thank you'
print(my_string.count('a'))

# String Formatting : cho phép gán biến cùng với chuỗi
# 3 kiểu dùng: % , format(), f-Strings

# %
name = 'tudaun'
my_string = "Moriaty %s" % name
#Result: my_string = "Moriaty tudaun"

# .format()
age = 21
height = 170.5
my_string = "I am {} years old; {:.3f} cm".format(age,height)
print(my_string)
#Result: I am 21 years old; 170.500 cm

# f-Strings
pi = 3.14159
name = Moriaty
my_string = f"Pi is {pi:.2f} and my name is {name}"
print(my_string)
# Result: Pi is 3.14 and my name is Moriaty
