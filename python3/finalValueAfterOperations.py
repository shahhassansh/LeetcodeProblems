class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for a in operations:
            if a == '++X' or a =='X++':
                x+=1
            if a == '--X' or a == 'X--':
                x-=1
        return x
        
