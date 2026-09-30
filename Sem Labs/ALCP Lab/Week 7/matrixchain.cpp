#include <iostream>
#include <vector>
#include <climits>

using namespace std;

// Recursive function to print the optimal parenthesization using the split table
void printParenthesis(int i, int j, const vector<vector<int>>& bracket, char& name) {
    if (i == j) {
        cout << name++;
        return;
    }

    cout << "(";
    printParenthesis(i, bracket[i][j], bracket, name);
    printParenthesis(bracket[i][j] + 1, j, bracket, name);
    cout << ")";
}

void matrixChainOrder(const vector<int>& arr) {
    int n = arr.size();
    
    vector<vector<int>> dp(n, vector<int>(n, 0));
    vector<vector<int>> bracket(n, vector<int>(n, 0));

    for (int len = 2; len < n; len++) {
        for (int i = 1; i < n - len + 1; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;

            for (int k = i; k < j; k++) {
                int cost = dp[i][k] + dp[k + 1][j] + (arr[i - 1] * arr[k] * arr[j]);
                
                if (cost < dp[i][j]) {
                    dp[i][j] = cost;
                    bracket[i][j] = k;
                }
            }
        }
    }

    cout << "\n----------------------------------------\n";
    cout << "Minimum number of multiplications: " << dp[1][n - 1] << endl;
    
    char name = 'A'; 
    cout << "Optimal Parenthesization: ";
    printParenthesis(1, n - 1, bracket, name);
    cout << "\n----------------------------------------" << endl;
}

int main() {
    int numMatrices;
    cout << "Enter the number of matrices: ";
    if (!(cin >> numMatrices) || numMatrices <= 0) {
        cout << "Invalid number of matrices." << endl;
        return 1;
    }

    // For 'N' matrices, we need an array of size 'N + 1' to store dimensions
    vector<int> arr(numMatrices + 1);

    cout << "Enter the dimensions sequence (separated by spaces or newlines):\n";
    cout << "(Note: For " << numMatrices << " matrices, you must enter " << numMatrices + 1 << " values)\n";
    
    for (int i = 0; i <= numMatrices; i++) {
        cout << "Dimension " << i << ": ";
        cin >> arr[i];
        if (arr[i] <= 0) {
            cout << "Dimensions must be positive integers!" << endl;
            return 1;
        }
    }

    matrixChainOrder(arr);
    
    return 0;
}
