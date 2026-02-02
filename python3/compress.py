class Solution:
    def compress(self, chars: List[str]) -> int:
        out = ""

        for i in range(len(chars)):
            if i == 0:
                out = out + chars[i]
                x = 1
            elif chars[i-1] == chars[i]:
                x+=1
            else:
                if x > 1:
                    out = out+ str(x)
                out = out + chars[i]
                x = 1
        if x > 1:
            out = out+ str(x)
        l = len(out)

        for i in range(l):
            chars[i] = out[i]

        return l
        
