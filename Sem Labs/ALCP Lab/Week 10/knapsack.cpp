#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Item{ 
    int weight, value; 
};

double knap(int index, int currentWeight, int currentValue, int n_items, const vector<Item>& items, int capacity){
    if(currentWeight>=capacity){
        return 0;
    }
    double result=currentValue;
    int totalWeight=currentWeight;
    int i; 
    for(i=index; i<n_items&&totalWeight+items[i].weight<=capacity; i++){
        totalWeight+=items[i].weight;
        result+=items[i].value;
    }
    if(i<n_items&&totalWeight<capacity){
        result+=(capacity-totalWeight)*((double)items[i].value/items[i].weight);
    }
    return result;
}

void knapsackbnb(int index, int currentWeight, int currentValue, int n_items, const vector<Item>& items, 
                 int capacity, int &bestValue, vector<bool>& currentSelection, vector<bool>& bestSelection){
    if(currentWeight>capacity){
        return;
    }
    if(currentValue>bestValue){
        bestValue=currentValue;
        bestSelection=currentSelection; 
    }
    if(index==n_items){
        return;
    }
    if(knap(index, currentWeight, currentValue, n_items, items, capacity)<=bestValue){
        return;
    }
    currentSelection[index]=true;
    knapsackbnb(index+1, currentWeight+items[index].weight, currentValue+items[index].value, n_items, items, capacity, bestValue, currentSelection, bestSelection);
    currentSelection[index]=false;
    knapsackbnb(index+1, currentWeight, currentValue, n_items, items, capacity, bestValue, currentSelection, bestSelection);
}

int main(){
    int n, capacity;
    cout<<"Enter the number of items: ";
    cin>>n;
    cout<<"Enter the capacity: ";
    cin>>capacity;
    vector<Item> items(n);
    int bestValue=0;
    for(int i=0; i<n; i++){
        cout<<"Enter the weight of item["<<i<<"]: ";
        cin>>items[i].weight;
        cout<<"Enter the profit of item["<<i<<"]: ";
        cin>>items[i].value;
    }
    sort(items.begin(), items.end(), [](const Item& a, const Item& b){
        return (double)a.value/a.weight>(double)b.value/b.weight;
    });
    vector<bool> currentSelection(n, false);
    vector<bool> bestSelection(n, false);
    knapsackbnb(0, 0, 0, n, items, capacity, bestValue, currentSelection, bestSelection); 
    cout<<"0/1 Knapsack Best Value: "<<bestValue<<endl;
    cout<<"Solution Set: ";
    bool itemsFound=false;
    for(int i=0; i<n; i++){
        if(bestSelection[i]){
            cout <<"1"<< " ";
            itemsFound=true;
        }
        else{
            cout<<"0"<<" ";
        }
    }
    if(!itemsFound){
        cout<<"None";
    }
    cout<<endl;
    return 0;
}