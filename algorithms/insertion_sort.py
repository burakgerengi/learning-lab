def insertion_sort(lst: list) -> list:
    """sorts the list entered as the argument."""

    for j in range(1, len(lst)):
        key = lst[j]
        i = j - 1

        while i >= 0 and key < lst[i]:
            lst[i + 1] = lst[i]
            i -= 1

        lst[i + 1] = key

    return lst


print(insertion_sort([9, 23, 5, 4, 2]))
