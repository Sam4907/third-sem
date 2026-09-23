#include <iostream>
using namespace std;

void activitySelection(int start[], int finish[], int n){
    cout<<"Selected Activities: ";
    int lastFinish=finish[0];
    cout<<"("<<start[0]<<","<<finish[0]<<") ";
    for(int i=1; i<n; i++){
        if(start[i]>=lastFinish){
            cout<<"("<<start[i]<<","<<finish[i]<<") ";
            lastFinish=finish[i];
        }
    }
    cout<<endl;
}

int main(){
    int start[]={1, 3, 0, 5, 8, 5};
    int finish[]={2, 4, 6, 7, 9, 9};
    activitySelection(start, finish, 6);
    return 0;
}