#include <iostream>

using namespace std;

int main()
{
   int i, sumSq=0, Sum=0, sqSum, diff;
   string nstr;

   cout<<"How many numbers would you like to sum? ";
   getline(cin,nstr);

   int n=stoi(nstr)+1;

   for (i=0;i<n;i++){
            sumSq+=i*i;
            Sum+=i;
   }
   sqSum=Sum*Sum;
   diff=sqSum-sumSq;

   cout <<"The sum of the squares of the first "<<nstr<<" numbers is: "<<sumSq;
   cout <<". The square of the sum of the first "<<nstr<<" numbers is: "<<sqSum;
   cout <<". The difference is "<<diff;

    return 0;
}
