class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) == len(B):
            AA = A+A
            return B in AA
        return False


def execute():
    sol = Solution()
    A = 'abcde'
    B = 'cdeab'
    print(sol.RotateString(A,B))


if __name__ == '__main__':
    execute()

