class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[len(digits)-1] <9:
            digits[len(digits)-1]+=1
            return digits
        else:
            for i in range(len(digits)-1,-1,-1):
                if i == 0 and digits[i]==9:

                    return [1,0]+digits[1:]
                elif digits[i]!=9:

                    digits[i]+=1
                    return digits
                else:
                    digits[i] = 0
