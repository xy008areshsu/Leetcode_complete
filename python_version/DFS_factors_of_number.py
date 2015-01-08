"""
e.g. 12 : return [ [1, 12], [2, 2, 3], [2, 6], [3, 4]  ]
"""

def factors_of_num(num):
    res = []
    list_aux = []
    helper(num, res, list_aux)

    return res

def helper(num, res, list_aux):
    if num == 1:
        if len(list_aux) < 2:
            list_aux.append(num)
            res.append(list_aux[:])
            list_aux.pop()
        else:
            res.append(list_aux[:])

        return

    for i in range(2, num + 1):
        if num % i == 0:
            if (len(list_aux) > 0 and i >= list_aux[-1]) or len(list_aux) == 0:
                list_aux.append(i)
                helper(num / i, res, list_aux)
                list_aux.pop()


print(factors_of_num(8864))