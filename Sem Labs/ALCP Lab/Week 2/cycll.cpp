#include <iostream>
using namespace std;

struct Node{
    int val;
    Node* next;
    Node(int v){
        val=v;
        next=NULL;
    }
};

bool cycle(Node* head){
    if(!head||!head->next){
        return false;
    }
    Node* f=head;
    Node* s=head;
    while(f&&f->next){
        s=s->next;
        f=f->next->next;
        if(s==f){
            return true;
        }
    }
    return false;
}

int main(){
    Node* head=new Node(0);
    (cycle(head))?cout<<"True"<<endl:cout<<"False"<<endl;
    head->next=new Node(1);
    (cycle(head))?cout<<"True"<<endl:cout<<"False"<<endl;
    head->next->next=new Node(2);
    (cycle(head))?cout<<"True"<<endl:cout<<"False"<<endl;
    head->next->next->next=new Node(3);
    head->next->next->next->next=new Node(4);
    head->next->next->next->next->next=new Node(5);
    head->next->next->next->next->next=head->next->next;
    (cycle(head))?cout<<"True"<<endl:cout<<"False"<<endl;
    return 0;
}