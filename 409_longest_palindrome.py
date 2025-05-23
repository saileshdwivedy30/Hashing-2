class Solution:
    def longestPalindrome(self, s: str) -> int:

        # return lenght of longest palindrome
        # TC: O(n)
        # SC: O(1), 52 chars max

        char_set = set()
        result = 0

        for char in s:
            if char in char_set:
                result = result + 2
                char_set.remove(char)
            else:
                char_set.add(char)

        if char_set:
            result = result + 1

        return result

        # return lenght of longest palindrome and the plaindreome too
        # TC: O(n)
        # SC: O(1) 52 chars max + O(n), palindrome string = O(n)

        # left_half = []
        # middle=""

        # for char in s:
        #     if char in char_set:
        #         left_half.append(char)
        #         result=result+2
        #         char_set.remove(char)
        #     else:
        #         char_set.add(char)

        # if char_set:
        #     middle=char_set.pop()
        #     result=result+1

        # left_string="".join(left_half)
        # palindrome_string=left_string+middle+left_string[::-1]

        # return result
