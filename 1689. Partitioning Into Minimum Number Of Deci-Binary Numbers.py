class Solution:
    def minPartitions(self, n: str) -> int:
        largest=0
        for digit in n:
            if int(digit)>largest:
                largest=int(digit)
        return largest