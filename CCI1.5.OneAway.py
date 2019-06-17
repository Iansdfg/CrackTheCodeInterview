
class Solution(object):
    def OneAway (self, s1, s2):
        if s1 == s2: return True
        m, n = len(s1), len(s2)
        if abs(m - n) > 1: return False
        count, i, j = 0, 0, 0
        while i < m and j < n:
            if s1[i] != s2[j]:
                if count == 1:
                    return False
                if m > n:
                    i += 1
                elif m < n:
                    j += 1
                else:
                    i += 1
                    j += 1
                count += 1
            else:
                i += 1
                j += 1
        if i < m or j < n:
            count += 1
        return count == 1

def execute():
    sol = Solution()
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]
    for [test_s1, test_s2, expected] in data:
        actual = sol.OneAway(test_s1, test_s2)
        if actual != expected:
            print(test_s1, test_s2, 'Actual: ', actual, 'Expected: ', expected )


if __name__ == '__main__':
    execute()

