#include <iostream>
using namespace std;

int sumofn(int n){
    return n*(n+1)/2;
}

int sumrecur(int n){
    if(n==0){
        return 0;
    }
    return n+sumrecur(n-1);
}

int main(){
    int num;
    cout<<"Enter a number: ";
    cin>>num;
    cout<<"The sum of "<<num<<" numbers is: "<<sumofn(num)<<endl;
    cout<<"The sum of "<<num<<" numbers is: "<<sumrecur(num)<<endl;
    return 0;
}