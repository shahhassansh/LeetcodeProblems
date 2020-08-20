class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(0,len(s)):
            if s[i] == ')' or s[i] == '}' or s[i] == ']':
                if len(st) == 0:
                    return False
                else:
                    if s[i] == ')' and st[-1] != '(':
                        return False
                    elif s[i] == ')' and st[-1] == '(':
                        st.pop()
                    elif s[i] == '}' and st[-1] != '{':
                        return False
                    elif s[i] == '}' and st[-1] == '{':
                        st.pop()
                    elif s[i] == ']' and st[-1] != '[':
                        return False
                    elif s[i] == ']' and st[-1] == '[':
                        st.pop()
            elif s[i] == '(' or s[i] == '{' or s[i] == '[':
                st.append(s[i])
        if len(st) == 0:
            return True
        else:
            return False
