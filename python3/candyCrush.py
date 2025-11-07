class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        r = len(board)
        c = len(board[0]) 
        while True:
            print('abs')
            s = set()
            stable = 1
            for i in range(r):
                for j in range(c-2):
                    if board[i][j] == board[i][j+1] == board[i][j+2] != 0:
                        s.add((i,j))
                        s.add((i,j+1))
                        s.add((i,j+2))
                        stable = 0
            # print(s)
            for i in range(r-2):
                for j in range(c):
                    if board[i][j] == board[i+1][j] == board[i+2][j] != 0:
                        s.add((i,j))
                        s.add((i+1,j))
                        s.add((i+2,j))
                        stable = 0
            # print(s)
            # break
            if stable:
                return board
            for x,y in s:
                # print(str(x)+' '+ str(y))
                board[x][y] = 0
            print(board)

            for i in range(c):
                offset = 0
                for j in range(r-1,-1,-1):
                    k = j+offset
                    if (j,i) in s:
                        offset +=1
                    else:
                        board[k][i] = board[j][i]
            
                for j in range(offset):
                    board[j][i] = 0

            


        
