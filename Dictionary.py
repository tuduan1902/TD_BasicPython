'''
Same Object in JS
Dictionary: một tập hợp các cặp key-value không có thứ tự, có thể thay đổi
và lập chỉ mục
Dictionary được khởi tạo với các dấu ngoặc nhọn {} và chúng có các key and value
Mỗi cặp key-value được xem như là một item. Key mà đã truyền cho item đó phải là duy nhất,
trong khi đó value có thể là bất kì kiểu giá trị nào

Key phải là một kiểu dữ liệu không thay đổi (immutable) như chuỗi, số hoặc tuple

'''
#Create a new Dictionary: 
my_dict = {"name" : "moriaty", "content" : "githubtuduan1902", "city" : "HCM"}
print(my_dict)

# Khởi tạo bằng hàm dict()
my_dict2 = dict(name="TuDaun",content="githubtuduan",city="HCM")
print(my_dict2)

#Access items 
content_in_dict = my_dict["content"] #Return value của key content
print(content_in_dict)

#Check for keys 
# use except try
try:
    print(my_dict["age"])
except KeyError:
    print("No Key Found")

# Add and change items(key-value)
# add a new key
my_dict["email"] = "uuxinhxinh2701@gmail.com"

# or overwrite the value on existing key
my_dict["email"] = "uuxinhxinh2701@github.dev"
print(my_dict)

# Delete items 
# delete a key-value pair 
 # del my_dict["city"]
# Hàm pop()
print("Popped value: " + my_dict.pop("city"))
print(my_dict)
# Hàm popitem() : remove item cuối cùng trong dictionary
my_dict["age"] = 25
print(my_dict)
my_dict.popitem()
print(my_dict)

# Looping through Dictionary

# loop over keys
for key in my_dict.keys():
    print(key, my_dict[key])
# loop over values
for value in my_dict.values():
    print(value)
# loop over keys and values
for key,value in my_dict.items():
    print(key, value)