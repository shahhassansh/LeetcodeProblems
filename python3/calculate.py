class Solution:
    def calculate(self, s: str) -> int:
        prev = '+'
        nm = 0
        st = []
        s = list(s)
        for i in range(len(s)):
            if s[i].isdigit():
                nm = nm*10+int(s[i])
            if s[i] in '+/-*' or i == (len(s)-1):
                if prev == '+':
                    st.append(nm)
                elif prev == '-':
                    st.append(-nm)
                elif prev == '*':
                    st[-1] = st[-1]*nm
                elif prev == '/':
                    st[-1] = int(st[-1]/nm)
                nm = 0
                prev = s[i]
        return sum(st)








        
