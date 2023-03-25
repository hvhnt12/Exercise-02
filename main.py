# TASK 1
def count_integer(numbers, integer):
    count = 0
    for num in numbers:
        if num == integer:
            count += 1
    if count == 0:
        return 42
    else:
        return count


# TASK 2
def list_func(numbers, integer):
    if integer in numbers:
        new_list = numbers.copy()
        for i in range(len(new_list)):
            if new_list[i] == integer:
                new_list[i] = 6
        new_list.reverse()
        print(new_list)
        return numbers
    else:
        return []


# TASK 3
def compare_lists(list1, list2):
    common_elements = []
    for elem in list1:
        if elem in list2 and elem not in common_elements:
            common_elements.append(elem)
    return common_elements


# TASK 4
def remove_duplicates(lst):
    new_lst = []
    for elem in lst:
        if elem not in new_lst:
            new_lst.append(elem)
    return new_lst


# TASK 5
def dict_func(dictionary):
    type_val = dictionary.get('Type', "unknown type")
    brand_val = dictionary.get('Brand', "unknown brand")
    price_val = dictionary.get('Price', "unknown price")
    print(f"You have a {type_val} from {brand_val} that costs {price_val}.")
    dictionary["OS"] = "Linux"
    print(dictionary)
    return dictionary
