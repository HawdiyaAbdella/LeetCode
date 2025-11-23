class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
       for(int i=0; i<nums.size();i++){
        for(int j=0; j< nums.size();j++)
        {
            if(nums[i]%2==0)
            {
                int temp=nums[i];
                nums[i]=nums[j];
                nums[j]= temp;
            }
        }
       } 
return nums;
    }
};