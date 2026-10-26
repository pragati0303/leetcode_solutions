
class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        result = ""

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            rem = total % 26

            result += chr(ord('z') - rem)

        return result