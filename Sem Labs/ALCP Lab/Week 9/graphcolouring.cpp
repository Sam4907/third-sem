#include <iostream>
#include <vector>
using namespace std;

int V=4;
int graph[4][4]={{0, 1, 1, 1}, {1, 1, 0, 0}, {1, 0, 0, 0}, {0, 1, 1, 1}};

bool isSafe(vector<int>&colour, int v, int c){
    for(int i=0; i<V; i++){
        if(graph[v][i]&&colour[i]==c){
            return false;
        }
    }
    return true;
}

bool graphc(vector<int>&colour, int v, int m){
    if(v==V){
        return true;
    }
    for(int c=1; c<=m; c++){
        if(isSafe(colour, v, c)){
            colour[v]=c;
            if(graphc(colour, v+1, m)){
                return true;
            }
            colour[v]=0;
        }
    }
    return false;
}

int main(){
    vector<int>color(V, 0);
    int m=4; 
    if(graphc(color, 0, m)){
        cout<<"Graph Coloring solution: ";
        for(int c: color){
            cout<<c<<" ";
        }
        cout<<endl;
    } 
    else{
        cout<<"No solution with "<<m<<" colors"<<endl;
    }
    return 0;
}