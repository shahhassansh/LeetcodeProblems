class Solution:
    def asteroidCollision(self, input):
        st = []
        for a in input:
            if a > 0:
                st.append(a)
            else:
                if len(st) >0 and st[-1] <0:
                    st.append(a)
                    continue
                while len(st) >0 and st[-1] < -a and st[-1] >0:
                    st.pop()
                if len(st) == 0 or st[-1] < 0:
                    st.append(a)
                elif -a == st[-1]:
                    st.pop()
        return st

