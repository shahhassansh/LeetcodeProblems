class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        num1 = list(num1[::-1])
        num2 = list(num2[::-1])
        for i in range(len(num1)):
            if i <= len(num2)-1:
                temp = int(num1[i]) + int(num2[i])+ carry
                if temp > 9:
                    carry = 1
                    num1[i] = str(temp%10)
                else:
                    carry = 0
                    num1[i] = str(temp)
            else:
                temp = int(num1[i]) + carry
                if temp > 9:
                    carry = 1
                    num1[i] = str(temp%10)
                else:
                    carry = 0
                    num1[i] = str(temp)
        if carry == 1:
            num1.append(str(carry))
        return ''.join(num1[::-1])




