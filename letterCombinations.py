class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        ans = ""
        lst = []  
        pos = 0
        if len(digits) == 0:
            return []
        def bfs(pos,ans):
            if pos == len(digits):
                lst.append(ans)
            else:
                letters = dic[digits[pos]]
                
                for i in letters:
                    bfs(pos+1,ans+i)
        bfs(pos,ans)
        return lst

        
        
        
