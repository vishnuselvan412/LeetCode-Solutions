class Solution {
    public int subtractProductAndSum(int n) {
        int num = n;
        int sum = 0;
        int rev=1,rem;
        while(num!=0){
            rem = num % 10;
            rev = rev * rem;
            sum = sum + rem;
            num/=10;
        }
        int result;
        result = rev - sum;

        return result;
    }
}