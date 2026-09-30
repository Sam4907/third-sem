#include <iostream>
#include <vector>
using namespace std;

bool isSafe(vector<int>&board, int row, int column){
    for(int r=0; r<row; r++){
        int c=board[r];
        if (c==column||abs(c-column)==abs(r-row)){
            return false;
        }
    }
    return true;
}

void printBoard(const vector<int>& board, int n) {
    for(int r=0; r<n; r++){
        for(int c=0; c<n; c++){
            if(board[r]==c){
                cout<<"Q ";
            } 
            else{
                cout<<". ";
            }
        }
        cout<<"\n";
    }
    cout<<"\n"; 
}

void nq(vector<int>& board, int row, int n, int& solutionCount) {
    if(row==n){
        solutionCount++;
        cout<<"Solution "<<solutionCount<<": ";
        for(int c: board){
            cout<<c<<" ";
        }
        cout<<endl;
        printBoard(board, n);
        return; 
    }
    for(int col=0; col<n; col++){
        if(isSafe(board, row, col)){
            board[row]=col; 
            nq(board, row+1, n, solutionCount); 
            board[row]=-1; 
        }
    }
}

int main(){
    int n;
    cout<<"Enter value of n: ";
    cin>>n;
    vector<int>board(n, -1);
    int s=0;
    nq(board, 0, n, s);
    return 0;
}