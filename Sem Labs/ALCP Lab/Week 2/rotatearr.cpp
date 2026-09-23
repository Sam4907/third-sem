#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void rotate(vector<int>&nums, int k){
    int n=nums.size();
    k%=n;
    reverse(nums.begin(), nums.end());
    reverse(nums.begin(), nums.begin()+k);
    reverse(nums.begin()+k, nums.end());
    for(auto i: nums){
        cout<<i<<"\t";
    }
    cout<<endl;
}

int main(){
    vector<int> vec1={1, 2, 3, 4, 5, 6, 7, 8};
    vector<int> vec2={5, 6, 7, 1, 2, 3, 4};
    vector<int> vec3={3, 2, 1, 1, 2, 3};
    vector<int> vec4={2, 1};
    vector<int> vec5={2};
    rotate(vec1, 4);
    rotate(vec2, 4);
    rotate(vec3, 3);
    rotate(vec4, 1);
    rotate(vec5, 2);
    return 0;
}