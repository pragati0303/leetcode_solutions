class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        X=0
        for op in operations:
            if op[1]=='+' :
                X+=1
            else:
                X-=1
        return X