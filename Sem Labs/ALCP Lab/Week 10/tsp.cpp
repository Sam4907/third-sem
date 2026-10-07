#include <iostream>
#include <algorithm>
#include <vector>
#include <climits> 
using namespace std;

void tsp(int currentCity, int level, int currentCost, int count, int numCities, 
         const vector<vector<int>>& cost, vector<bool>& visitedCity, int &bestTourCost,
         vector<int>& currentPath, vector<int>& bestPath){
    if(level==numCities&&cost[currentCity][0]>0){
        if(currentCost+cost[currentCity][0]<bestTourCost){
            bestTourCost=currentCost+cost[currentCity][0];
            bestPath=currentPath; 
        }
        return;
    }
    for(int next=0; next<numCities; next++){
        if(!visitedCity[next]&&cost[currentCity][next]>0){
            if(currentCost+cost[currentCity][next]>=bestTourCost){
                continue;
            }
            visitedCity[next]=true;
            currentPath.push_back(next); 
            tsp(next, level+1, currentCost+cost[currentCity][next], count+1, 
                numCities, cost, visitedCity, bestTourCost, currentPath, bestPath);  
            currentPath.pop_back();      
            visitedCity[next]=false; 
        }
    }
}

int main(){
    int nc;
    cout<<"Enter the number of cities: ";
    cin>>nc;
    vector<vector<int>> cost(nc, vector<int>(nc, 0));
    vector<bool> visitedCity(nc, false);
    int bestTourCost=INT_MAX;
    cout<<"Enter the cost adjacency matrix: "<<endl;
    for(int i=0; i<nc; i++){
        for(int j=0; j<nc; j++){
            cin>>cost[i][j];
        }
    }
    vector<int> currentPath;
    vector<int> bestPath;
    fill(visitedCity.begin(), visitedCity.end(), false);
    visitedCity[0]=true;
    currentPath.push_back(0); 
    tsp(0, 1, 0, 1, nc, cost, visitedCity, bestTourCost, currentPath, bestPath);
    cout<<"TSP Minimum Tour Cost: "<<bestTourCost<<endl;
    if(bestTourCost!=INT_MAX){
        cout<<"Optimal Path: ";
        for(int city: bestPath){
            cout<<city<< "->";
        }
        cout<<"0"<<endl; 
    } 
    else{
        cout<<"No valid TSP path exists."<<endl;
    }
    return 0;
}
