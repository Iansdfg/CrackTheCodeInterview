class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        dic = dict()
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        for char in t:
            if char in dic:
                dic[char] -= 1
            else:
                return False
        for value in dic.values():
            if value != 0:
                return False
        return True
        
        
