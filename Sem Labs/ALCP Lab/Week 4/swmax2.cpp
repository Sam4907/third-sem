#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> swmax(vector<int>& nums, int k) {
    int n=nums.size();
    vector<int>res;
    deque<int>q;
    for(int i=0; i<n; i++){
        if(!q.empty()&&q.front()<=i-k){
            q.pop_front();
        }
        while(!q.empty()&&nums[q.back()]<=nums[i]){
            q.pop_back();
        }
        q.push_back(i);
        if(i>=k-1){
            res.push_back(nums[q.front()]);
        }
    }
    return res;
}

int main(){
    vector<int>ans={23, 12, 43, -2, -1, 9, 0, 1007};
    vector<int>ch=swmax(ans, 2);
    for(auto i: ch){
        cout<<i<<"\t";
    }
    cout<<endl;
    return 0;
}
