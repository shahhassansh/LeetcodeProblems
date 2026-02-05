class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for a in s:
            if a == '*':
                st.pop()
            else:
                st.append(a)
        return ''.join(st)

        
