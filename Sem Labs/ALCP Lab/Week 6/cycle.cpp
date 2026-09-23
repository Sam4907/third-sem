#include <iostream>
#include <vector>
using namespace std;

bool dfs(vector<int>adjmat[], vector<bool>&visited, int c, int p){
    visited[c]=true;
    for(int v: adjmat[c]){
        if(!visited[v]){
            if(dfs(adjmat, visited, v, c)){
                return true; 
            }
        }
        else if(v!=p){
            return true;
        }
    }
    return false;
}

bool hasCycle(vector<int> adjmat[], int n){
    vector<bool> visited(n+1, false);
    for(int u=1; u<=n; u++){
        if(!visited[u]){
            if(dfs(adjmat, visited, u, -1)){
                return true;
            }
        }
    }
    return false;
}

int main(){
    int n=4;
    vector<int> adj[n+1];
    adj[1].push_back(2); 
    adj[2].push_back(1);
    adj[2].push_back(3); 
    adj[3].push_back(2);
    adj[3].push_back(4); 
    adj[4].push_back(3);
    adj[4].push_back(2); 
    adj[2].push_back(4);
    if(hasCycle(adj, n)){
        cout<<"Cycle detected"<<endl;
    }
    else{
        cout<<"Cycle not detected"<<endl;
    }
    return 0;
}