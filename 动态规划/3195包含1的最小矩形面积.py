import unittest

class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        """_summary_

        Args:
            grid (list[list[int]]): _description_

        Returns:
            int: _description_
        """
        m, n = len(grid), len(grid[0])
        left, right, up, down = n, 0, m, 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    left = min(left, j)
                    right = max(right, j)
                    up = min(up, i)
                    down = i
        return (right - left + 1) * (down - up + 1)
    

class TestMiniArea(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.solution = Solution()

    def test_mini_area(
        self,
        testcases=[
            {"grid": [[0, 1, 0], [1, 1, 1], [0, 1, 0]], "ans": 9},
            {"grid": [[1, 1, 1], [1, 1, 1], [1, 1, 1]], "ans": 9},
            {"grid": [[0, 1], [0, 0]], "ans": 1},
        ],
    ):
        for testcase in testcases:
            self.assertEqual(
                self.solution.minimumArea(testcase["grid"]), testcase["ans"]
            )


if __name__ == "__main__":
    unittest.main()
