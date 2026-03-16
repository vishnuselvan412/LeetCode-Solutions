class Solution {
    public void duplicateZeros(int[] arr) {
        int[] result = new int[arr.length];
        int j = 0;
        for (int i = 0; i < arr.length && j < arr.length; i++) {
            result[j++] = arr[i];
            if (arr[i] == 0 && j < arr.length) {
                result[j++] = 0;  // duplicate the zero
            }
        }
        // copy back to arr
        for (int i = 0; i < arr.length; i++) {
            arr[i] = result[i];
        }
    }
}