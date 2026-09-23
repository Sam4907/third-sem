#include <iostream>
#include <vector>
using namespace std;

int bsearch(vector<int>&vec, int low, int high, int key){
    if(low>high){
        return -1;
    }
    int mid=(low+high)/2;
    if(vec[mid]==key){
        return mid;
    }
    else if(vec[mid]>key){
        return bsearch(vec, low, mid-1, key);
    }
    else{
        return bsearch(vec, mid+1, high, key);
    }
}

int main(){
    vector<int>res={1, 2, 3, 4, 5};
    int ans=bsearch(res, 0, res.size()-1, 4);
    if(ans==-1){
        cout<<"Target not found"<<endl;
    }
    else{
        cout<<"Target found at index: "<<ans<<endl;
    }
    return 0;
}