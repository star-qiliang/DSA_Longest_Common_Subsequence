class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)+1
        n = len(text2)+1

        danamic_programming_matrix = [[0]*n for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1]==text2[j-1]:
                    danamic_programming_matrix[i][j] = danamic_programming_matrix[i-1][j-1]+1
                else:
                    res1 = danamic_programming_matrix[i][j-1]
                    res2 = danamic_programming_matrix[i-1][j]
                    danamic_programming_matrix[i][j] = max(res1, res2)

        res = danamic_programming_matrix[m-1][n-1]
        return res