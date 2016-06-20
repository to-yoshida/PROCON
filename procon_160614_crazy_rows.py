
def make_last_el_index_list(n, matrix):
    last_el_index_list = []
    for i in range(n):
        last_el_index = 0
        for k in range(1, n + 1):
            if matrix[i][-k] == 1:
                last_el_index = n - k
                break
        last_el_index_list.append(last_el_index)
    return last_el_index_list


def change_rows(p, q, index_list): # pをqの位置に。但し、q < p。
    if p <= q:
        raise Exception
    return index_list[:q] + [index_list[p]] + index_list[q:p] + index_list[p + 1:]


def solve(n, matrix):
    ans = 0
    last_el_index_list = make_last_el_index_list(n, matrix)
    for i in range(n):
        if last_el_index_list[i] > i:
            k = 1
            while True:
                if last_el_index_list[i + k] <= i:
                    ans += k
                    last_el_index_list = change_rows(i + k, i, last_el_index_list)
                    break
                k += 1
    print(last_el_index_list)
    return ans

matrix = [[1, 0, 1], [1, 1, 0], [1, 0, 0]]
print(solve(3, matrix))

