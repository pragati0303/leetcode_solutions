class Solution:
    def reverseDegree(self, s: str) -> int:
        #Cut words,
        #get rev val
        #multiply rev val * position
        #total val
        op = 0
        for idx, alpha in enumerate(s):
            reverseIdx = 27 - ( ord(alpha) - 96)
            position = idx + 1
            mulVal = reverseIdx * position
            op += mulVal

        return op
