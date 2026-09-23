#include <iostream>
using namespace std;

int gcd(int a, int b){
    return b==0?a:gcd(b, a%b);
}

int gcdOfOddEvenSums(int n){
    int sumEven=0, sumOdd=0, i=2, j=1, count=0;
    while(count<n){
        sumEven+=i;
        sumOdd+=j;
        i+=2;
        j+=2;
        count++;
    }
    return gcd(sumEven, sumOdd);
}

int main(){
    cout<<gcdOfOddEvenSums(1002);
    return 0;
}