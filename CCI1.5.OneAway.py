
class Solution(object):
    def OneAway (self, s1, s2):
        if s1 == s2: return True

        m = len(s1)
        n = len(s2)

        if abs(m - n) > 1:
            return False

        count = 0  # Count of isEditDistanceOne

        i = 0
        j = 0
        while i < m and j < n:
            # If current characters dont match
            if s1[i] != s2[j]:
                if count == 1:
                    return False

                    # If length of one string is
                # more, then only possible edit
                # is to remove a character
                if m > n:
                    i += 1
                elif m < n:
                    j += 1
                else:  # If lengths of both strings is same
                    i += 1
                    j += 1

                # Increment count of edits
                count += 1

            else:  # if current characters match
                i += 1
                j += 1

        # if last character is extra in any string
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

