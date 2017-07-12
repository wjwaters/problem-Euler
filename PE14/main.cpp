#include <iostream>

using namespace std;

int main()
{

//string mstr;
int n, number;
int counter;
int n_max=1;
int counter_max=0;

//cout<< "Find the largest collatz sequence for numbers under m? m= ";
//getline(cin,mstr);
//double m=stoi(mstr);



for (n=2;n<10;n++){
    counter=0;
    number=n;
    while(n>1)
        if(n%2==true){
            n=n/2;
            counter+=1;}
        else{
            n=3*n+1;
            counter+=1;}
    if(counter>counter_max){
        n_max=number;
        counter_max=counter;}
    }
cout<<"The longest collatz sequence for numbers under 14 is "<<counter_max<<" corresponding to number "<<n_max<<endl;

return 0;
}
