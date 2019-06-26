/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param root: A Tree
     * @return: Postorder in ArrayList which contains node values.
     */
    public List<Integer> postorderTraversal(TreeNode root) {
        // write your code here
        List<Integer> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        TreeNode prev = null;
        TreeNode curt = null;
        while (!stack.empty()) {
            curt = stack.peek();
            if (prev == null || prev.left == curt || prev.right == curt) {
                if (curt.left != null) {
                    stack.push(curt.left);
                } else if (curt.right != null) {
                    stack.push(curt.right);
                }
            } else if (curt.left == prev) {
                if (curt.right != null) {
                    stack.push(curt.right);
                }
            } else {
                result.add(curt.val);
                stack.pop();
            }
            prev = curt;
        }
        return result;
    }
}