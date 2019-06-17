class Solution(object):
    def PalindromePermutation(self, s):
        """
        :type n: int
        :rtype: int
        """
        chars = dict()
        for char in s:
            if char.isalpha():
                if char.lower() in chars:
                    chars.pop(char.lower())
                else:
                    chars[char.lower()] = 1
        return len(chars) <= 1



def execute():
    sol = Solution()
    s = 'Tact Coa'
    print(sol.PalindromePermutation(s))

if __name__ == '__main__':
    execute()

