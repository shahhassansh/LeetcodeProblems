class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                st.append([i,s[i]])
            if s[i] == ')':
                if len(st) == 0:
                    st.append([i,s[i]])
                elif st[-1][1] == '(':
                    st.pop()
                else:
                    st.append([i,s[i]])
        print(st)
        for j in range(len(st)-1,-1,-1):
            a = st[j]
            s.pop(a[0])
        return s
        
