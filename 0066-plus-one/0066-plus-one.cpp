class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry=1;
        int size = digits.size();
        for(int i=size-1; i>=0;i--){
            if((digits[i]+carry)/10){
                int temp = digits[i];
                digits[i] = (digits[i]+carry)%10;
                carry = (temp+carry)/10;
            }
            else{
                digits[i] = digits[i]+1;
                carry=0;
                break;
            }
        }
        if(carry){
            digits.push_back(0);
            for(int i=size-1; i>0;i--){
                digits[i] = digits[i-1];
            }
            digits[0] = carry;
        }
        
        return digits;
    }
};