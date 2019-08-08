public class Solution {
    /**
     * @param L: Given n pieces of wood with length L[i]
     * @param k: An integer
     * @return: The maximum length of the small pieces
     */

    public int woodCut(int[] L, int k) {
        if (L == null || L.length == 0) {
            return 0;
        }
        
        int end = 0, start = 1;
        for (int l : L) {
            end = Math.max(l, end);
        }
        
        /**
         * Find last position <= target
         */
        while(start + 1 < end) {
            int mid = (end - start) / 2 + start;
            int numPieces = 0;
            for (int l : L) {
                numPieces += l / mid;
            }
            if (numPieces >= k) {
                start = mid;
            } else {
                end = mid;
            }
        }
        
        int numPiecesS = 0, numPiecesE = 0;
        for (int l : L) {
            numPiecesS += l / start;
            numPiecesE += l / end;
        }
        if (numPiecesE >= k) {
            return end;
        } 
        if (numPiecesS >= k) {
            return start;
        } 
        return 0;
        
    }
}