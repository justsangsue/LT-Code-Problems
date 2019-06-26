public class SolutionOne {
	/**
     * @param A: an integer rotated sorted array
     * @param target: an integer to be searched
     * @return: an integer
     */
	public static int search(int[] A, int target) {
		
		if (A.length == 0 || A == null) {
			return -1;
		}

		int start = 0;
		int end = A.length - 1;

		while (start + 1 < end) {
			int mid = start + (end - start) / 2;

			if (A[mid] == target) {
				return mid;
			}

			if (A[mid] > A[end]) {
				/* Consider the range carefully! */
				if (target <= A[mid] && target >= A[start]) {
					end = mid;
				} else {
					start = mid;
				}
			} else {
				/* Consider the range carefully! */
				if (target >= A[mid] && target <= A[end]) {
					start = mid;
				} else {
					end = mid;
				}
			}
		}

		if (A[start] == target) {
			return start;
		} else if (A[end] == target) {
			return end;
		} else {
			return -1;
		}
	}

	public void test() {
		int[] A = {4, 5, 1, 2, 3};
		int target = 1;
		int out = search(A, target);
		System.out.println(out);
	}

	public static void main(String[] args) {
		Solution.test();
	}
}