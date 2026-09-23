#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 0 1 2 3 4 5 6 7 8
// 1 1 2 2 3 3 4 5 5 
// 0   0   0   4 0    

int singlen(vector<int>&nums){
    vector<int>ans;
    sort(nums.begin(), nums.end());
    for(int i=0; i<nums.size(); i+=2){
        if(nums[i]!=nums[i+1]){
            ans.push_back(nums[i]);
            i++;
        }
        ans.push_back(nums[i]^nums[i+1]);
    }
    for(auto m: ans){
        if(m!=0){
            return m;
        }
    }
}

int main(){
    vector<int> vec1={5, 5, 1, 1, 2, 4, 2, 3, 3};
    vector<int> vec2={1, 2, 3, 1, 2};
    vector<int> vec3={4, 4, 1, 2, 1, 5, 5, 6, 2};
    vector<int> vec4={2, 9, 9};
    vector<int> vec5={2};
    cout<<singlen(vec1)<<endl;
    cout<<singlen(vec2)<<endl;
    cout<<singlen(vec3)<<endl;
    cout<<singlen(vec4)<<endl;
    cout<<singlen(vec5)<<endl;
    return 0;
}