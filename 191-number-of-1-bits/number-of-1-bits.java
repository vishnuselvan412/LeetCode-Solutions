class Solution {
    public int hammingWeight(int n) {
        String binary = Integer.toString(n,2);
        int count = 0;
        for(int i=0;i<binary.length();i++){
            if(binary.charAt(i) == '1'){
                count++;
            }
        }

        return count;
    }
}