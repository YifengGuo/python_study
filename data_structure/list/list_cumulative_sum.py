def cumulative_sum(l):
    res = []
    i = 0
    while i < len(l):
        res.append(reduce(lambda x, y: x + y, l[:i + 1]))
        i += 1
    return res


l = [1, 2, 3]
print(cumulative_sum(l))
