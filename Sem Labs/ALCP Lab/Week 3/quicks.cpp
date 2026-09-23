#include <iostream>
#include <vector>
using namespace std;

int partition(vector<int>& arr, int low, int high){
    int pivot=arr[high]; 
    int i=low-1;       
    for(int j=low; j<high; j++){
        if(arr[j]<=pivot){
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i+1], arr[high]);
    return (i+1);
}

void quickSort(vector<int>& arr, int low, int high) {
    if(low<high){
        int pi=partition(arr, low, high);
        quickSort(arr, low, pi-1);
        quickSort(arr, pi+1, high);
    }
}

int main(){
    vector<int>vec={1, 2, 5, 6, 8, 9, 3, 4, 7};
    quickSort(vec, 0, vec.size()-1);
    for(auto v: vec){
        cout<<v<<"\t";
    }
    cout<<endl;
    return 0;
}