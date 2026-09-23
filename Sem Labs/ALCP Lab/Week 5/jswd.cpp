#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Job{ 
    char id; 
    int deadline, profit; 
};

bool compareProfit(Job a, Job b){
    return a.profit>b.profit;
}

void jobSequencing(Job jobs[], int n){
    sort(jobs, jobs+n, compareProfit);
    int maxDeadline=0;
    for(int i=0; i<n; i++){
        maxDeadline=max(maxDeadline, jobs[i].deadline);
    }
    vector<int> slot(maxDeadline+1, -1);
    int totalProfit=0;
    for(int i=0; i<n; i++){
        for(int j=min(maxDeadline, jobs[i].deadline); j>=1; j--){
            if(slot[j]==-1){
                slot[j]=i;
                totalProfit+=jobs[i].profit;
                break;
            }
        }
    }
    cout<<"Scheduled Jobs: ";
    for(int j=1; j<=maxDeadline; j++){
        if(slot[j]!=-1){
            cout<<jobs[slot[j]].id<<" ";
        }
    }
    cout<<endl<<"Maximum Profit= "<<totalProfit<<endl;
}

int main(){
    Job jobs1[]={{'J', 2, 100}, {'A', 1, 19}, {'B', 2, 27}, {'C', 1, 25}, {'D', 3, 15}};
    Job jobs2[]={{'P', 12, 50}, {'Q', 4, 50}, {'R', 1, 1}, {'S', 3, 12}};
    Job jobs3[]={{'J', 6, 7}};
    jobSequencing(jobs1, 5);
    jobSequencing(jobs2, 4);
    jobSequencing(jobs3, 1);
    return 0;
}
