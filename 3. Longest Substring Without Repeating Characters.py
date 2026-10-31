class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()

        left = 0
        maximum = 0

        for right in range(len(s)):

            # Remove characters until there is no duplicate
            while s[right] in characters:
                characters.remove(s[left])
                left += 1

            # Add the current character
            characters.add(s[right])

            # Find current window length
            maximum = max(maximum, right - left + 1)

        return maximum