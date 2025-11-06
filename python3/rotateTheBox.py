class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        #print(self.shiftArray(boxGrid[0]))
        for i in range(len(boxGrid)):
            boxGrid[i] = self.shiftArray(boxGrid[i])
        #print(boxGrid)
        box2 = [[""] * len(boxGrid) for _ in range(len(boxGrid[0]))]
        r = len(box2)
        c = len(box2[0])
        for i in range(r):
            for j in range(c):
                box2[i][j] = boxGrid[c-j-1][i]
        return box2
        

    def shiftArray(self, arr):
        wall = len(arr) -1
        for i in range(len(arr)-1,-1,-1):
            if arr[i] == '*':
                wall=i-1
            elif arr[i] == '#':
                if wall != i:
                    arr[i] = '.'
                    arr[wall] = '#'
                wall -=1
        return arr
            
