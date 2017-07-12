#include <iostream>
#include"factorial.h"

using namespace std;

double binomial(int n,int k){
double binom;
binom=factorial(n)/(factorial(k)*factorial(n-k));

return binom;

}
