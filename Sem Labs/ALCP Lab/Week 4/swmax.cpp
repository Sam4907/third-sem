#include <iostream>
#include <vector>
using namespace std;

vector<int> swmax(vector<int>arr, int k){
    int r=0;
    vector<int>ans;
    for(int l=0; r<arr.size(); l++){
        r=l+1;
        int curr=arr[l];
        while(r-l!=k){
            curr=max(curr, arr[r]);
            r++;
        }
        ans.push_back(curr);
    }
    return ans;
}

int main(){
    vector<int>ans={9, 1, 12, 54, 32, 21, 11, 99, 100};
    vector<int>ch=swmax(ans, 3);
    for(auto i: ch){
        cout<<i<<"\t";
    }
    cout<<endl;
    return 0;
}