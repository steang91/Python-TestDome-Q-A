def count_numbers(sorted_list, less_than):
    c=0
    ll =len(sorted_list)
    if sorted_list[0] >= less_than:
        return c
    if sorted_list[-1] < less_than:
        return ll

    while True:
        if c >= ll:
            return 0

        if c < 0 or ll > len(sorted_list):
            return 0

        pivot = int((c + ll) / 2)
        if sorted_list[pivot] < less_than:
            if sorted_list[pivot + 1] >= less_than:
                return pivot + 1
            else:
                c = pivot
        elif sorted_list[pivot] >= less_than:
            ll = pivot

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4)) # should print 2