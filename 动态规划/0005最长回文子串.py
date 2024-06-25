import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """get the longest palindrome substring of s

        Args:
            s (str): input strings

        Returns:
            str: the longest palindrome substring of s
        """
        n = len(s)
        if n < 2:
            return s
        ans = 1  # 记录最长回文串的长度
        start = 0  # 记录最长回文串的起始位置
        dp = [[False] * n for _ in range(n)]  # dp[i][j]表示 s[i:j+1] 是否为回文串
        for i in range(n):
            dp[i][i] = True
        for i in range(n):
            # 以i为中心向两边扩展，最多扩展的长度为i
            for j in range(1, i + 1):
                left = i - j
                right = i + j
                if right >= n:
                    break
                if s[left] != s[right]:
                    continue
                dp[left][right] = dp[left + 1][right - 1]
                if right - left + 1 > ans and dp[left][right]:
                    ans = right - left + 1
                    start = left
            # 以i和i+1为中心向两边扩展，最长的扩展长度为i+1
            for j in range(1, i + 2):
                left = i - j + 1
                right = i + j
                if right >= n or left < 0:
                    break
                if s[left] != s[right]:
                    continue
                if right - left == 1:
                    dp[left][right] = True
                else:
                    dp[left][right] = dp[left + 1][right - 1]
                if right - left + 1 > ans and dp[left][right]:
                    ans = right - left + 1
                    start = left
        return s[start: start + ans]


class TestSolution(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_longestPalindrome(
        self,
        question_ans_dict={
            "babda": "bab",
            "babad": "bab",
            "cbbd": "bb",
            "a": "a",
            "ac": "a",
        },
    ):
        for k, v in question_ans_dict.items():
            self.assertEqual(self.solution.longestPalindrome(k), v)


if __name__ == "__main__":
    unittest.main()
