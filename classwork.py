def calc_factorial_for(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def calc_factorial_while(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res


def find_max_2(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2


def find_max_3(num1, num2, num_3):
    return find_max_2(find_max_2(num1, num2), num_3)


def find_max(*args):
    max_num = args[0]
    for i in range(1, len(args)):
        val = args[i]
        if val > max_num:
            max_num = val
    return max_num


def change_array_1(my_list: list):
    tmp = my_list[0]
    my_list[0] = my_list[-1]
    my_list[-1] = tmp
    return my_list


def change_array(my_list: list):
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
    return my_list


list_len = int(input("enter list's length: "))
array = []
for _ in range(list_len):
    array.append(int(input("enter a number: ")))
new_array = change_array(array)

print(new_array)
