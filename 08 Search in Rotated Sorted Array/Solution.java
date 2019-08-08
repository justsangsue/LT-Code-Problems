public class Solution {
    /**
     * @param A: an integer rotated sorted array
     * @param target: an integer to be searched
     * @return: an integer
     */
    public int search(int[] A, int target) {
        if (A.length == 0 || A == null) {
			return -1;
		}

		int start = 0, end = A.length - 1;
		while (start + 1 < end) {
		    int mid = (end - start) / 2 + start;
		    if (A[mid] > A[end]) {
                if (target == A[start]) {
                    return start;
                } else if (target == A[mid]) {
                    return mid;
                } else if (target > A[start] && target < A[mid]) {
                    end = mid;
                } else {
                    start = mid;
                }
            } else {
                if (target == A[end]) {
                    return end;
                } else if (target == A[mid]) {
                    return mid;
                } else if (target > A[mid] && target < A[end]) {
                    start = mid;
                } else {
                    end = mid;
                }
            } 
		}
	
    	if (A[start] == target) {
    	    return start;
    	} 
    	
    	if (A[end] == target) {
    	    return end;
    	}
	return -1;
    }
}