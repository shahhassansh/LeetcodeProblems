class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:
        numbers.sort()
        for i in range(1, len(numbers)):
            l = len(numbers[i-1])
            if numbers[i-1] == numbers[i][:l]:
                return False
        return True
        
