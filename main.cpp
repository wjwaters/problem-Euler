#include <iostream>


using namespace std;

int main()
{
int i,j,digit,num,numInitial,num_large=10100,rev;
//int digit,rev=0,num=9702;
    for(i=999;i>100;i--){
        for(j=999;j>100;j--){
            //cout<<i*j;
            numInitial=i*j;
            num=i*j;
            rev=0;
            do
            {
                digit = num % 10;
                rev = (rev * 10) + digit;
                num = num / 10;
            }  while (num != 0);
//cout<<"the reversed number is: "<<rev;
        //cout<<numInitial<<rev;
            //cout<<rev;
            if(numInitial==rev && numInitial>num_large){
                    num_large=numInitial;}

        }
         // }
    }
cout<<"The largest palindrome product of 2 3-digit numbers is: "<< num_large <<endl;
return 0;
}
