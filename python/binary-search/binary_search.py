def find(search_list, value):
    if not search_list:
        raise ValueError("value not in array")
    mid = len(search_list) // 2
    if search_list[mid] == value:
        return mid
    elif value < search_list[mid]:
        return find(search_list[:mid], value)
    else:
        return find(search_list[mid + 1 :], value) + mid + 1
