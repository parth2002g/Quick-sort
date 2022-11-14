import random


def quicksort(items):

    def sort(lst, l, r):
        if r <= l:
            return

        pivot_index = random.randint(l, r)

        lst[l], lst[pivot_index] = lst[pivot_index], lst[l]

        i = l
        for j in range(l+1, r+1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        lst[i], lst[l] = lst[l], lst[i]

        sort(lst, l, i-1)
        sort(lst, i+1, r)

    if items is None or len(items) < 2:
        return

    sort(items, 0, len(items) - 1)

numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print('unsorted: ', numbers)
quicksort(numbers)
print('sorted:   ', numbers)