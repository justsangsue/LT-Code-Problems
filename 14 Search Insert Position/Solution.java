/**
 * 1. Be careful if target is greater than the last element, result should + 1.
 */
public class Solution {
    /**
     * @param A: an integer sorted array
     * @param target: an integer to be inserted
     * @return: An integer
     */
    public int searchInsert(int[] A, int target) {
        if (A.length == 0 || A == null) {
            return 0;
        }
        
        int start = 0;
        int end = A.length - 1;
        
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (A[mid] == target) {
                return mid;
            } else if (A[mid] > target) {
                end = mid;
            } else {
                start = mid;
            }
        }
        
        if (A[start] >= target) {
            return start;
        }
        if (A[end] == target) {
            return end;
        }
        if (A[end] < target) {
            return end + 1;
        }
        return end;
    }
}