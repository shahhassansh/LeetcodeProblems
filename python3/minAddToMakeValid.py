
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        for a in s:
            if len(st) >0:
                if a == ')' and st[-1] == '(':
                    st.pop()
                else:
                    st.append(a)
            else:
                st.append(a)
        return len(st)
        
