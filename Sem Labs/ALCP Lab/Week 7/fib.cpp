#include <iostream>
#include <vector>
using namespace std;

int fibonacci(int n){
    if(n==0||n==1){
        return 1;
    }
    vector<int>dp(n-1, 0);
    dp[1]=1;
    dp[2]=2;
    for(int i=3; i<=n; i++){
        dp[i]=dp[i-1]+dp[i-2];
    }
    return dp[n];
}

int main(){
    int n=0;
    cout<<"Enter the number: ";
    cin>>n;
    cout<<"Result: "<<fibonacci(n)<<endl;
    return 0;
}