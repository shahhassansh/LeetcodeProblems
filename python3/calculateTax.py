class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        x = brackets
        for i in range(len(x)):
            if income <= 0:
                return tax
            if i == 0:
                curr = min(x[i][0] , income) 
                tax += (x[i][1]*1.0/100)*curr
                income -= x[i][0]
            else:
                curr = min(x[i][0] - x[i-1][0] , income) 
                tax += (x[i][1]*1.0/100)*curr
                income -= curr
        return tax
        
