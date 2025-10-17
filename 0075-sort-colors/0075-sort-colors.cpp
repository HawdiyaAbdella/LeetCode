class Solution {
public:
    void sortColors(vector<int>& nums) {
      int n= nums.size();
      int i,j;

       for (i=0; i<n;i++)
       {
        int minindex=i;
        for (j=i+1;j<n;j++)
         { 
         if ( nums[j]<nums[minindex])
            minindex = j;

          }
         
          int temp= nums[i];
          nums[i]=nums[minindex];
          nums[minindex]=temp;
    
       }
    }
};