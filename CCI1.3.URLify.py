
class Solution(object):
    def URLify (self, s):
        res = ''
        for i, char in enumerate(s):
            if char ==' ':
                if s[i-1]!=' ':
                    res+='20%'
            else:
                res+=char
        return res


def execute():
    sol = Solution()
    s = 'Mr John   Smith'
    print(sol.URLify(s))


if __name__ == '__main__':
    execute()

