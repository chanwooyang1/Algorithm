def solution(my_string, indices):
    my_string_list = list(my_string)
    for ind in indices:
        my_string_list[ind] = ""
    return "".join(my_string_list)