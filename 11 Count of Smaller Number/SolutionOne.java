import java.util.ArrayList;

public class Solution {
    /**
     * @param A: An integer array
     * @param queries: The query list
     * @return: The number of element in the array that are smaller that the given integer
     */
    public List<Integer> countOfSmallerNumber(int[] A, int[] queries) {
        List<Integer> answer = new ArrayList<>();
        if (queries == null || queries.length == 0) {
            return answer;
        }
        
        Arrays.sort(A);
        for (int q : queries) {
            answer.add(binarySearch(A, q));
        }
        
        return answer;
    }
    
    public int binarySearch(int[] A, int q) {
        if (A == null || A.length == 0) {
            return 0;
        }
        
        int start = 0, end = A.length - 1;
        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;
            if (A[mid] < q) {
                start = mid;
            } else {
                end = mid;
            }
        }
        
        if (A[start] < q) {
            return start + 1;
        } else if (A[start] == q) {
            if (A[start] != A[end]) {
                return start;
            } else {
                return 0;
            }
        } else {
            return start;
        }
        
    }
}