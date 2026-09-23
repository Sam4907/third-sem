#include <iostream>
#include <algorithm>
using namespace std;

struct Item{ 
    int weight, value; 
};

bool compareRatio(Item a, Item b){
    double r1=(double) a.value/a.weight;
    double r2=(double) b.value/b.weight;
    return r1>r2; 
}

double fractionalKnapsack(Item items[], int n, int capacity) {
    sort(items, items+n, compareRatio);
    double totalValue=0;
    for(int i=0; i<n&&capacity>0; i++){
        if(items[i].weight<=capacity){
            totalValue+=items[i].value;
            capacity-=items[i].weight;
        } 
        else{
            totalValue+=items[i].value*((double) capacity/items[i].weight);
            capacity=0;
        }
    }
    return totalValue;
}

int main(){
    Item items[]={{10, 60}, {20, 100}, {30, 120}};
    cout<<"Maximum Profit= "<<fractionalKnapsack(items, 3, 50)<<endl;
    cout<<"Maximum Profit= "<<fractionalKnapsack(items, 3, 100)<<endl;
    return 0;
}