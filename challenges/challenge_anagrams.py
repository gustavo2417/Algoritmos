def quick_sort(list):
    left = []
    mid = []
    right = []

    if len(list) > 1:
        pivot = len(list) // 2
        value = list[pivot]

        for i in list:
            if i > value:
                right.append(i)
            elif i < value:
                left.append(i)
            else:
                mid.append(i)

        return quick_sort(left) + mid + quick_sort(right)

    return list


def is_anagram(first_string, second_string):
    first_list = list(first_string.lower())
    second_list = list(second_string.lower())

    sort_f = "".join(quick_sort(first_list))
    sort_s = "".join(quick_sort(second_list))

    if len(sort_f) > 0 and sort_f == sort_s:
        return (sort_f, sort_s, True)

    return (sort_f, sort_s, False)
