def LCS(A, B):
    na, nb = len(A), len(B)
    LCS_table = [([0] * (nb + 1)) for _ in range(na + 1)]
    for i in range(1, na + 1):
        for j in range(1, nb + 1):
            if A[i - 1] == B[j - 1]:
                LCS_table[i][j] = LCS_table[i - 1][j - 1] + 1
            else:
                LCS_table[i][j] = max(LCS_table[i - 1][j], LCS_table[i][j - 1])
    ''' 문자열 출력할 때 필요.
    result = []
  
    while na > 0 and nb > 0:
        if LCS_table[na][nb - 1] == LCS_table[na][nb] or LCS_table[na - 1][nb] == LCS_table[na][nb]:
            if LCS_table[na][nb - 1] == LCS_table[na][nb]:
                nb -= 1
            else:
                na -= 1
        else:
            result.append(A[na - 1])
            na -= 1
            nb -= 1
        if LCS_table[na][nb] == 0:
            break
    result.reverse()

    return ''.join(result)
  '''
  return LCS_table[-1][-1]

str_A = input()
str_B = input()

print(LCS_table(str_A, str_B))
