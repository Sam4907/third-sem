#include <iostream>
using namespace std;

bool poweroftwo(int n){
    if(n<=0){
        return false;
    }
    return (n&(n-1))==0;
}

int main(){
    int n;
    cout<<"Enter a number: ";
    cin>>n;
    poweroftwo(n)?cout<<"True"<<endl:cout<<"False"<<endl;
    return 0;
}