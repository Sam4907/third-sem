#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void lcs(string x, string y){
    int m=x.size(), n=y.size();
    vector<vector<int>>dp(m+1, vector<int>(n+1, 0));
    for(int i=1; i<=m; i++){
        for(int j=1; j<=n; j++){
            if(x[i]==y[j]){
                dp[i][j]=1+dp[i-1][j-1];
            }
            else{
                dp[i][j]=max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    string lcss="";
    int i=m, j=n;
    while(i>0&&j>0){
        if(x[i-1]==y[j-1]){
            lcss.push_back(x[i-1]);
            i--;
            j--;
        }
        else if(dp[i-1][j]>dp[i][j-1]){
            i--;
        }
        else{
            j--;
        }
    }
    reverse(lcss.begin(), lcss.end());
    cout<<"LCS String: "<<lcss<<endl;
    cout<<"Length of lcs: "<<dp[n][m]<<endl;
}

int main(){
    //string x, y;
    /*cout<<"Enter string 1: ";
    cin>>x;
    cout<<"Enter string 2: ";
    cin>>y;*/
    string x="abaaba";
    string y="babbab";
    lcs(x, y);
    return 0;
}