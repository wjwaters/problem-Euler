#include <iostream>
#include <math.h>

using namespace std;

int main()
{


bool Test=false;
int a_final,b_final,c_final,product,a,b;
float temp;

    while(Test==false){
        for (a=1;a<500;a++){
            for (b=1;b<500;b++){
                temp=a+b+sqrt(a*a+b*b);
                if (temp==1000){
                    Test=true;
                    a_final=a;
                    b_final=b;
                    c_final=sqrt(a*a+b*b);}
            }
        }
    }
product=a_final*b_final*c_final;
cout<<"The product of the only pythagorean triple whose sum equals 1000 is: "<<product;
cout<<" a equals "<<a_final;
cout<<" b equals "<<b_final;
cout<<" c equals "<<c_final;
return 0;
}
