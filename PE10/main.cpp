#include <iostream>
#include<algorithm>
#include<array>

using namespace std;

int main()
{

string nstr;
int sum_of_primes,i,prime;

cout<< "This code calculates the sum of primes below n, what value of n would you like? n= ";
getline(cin,nstr);
int n=stoi(nstr);


int vect[n]={};
prime=3;
sum_of_primes=2;

while(prime<n){
    if (vect[prime]==0){
        sum_of_primes+=prime;
        i=prime;}
        while(i<n){
            vect[i]=1;
            i+=prime;}
    prime+=2;}

cout<<"The sum of primes below "<<n<<" is: "<<sum_of_primes;



return 0;
}
