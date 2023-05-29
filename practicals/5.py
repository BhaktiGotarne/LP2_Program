# Explanation of the code
# is_attack(int i,int j) →  This is a function to check if the cell (i,j) is under attack by any other queen or not. We are just checking if there is any other queen in the row ‘i’ or column ‘j’. Then we are checking if there is any queen on the diagonal cells of the cell (i,j) or not. Any cell (k,l) will be diagonal to the cell (i,j) if k+l is equal to i+j or k-l is equal to i-j.

# N_queen → This is the f+unction where we are really implementing the backtracking algorithm.

# if(n==0) → If there is no queen left, it means all queens are placed and we have got a solution.

# if((!is_attack(i,j)) && (board[i][j]!=1)) → We are just checking if the cell is available to place a queen or not. is_attack function will check if the cell is under attack by any other queen and board[i][j]!=1 is making sure that the cell is vacant. If these conditions are met then we can put a queen in the cell – board[i][j] = 1.

# if(N_queen(n-1)==1) → Now, we are calling the function again to place the remaining queens and this is where we are doing backtracking. If this function (for placing the remaining queen) is not true, then we are just changing our current move – board[i][j] = 0 and the loop will place the queen on some another position this time.

  # I will also discuss more problems on this topic in the upcoming posts

print ("Enter the number of queens")
N = int(input())


board = [[0]*N for _ in range(N)]

def is_attack(i, j):
    
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
   
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False

def N_queen(n):
    
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                
                if N_queen(n-1)==True:
                    return True
                board[i][j] = 0

    return False

N_queen(N)
for i in board:
    print (i)



