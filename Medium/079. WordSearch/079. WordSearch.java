class Solution {
    int ROW;
    int COL;

    int[] dir = {0, 1, 0, -1, 0};
    public boolean exist(char[][] board, String word) {
        ROW = board.length;
        COL = board[0].length;

        for(int r=0; r<ROW; r++){
            for(int c=0; c<COL; c++){
                if(dfs(board, word, r, c, 0)){
                    return true;
                }
            }
        }
        return false;
    /**
    check all cells
    if a cell matches firstletter try
        mark as visited
        check all directions for next letter
    
    */
}
    public boolean dfs(char[][] board, String word, int row, int col, int index){
        if(row >= ROW || row < 0 || col >= COL || col < 0 || word.charAt(index) != board[row][col]) return false;
        if(index == word.length()-1 && board[row][col] == word.charAt(index)) return true;
        
        board[row][col] = '!';
        for(int i=0; i<dir.length-1; i++){
            if(dfs(board, word, row + dir[i], col + dir[i+1], index + 1)) return true;
        }
        board[row][col] = word.charAt(index);
        return false;
    }
} 