class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        arr2 =[]
        for i in range(len(arr)):
            if len(arr[i]) != 0:
                if arr[i] == "..":
                    arr2 = arr2[:-1]
                elif arr[i] == '.':
                    continue
                else:
                    arr2.append(arr[i])
        return '/'+'/'.join(arr2)
                

        
