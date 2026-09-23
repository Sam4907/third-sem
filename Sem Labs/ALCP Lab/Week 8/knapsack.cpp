#include <iostream>
#include <vector>
using namespace std;

void knapsack(int n, vector<int>weights, vector<int>profit, int m){
    vector<vector<int>>dp(n+1, vector<int>(m+1, 0));
    for(int i=1; i<=n; i++){
        for(int j=1; j<=m; j++){
            if(weights[i-1]<=m){
                dp[i][j]=max(profit[i-1]+dp[i-1][j-weights[i-1]], dp[i-1][j]);
            }
            else{
                dp[i][j]=dp[i-1][j];
            }
        }
    }
    int ans=dp[n][m];
    vector<int>res(n, 0);
    for(int i=n; i>0; i--){
        if(dp[i][ans]!=dp[i-1][ans]){
            res[i-1]=1;
            ans-=weights[i-1];
        }
    }   
    cout<<"Solution set: ";
    for(int i: res){
        cout<<i<<" ";
    }
    cout<<endl;
    cout<<"Maximum profit: "<<dp[n][m]<<endl;
}

int main(){
    /*int n, m;
    cout<<"Enter the number of items: ";
    cin>>n;
    vector<int>weights(n);
    vector<int>profits(n);
    for(int i=0; i<n; i++){
        cout<<"Enter weight of item "<<i<<": ";
        cin>>weights[i];
        cout<<"Enter profit of item "<<i<<": ";
        cin>>profits[i];
        cout<<endl;
    }
    cout<<"Enter the maximum weight: ";
    cin>>m;*/
    int n=4, m=8;
    vector<int>weights={2, 3, 4, 5};
    vector<int>profits={1, 2, 5, 6};
    knapsack(n, weights, profits, m);
    return 0;
}

/*2, 1
3, 2
4, 5
5, 6*/
