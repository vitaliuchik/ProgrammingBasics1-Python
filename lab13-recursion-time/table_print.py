tbl = dict()

def table(m, n):
    """
    (int, int) -> int
    Builds table as in task 3
    """
    ind = str(m) + '_' + str(n)
    if m > 0 and n > 0:
        tbl['1_1'] = 1
    if m == 1:
        tbl[ind] = 1
        return 1
    elif n == 1:
        tbl[ind] = 1
        return 1
    else:
        tbl[ind] = table(m-1, n) + table(m, n-1)
        return tbl[ind]

table(7, 5)
tbl_keys = list(tbl.keys())
tbl_keys.sort()
m = int(tbl_keys[-1][:1])
n = int(tbl_keys[-1][2:])
for i in range(m):
    for j in range(n):
        el = tbl[tbl_keys[n*i + j]]
        print(el, end=(5-len(str(el)))*' ')
    print()

