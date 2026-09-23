#include <iostream>
#include <vector>
using namespace std;

void merges(vector<int>&vec, int low, int mid, int high){
    vector<int>l, r, ans;
    for(int i=low; i<=mid; i++){
        l.push_back(vec[i]);
    }
    for(int i=mid+1; i<=high; i++){
        r.push_back(vec[i]);
    }
    int i=0, j=0;
    while(i<l.size()&&j<r.size()){
        if(l[i]<=r[j]){
            ans.push_back(l[i]);
            i++;
        }
        else{
            ans.push_back(r[j]);
            j++;
        }
    }
    while(i<l.size()){
        ans.push_back(l[i]);
        i++;
    }
    while(j<r.size()){
        ans.push_back(r[j]);
        j++;
    }
    for(int k=low; k<=high; k++){
        vec[k]=ans[k-low];
    }
}

void merge(vector<int>&vec, int low, int high){
    if(low>=high){
        return;
    }
    int mid=(low+high)/2;
    merge(vec, low, mid);
    merge(vec, mid+1, high);
    merges(vec, low, mid, high);
}

int main(){
    vector<int> ans={4, 3, 1, 5, 2, 10, 9, 11, 6, 7, 8};
    merge(ans, 0, ans.size()-1);
    for(int i: ans){
        cout<<i<<"\t";
    }
    cout<<endl;
    return 0;
}