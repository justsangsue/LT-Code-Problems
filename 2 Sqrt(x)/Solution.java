/**
 * 1. Consider 0 and 1 (initial cases)
 * 2. It could be very large, mid * mid could exceed the limit of INT (extreme cases)
 */
public class Solution {
	/**
     * @param x: An integer
     * @return: The sqrt of x
     */
    public static int sqrt(int x) {
        // write your code here
        if (x == 1 || x == 0) {
            return x;
        }

        int start = 1;
        int end = x;
        while (start + 1 < end) {
        	int mid = start + (end - start) / 2;
	        if (mid == x / mid) {
	        	return mid;
	        } else if (mid > x / mid) {
	        	end = mid;
	        } else {
	        	start = mid;
	        }
	    }

	    return start;
    }

    public static void test() {
    	int x = 4187;
    	int out = sqrt(x);
    	System.out.println(out);
    }

    public static void main(String[] args) {
    	test();
    }
}