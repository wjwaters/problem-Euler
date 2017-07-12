#include <iostream>


using namespace std;

double factorial(int j){
double fact=1;
int N =j+1;
int i;
for (i=1;i<N;i++)
{
    fact*=i;
}
return fact;

}
