public class Solution {
    /**
     * @param nums: An integer array sorted in ascending order
     * @param target: An integer
     * @return: An integer
     */
    public int lastPosition(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        
        int start = 0, end = nums.length - 1;
        
        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;
            
            if (target == nums[mid]) {
                start = mid;
            } else if (target < nums[mid]) {
                end = mid;
            } else {
                start = mid;
            }
        }
        
        if (target == nums[start]) {
            if (nums[start] == nums[end]) {
                return end;
            } else {
                return start;
            }
        }
        
        if (target == nums[end]) {
            return end;
        }
        
        return -1;
    }
}