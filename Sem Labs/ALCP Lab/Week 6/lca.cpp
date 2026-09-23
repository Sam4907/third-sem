#include <iostream>
using namespace std;

struct Node{
    Node* left;
    Node* right;
    int val;
};

Node* lca(Node* root, Node* p, Node* q){
    if(!root||root==p||root==q){
        return root;
    }
    Node* l=lca(root->left, p, q);
    Node* r=lca(root->right, p, q);
    if(l&&r){
        return root;
    }
    return l?l:r;
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
    root->left->right=new Node();
    root->left->right->val=9;
    root->left->left->right=new Node();
    root->left->left->right->val=5;
    root->left->right->right=new Node();
    root->left->right->right->val=7;
    Node* ans=lca(root, root->left->left, root->left->right);
    cout<<ans->val<<endl;
    return 0;
}