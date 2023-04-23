# exercise https://leetcode.com/problems/valid-palindrome
# improve execute time. For now, execution time is 82 ms


import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r' |,|\s|\.|:|[\W_]', '', s).lower()
        i = 0
        j = len(s) - 1

        # if len(s) == 1:
        #     return False

        is_palindrome = True
        while is_palindrome is True and i <= j:
            print(i, j, is_palindrome)
            if s[i] != s[j]:
                is_palindrome = False
                break

            i += 1
            j -= 1

        return is_palindrome
