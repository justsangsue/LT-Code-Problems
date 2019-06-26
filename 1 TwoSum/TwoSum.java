import java.util.*;

public class TwoSum {
	public static int[] twoSum_On2(int[] list, int sum) {
		/*
		int MAX = Integer.maximum;
		if (sum > MAX) {
			System.out.println("Out of bounrdry!");
			return new int[0];
		}
		*/
		for (int i = 0; i < list.length; i++) {
			for (int j = i; j < list.length; j++) {
				if (list[i] + list[j] == sum) {
					return new int[] {i, j};
				}
			}
		}
		return new int[0];
	}

	public static void main(String[] args) {
		int[] input = new int[] {2, 8, 4, 19};
		int sum = 6;
		int[] result = twoSum_On2(input, sum);
		for (int i : result) {
			System.out.println(i);
		}
	}
}