public class Solution {
    /**
     * @param nums: An integer array
     * @return: nothing
     */
    public void reverseRange(List<Integer> nums, int l, int r) {
        for (int i = l; i <= (r - l) / 2 + l; i++) {
            int tmp = nums.get(i);
            nums.set(i, nums.get(r - i + l));
            nums.set(r - i + l, tmp);
        }
    }
    
    public void recoverRotatedSortedArray(List<Integer> nums) {
        if (nums == null || nums.size() == 0) {
            return;
        }
        for (int i = 0; i < nums.size() - 2; i++) {
            if (nums.get(i) > nums.get(i + 1)) {
                reverseRange(nums, 0, i);
                reverseRange(nums, i + 1, nums.size() - 1);
                reverseRange(nums, 0, nums.size() - 1);
            }
        }
    }
}