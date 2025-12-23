class Solution:
    def itr_collision(self, input):
        st = []
        for a in input:
            if len(st) == 0:
                st.append(a)
            else:
                if a > 0:
                    st.append(a)
                elif a <0 and st[-1] <0:
                    st.append(a)
                else:
                    if st[-1] > 0:
                        if st[-1] < -1*a:
                            st[-1] = a
                        elif st[-1] == -1*a:
                            st.pop()
        return st

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        while asteroids != self.itr_collision(asteroids):
            asteroids = self.itr_collision(asteroids)
        return asteroids
