
def lcs(a: str, b: str):
    result = [['' for a in range(len(b)+1)] for _ in range(len(a)+1)]

    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                result[i][j] = result[i-1][j-1] + a[i-1]
            else:
                sub_a = result[i-1][j]
                sub_b = result[i][j-1]

                result[i][j] = sub_a if len(sub_a) >= len(sub_b) else sub_b

    return result[-1][-1]


print(lcs('abcdaf', 'acbcf'))  # abcf
