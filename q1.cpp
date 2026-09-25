#include<iostream>
using namespace std;
int main(){
    int res=100;
    int *ptr=&res;
    cout<<"ptr value:"<<ptr<<endl;
    cout<<*ptr;
    return 0;
    
}