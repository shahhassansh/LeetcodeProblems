class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for a in s:
            if a != ']':
                st.append(a)
            else:
                strg = ""
                while st[-1] != '[':
                    strg = st.pop() + strg
                st.pop()

                k = ""
                while st and st[-1].isdigit():
                    k = st.pop() + k
                st.append(int(k)*strg)
        return ''.join(st)

        
