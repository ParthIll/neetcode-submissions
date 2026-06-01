class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> num = new HashSet<Integer>();
        for(int i=0;i<nums.length;i++){
            boolean isAdded = num.add(nums[i]);
            if(!isAdded){
                return true;
            }
        }
        return false;
    }
}