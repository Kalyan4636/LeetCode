class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if not n or n == 0:
            return 0

        # dp initializtion
        # f[i][j] represents a i-length string ending with vowel[j]
        f = [[0 for _ in range(5)] for _ in range(n)]

        for j in range(5):
            f[0][j] = 1

        for i in range(1, n):
            for j in range(5):
                f[i][0] = f[i - 1][1] + f[i - 1][2] + f[i - 1][4]
                f[i][1] = f[i - 1][0] + f[i - 1][2]
                f[i][2] = f[i - 1][1] + f[i - 1][3]
                f[i][3] = f[i - 1][2]
                f[i][4] = f[i - 1][2] + f[i - 1][3]

        res = sum(f[-1])
        return res % (10 ** 9 + 7)