#include <iostream>
#include <vector>
#include <stack>
using namespace std;

#include <vector>
#include <stack>

using namespace std;

vector<int> nextg(vector<int>& nums) {
    int n = nums.size();
    vector<int> ans(n, -1); // Initialize answer array with -1
    stack<int> st;

    // Traverse the array from right to left
    for (int i = n - 1; i >= 0; i--) {
        // Pop elements from the stack that are smaller than or equal to current element
        while (!st.empty() && st.top() <= nums[i]) {
            st.pop();
        }

        // If stack is not empty, the top element is the next greater element
        if (!st.empty()) {
            ans[i] = st.top();
        }

        // Push current element onto the stack for upcoming elements
        st.push(nums[i]);
    }

    return ans;
}


int main(){
    vector<int>vec={55, 55, 10, 10, 11, 21, 22, 1};
    for(auto i: vec){
        cout<<i<<"\t";
    }
    cout<<endl;
    vector<int>ans=nextg(vec);
    for(auto i: ans){
        cout<<i<<"\t";
    }
    cout<<endl;
    return 0;
}