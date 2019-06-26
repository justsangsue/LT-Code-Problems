public class Solution {
    /**
     * @param pages: an array of integers
     * @param k: An integer
     * @return: an integer
     */
    public int countCopiers(int[] pages, int n) {
        int k = 0, total = 0;
        for (int page : pages) {
            if (total + page > n) {
                k++;
                total = 0;
            }
            total += page;
        }
        
        return k + (total > 0 ? 1 : 0);
    } 
    
    public int copyBooks(int[] pages, int k) {
        if (pages == null || pages.length == 0) {
            return 0;
        }
        
        int start = 0, end = 0;
        for (int page : pages) {
            start = Math.max(page, start);
            end += page;
        }
        
        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;
            if (countCopiers(pages, mid) <= k) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        
        if (countCopiers(pages, start) <= k) {
            return start;
        }
        return end;
    }
}