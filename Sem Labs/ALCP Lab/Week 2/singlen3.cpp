#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

int singlen(vector<int>&nums){
    sort(nums.begin(), nums.end());
    for(int i=1; i<nums.size(); i+=2){
        if(nums[i]!=nums[i-1]){
            return nums[i-1];
        }
    }
    return nums[nums.size()-1];
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
