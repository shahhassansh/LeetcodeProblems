class Solution:
    def addBinary(self, a: str, b: str) -> str:
        o = ""
        carr = "0"
        if len(b) > len(a):
            z = a
            a = b
            b = z
        x = max(len(a),len(b))
        k = len(a)-1
        l = len(b)-1
        for i in range(x-1,-1,-1):
            if k >=0 and l>= 0:
                if a[k] == '0' and b[l] == "0" and carr == "0":
                    o = "0"+o
                elif a[k] == '0' and b[l] == "0" and carr == "1":
                    o = "1"+o
                    carr = "0"
                elif a[k] == '0' and b[l] == "1" and carr == "0":
                    o = "1"+o
                elif a[k] == '1' and b[l] == "0" and carr == "0":
                    o = "1"+o
                elif a[k] == '1' and b[l] == "1" and carr == "0":
                    o = "0"+o
                    carr = "1"
                elif a[k] == '1' and b[l] == "0" and carr == "1":
                    o = "0"+o
                elif a[k] == '0' and b[l] == "1" and carr == "1":
                    o = "0"+o
                elif a[k] == '1' and b[l] == "1" and carr == "1":
                    o = "1"+o
                    carr = "1"
                k-=1
                l-=1
            elif k >=0 and l <0:
                if a[k] == "0" and carr == "0":
                    o = "0"+o
                elif a[k] == "1" and carr == "0":
                    o = "1"+o
                elif a[k] == "0" and carr == "1":
                    o = "1"+o
                    carr = "0"
                elif a[k] == "1" and carr == "1":
                    o = "0"+o
                k-=1
        if carr == "1":
            o = "1"+o
        return o
