# Khai báo hàm
# def <tên_hàm>:
    # Các đoạn code trong thân hàm
def show():
    for i in range(1, 11):
        # end = " " có nghĩa là sử dụng hàm print và không xuống dòng
        print(i, end=" ")
    print()
# gọi tới hàm show
show()
# Result: 1 2 3 4 5 6 7 8 9 10 

# Ví dụ về hàm trả về tổng các phần tử trong list
def sum_of_list(lst):
    answer = 0
    for v in lst:
        answer += v
    return answer

print(sum_of_list([3, 4, 2]))
print(sum_of_list([8, 4, 7]))
print(sum_of_list([1, 2, 3]))
#Result: 9 19 6

