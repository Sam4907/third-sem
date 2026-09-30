#include <iostream>
#include <vector>
using namespace std;

int V=4;

bool isSafe(vector<int>&path, int v, int pos, vector<vector<int>>graph){
    if(!graph[path[pos-1]][v]){
        return false;
    }
    for(int i=0; i<pos; i++){
        if(path[i]==v){
            return false;
        }
    }
    return true;
}

void hamcycle(vector<int>& path, int pos, int& solutionCount, vector<vector<int>>graph){
    if(pos==V){
        if(graph[path[pos-1]][path[0]]){
            solutionCount++;
            cout<<"Solution "<<solutionCount<<": ";
            for(int v: path){
                cout<<v<< " -> ";
            }
            cout<<path[0]<<endl; 
        }
        return;
    }
    
    for(int v=1; v<V; v++){
        if(isSafe(path, v, pos, graph)){
            path[pos]=v;
            hamcycle(path, pos+1, solutionCount, graph);
            path[pos]=-1; 
        }
    }
}

int main(){
    vector<int> path(V, -1);
    path[0]=0;
    int m=0;
    int s=0;
    vector<vector<int>>graph1={{0, 0, 1, 1}, {1, 1, 1, 0}, {1, 0, 1, 0}, {1, 0, 0, 1}};
    vector<vector<int>>graph2={{0, 0, 1, 1}, {1, 1, 0, 1}, {1, 1, 1, 1}, {1, 1, 0, 1}};
    hamcycle(path, 1, m, graph1);
    if(m==0){
        cout<<"No cycle detected"<<endl;
    }
    hamcycle(path, 1, s, graph2);
    if(s==0){
        cout<<"No cycle detected"<<endl;
    }
    return 0;
}