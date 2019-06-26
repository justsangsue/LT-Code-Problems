/**
 * 1. If target in last row, then target could be greater than matrix[end][0]
 * 2. 
 */
public class Solution {
	 /**
     * @param matrix: matrix, a list of lists of integers
     * @param target: An integer
     * @return: a boolean, indicate whether matrix contains target
     */
    public boolean searchMatrix(int[][] matrix, int target) {
    	if (matrix == null || matrix.length == 0) {
            return false;
        }
        
        if (matrix[0].length == 0 || matrix[0] == null) {
            return false;
        }
        
        int num_rows = matrix.length;
        int num_cols = matrix[0].length;
        
        /* First binary search: find row */
        int start = 0;
        int end = num_rows - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (matrix[mid][0] == target) {
                return true;
            } else if (matrix[mid][0] > target) {
                end = mid;
            } else {
                start = mid;
            }
        }
        
        if (matrix[start][0] == target || matrix[end][0] == target) {
            return true;
        }
        
        int[] target_list = {};
        if (target > matrix[end][0]) {
            target_list = matrix[end];
        } else {
            target_list = matrix[start];
        }
        /* Second binary search */
        start = 0;
        end = num_cols - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (target_list[mid] == target) {
                return true;
            } else if (target_list[mid] > target) {
                end = mid;
            } else {
                start = mid;
            }
        }
        
        if (target_list[start] == target || target_list[end] == target) {
            return true;
        }
        
        return false;
    }
}