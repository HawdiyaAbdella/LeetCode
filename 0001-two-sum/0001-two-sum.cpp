class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        for (int i = 0; i < n; i++) {            
            for (int j = i + 1; j < n; j++) {   
                if (numbers[i] + numbers[j] == target) {
                    return {i , j };     
                }
            }
        }
        return {-1, -1}; 
    }
};
