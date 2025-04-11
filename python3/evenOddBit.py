class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        bits = []
        while n >0 :
            if n%2 == 0:
                bits.append(0)
            else:
                bits.append(1)
            n = n//2
        print(bits)
        odd = even = 0
        for i in range(len(bits)):
            if bits[i] == 1:
                if i % 2 == 0:
                    even +=1
                else:
                    odd +=1
        return [even, odd] 


        
