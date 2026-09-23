#include <iostream>
#include <stack>
using namespace std;

bool isComplete(char op, char cl){
    if((op=='('&&cl==')')||(op=='{'&&cl=='}')||(op=='['&&cl==']')){
        return true;
    }
    return false;
}

void check(string s){
    stack<char> st;
    for(char c: s){
        if(c=='('||c=='{'||c=='['){
            st.push(c);
        }
        else{
            if(!isComplete(st.top(), c)){
                cout<<"Unbalanced"<<endl;
                return;
            }
            else{
                st.pop();
            }
        }
    }
    if(st.empty()){
        cout<<"Balanced"<<endl;
    }
}

int main(){
    string s="[({})]";
    string u="{(}]";
    check(s);
    check(u);
    return 0;
}