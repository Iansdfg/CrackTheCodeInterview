class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        def spit(s):
            ans = []
            for i in range(len(s)):
                ans.append(s[i])
            return ans

        alp = 0
        res = []
        while alp < len(chars):
            nowAlp = chars[alp]
            res.append(nowAlp)
            cnt = alp + 1
            while cnt < len(chars) and chars[cnt] == nowAlp:
                cnt += 1
            if cnt-alp > 1:
                res += spit(str(cnt-alp))
            alp = cnt
        chars[:] = res
        return ''.join(chars)


def execute():
    sol = Solution()
    chars = ["a","a","a","a","a","b"]
    print(sol.compress(chars))

if __name__ == '__main__':
    execute()

