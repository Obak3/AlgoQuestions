'''
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
'''

class Solution:
    def removeVowels(self, s: str) -> str:
        # Declare an empty string
        ans = ""
        # Iterate through provided string
        for i in s:
            # If the letter is not in the list
            if i not in ["a","e","i","o","u"]:
                # Add the string
                rtn_str += i
        # Return ans
        return ans
