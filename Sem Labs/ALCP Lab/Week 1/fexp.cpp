#include <iostream>
using namespace std;

int fexp(int a, int b, int m){
    int res=1;
    while(b>0){
        if(b%2==0){
            res=(res*a)%m;
        }
        a=(a*a)%m;
        b/=2;
    }
    return res;
}

int main(){
    int a, b, m;
    cout<<"Enter a, b and m: ";
    cin>>a>>b>>m;
    cout<<a<<"^"<<b<<" mod "<<m<<"="<<fexp(a, b, m)<<endl;
    return 0;
}