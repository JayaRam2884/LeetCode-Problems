class Solution {
    public static boolean isAlphaNumeric(char c) {
        return Character.isLetterOrDigit(c); // More robust
    }

    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        char[] A = s.toCharArray();
        int i = 0, j = A.length - 1;

        while (i < j) {
            if (!isAlphaNumeric(A[i])) {
                i++;
            } else if (!isAlphaNumeric(A[j])) {
                j--;
            } else {
                if (A[i] != A[j]) {
                    return false;
                }
                i++;
                j--;
            }
        }

        return true;
    }
}
