#include <iostream>
#include<algorithm>

using namespace std;

int main()
{
bool found;
string nstr;
int counter=2,i=5,div;

cout<< "Which prime would you like to find? n= ";
getline(cin,nstr);
int n=stoi(nstr);


    for(;;)
    {
        found=true;
        for(div=3;div<i/2;div+=2)
        if (!(i%div))
            found=false;
        if(found)
            counter+=1;
        if(counter>=n)
            break;
        i+=2;
    }
    cout<<"The "<<n<<" th prime is: "<<i;



    return 0;
}
