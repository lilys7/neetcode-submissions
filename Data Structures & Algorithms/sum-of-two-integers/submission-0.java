class Solution {
    public int getSum(int a, int b) {
        //keeps 32 bit integer
        
        while (b != 0) {
            int res = (a & b) << 1;
            a = a ^ b;
            b = res;
        }
        return a;
    }
}
