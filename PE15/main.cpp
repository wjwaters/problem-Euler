#include <iostream>
#include"binomial.h"
#include"factorial.h"

using namespace std;

int main()
{

string astr, bstr;

cout<< "Find the number of possible paths for rectangular lattice from top left to bottom right where only movements down or right are allowed. What are the dimensions of the lattice axb? a= ";
getline(cin,astr);
cout<<" b = ";
getline(cin,bstr);

int a=stoi(astr);
int b=stoi(bstr);

int p=a+b;
double num_path=binomial(p,a);

cout<<"The number of possible paths is "<<num_path;

return 0;
}
