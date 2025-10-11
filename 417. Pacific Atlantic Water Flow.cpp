class Solution {
public:
    // Directions: right, left, down, up
    vector<vector<int>> dirs = {{0,1},{0,-1},{1,0},{-1,0}};
    
    void dfs(int i, int j, vector<vector<int>>& heights, vector<vector<bool>>& visited) {
        visited[i][j] = true;
        int m = heights.size(), n = heights[0].size();
        for (auto& d : dirs) {
            int ni = i + d[0], nj = j + d[1];
            // Check bounds and if neighbor is not visited and is higher or equal
            if (ni >= 0 && ni < m && nj >= 0 && nj < n &&
                !visited[ni][nj] && heights[ni][nj] >= heights[i][j]) {
                dfs(ni, nj, heights, visited);
            }
        }
    }
    
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int m = heights.size(), n = heights[0].size();
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));
        
        // DFS from Pacific (top row and left col)
        for (int i = 0; i < m; ++i) dfs(i, 0, heights, pacific);
        for (int j = 0; j < n; ++j) dfs(0, j, heights, pacific);
        
        // DFS from Atlantic (bottom row and right col)
        for (int i = 0; i < m; ++i) dfs(i, n-1, heights, atlantic);
        for (int j = 0; j < n; ++j) dfs(m-1, j, heights, atlantic);
        
        // Collect cells reachable from both oceans
        vector<vector<int>> res;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (pacific[i][j] && atlantic[i][j]) {
                    res.push_back({i, j});
                }
            }
        }
        return res;
    }
};