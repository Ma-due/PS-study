class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def dfs(open, close, s):
            if len(s) == n * 2:
                answer.append(s)
                return

            if open < n:
                dfs(open + 1, close, s + '(')

            if close < open:
                dfs(open, close + 1, s + ')')

        answer = []
        dfs(0, 0, '')

        return answer
