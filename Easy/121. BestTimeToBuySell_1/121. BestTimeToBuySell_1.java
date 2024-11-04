class Solution {
    public int maxProfit(int[] prices) {
        int s = Integer.MAX_VALUE, mp = Integer.MIN_VALUE;

        for(int price: prices){
            if(price < s){s=price;}
            mp = Math.max(mp, price - s);
        }
        return mp;
    }
}