class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        x = 0
        first_1 = 0
        if max(flowerbed) == 0:
            if n <= (len(flowerbed)+1)/2:
                return True
            else:
                return False
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                if first_1 == 0:
                    if cnt > 1:
                        x+= cnt//2
                else:
                    if cnt >2:
                        x += (cnt-1)//2
                first_1 = 1
                cnt = 0
            else:
                cnt+=1
        if cnt > 1:
            x+= cnt//2
        if x>=n :
            return True
        else:
            return False


        
