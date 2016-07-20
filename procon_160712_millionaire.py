

def solve(M, P, X):
    pre_list = [0, P, 1]
    for m in range(2, M + 1):
        new_list = []
        for i in range(2 ** m):
            if i % 2 == 0:
                new_list.append(pre_list[int(i / 2)])
            else:
                k = int(i // 2)
                lose_case = pre_list[k]
                win_case = pre_list[k + 1]
                new_list.append((1 - P) * lose_case + P * win_case)
        new_list.append(1)
        pre_list = new_list
        print(new_list)
    print(pre_list[find_x_point(M, X)])


def find_x_point(M, X):
    i = 0
    while True:
        if X < i * (1000000 / (2 ** M)):
            return i - 1
        else:
            i += 1


print(find_x_point(3, 1))

solve(3, 0.5, 500000)
