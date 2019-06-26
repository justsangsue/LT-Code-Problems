public class Solution {
    /**
     * @param A: an integer sorted array
     * @param target: an integer to be inserted
     * @return: a list of length 2, [index1, index2]
     */
    public int[] searchRange(int[] A, int target) {
        int index1 = -1, index2 = -1;
        if (A == null || A.length == 0) {
            return new int[]{index1, index2};
        }
        
        /**
         * Find last position <= target and first position >= target
         */ 
        int start = 0, end = A.length - 1;
        /**
         * index1: last position <= target
         */
        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;
            if (A[mid] <= target) {
                start = mid;
            } else {
                end = mid;
            } 
        }
        
        if (A[start] == target) {
            index1 = start;
        }
        
        if (A[end] == target) {
            index1 = end;
        }

        start = 0; end = A.length - 1;
        /**
         * index2: first position >= target
         */
        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;
            if (A[mid] >= target) {
                end = mid;
            } else {
                start = mid;
            } 
        }
        
        if (A[end] == target) {
            index2 = end;
        }
        
        if (A[start] == target) {
            index2 = start;
        }
        
        if (index1 != -1 && index2 != -1 && A[index1] == A[index2]) {
            int tmp;
            tmp = index1;
            index1 = index2;
            index2 = tmp;
        }
        
        return new int[]{index1, index2};
    }
}