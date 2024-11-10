def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

def find_all_occurence(numbers,numbeTOfind):
    index=binary_search(numbers,numbeTOfind)
    list=[index]
    i=index-1
    while i>=0:
        if numbers[i]==numbeTOfind:
            list.append(i)
        else:
            break
        i=i-1
    j=index+1
    while j<len(numbers):
        if numbers[i]==numbeTOfind:
            list.append(i)
        else:
            break
        j=j+1
    return list
if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 21
    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find_excercise = 15
    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    print(f"Number found at index {index} using binary search",binary_search(numbers_list,number_to_find))
    print('find',find_all_occurence(numbers,number_to_find_excercise))

# there are some error which i have to fix later , tata