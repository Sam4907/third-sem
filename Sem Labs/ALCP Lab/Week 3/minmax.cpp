#include <iostream>
#include <vector>
using namespace std;

void maxmin(vector<int>&arr, int i, int j, int &max, int &min){
    if(i==j){
        max=min=arr[i];
    }
    else if(i==j-1){
        if(arr[i]>arr[j]){
            min=arr[j];
            max=arr[i];
        }
        else{
            min=arr[i];
            max=arr[j];
        }
    }
    else{
        int mid=(i+j)/2;
        int max1, min1;
        maxmin(arr, i, mid, max, min);
        maxmin(arr, mid+1, j, max1, min1);
        if(max<max1){
            max=max1;
        }
        if(min>min1){
            min=min1;
        }
    }
}

int main(){
    vector<int>vec={5, 4, 1, 2, 3};
    int rmin, rmax;
    maxmin(vec, 0, vec.size()-1, rmax, rmin);
    cout<<"Maximum: "<<rmax<<endl<<"Minimum: "<<rmin<<endl;
    return 0;
}