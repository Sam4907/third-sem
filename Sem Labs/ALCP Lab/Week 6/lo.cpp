#include <iostream>
#include <queue>
using namespace std;

struct Node{
    Node* left;
    Node* right;
    int val;
};

void lo(Node* root){
    vector<int>ans;
    queue<Node*>q;
    q.push(root);
    while(!q.empty()){
        Node* curr=q.front();
        ans.push_back(curr->val);
        if(curr->left){
            q.push(curr->left);
        }
        if(curr->right){
            q.push(curr->right);
        }
        q.pop();
    }
    for(auto i: ans){
        cout<<i<<"\t";
    }
    cout<<endl;
}

int main(){
    Node* root=new Node();
    root->val=1;
    root->left=new Node();
    root->left->val=4;
    root->right=new Node();
    root->right->val=2;
    root->left->left=new Node();
    root->left->left->val=3;
    root->left->left->right=new Node();
    root->left->left->right->val=5;
    lo(root);
    return 0;
}