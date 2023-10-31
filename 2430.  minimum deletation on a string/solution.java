class Solution {
    public int deleteString(String s) {
        final int n = s.length();
        // lcs[i][j] := # of the same characters of s[i:] and s[j:]
        int[][] lcs = new int[n + 1][n + 1];
        // dp[i] := max # of operations needed to delete s[i:]
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        for (int i = n - 1; i >= 0; --i)
            for (int j = i + 1; j < n; ++j) {
                if (s.charAt(i) == s.charAt(j))
                    lcs[i][j] = lcs[i + 1][j + 1] + 1;
                if (lcs[i][j] >= j - i)
                    dp[i] = Math.max(dp[i], dp[j] + 1);
            }

        return dp[0];
    }
}
