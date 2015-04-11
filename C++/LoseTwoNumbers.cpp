// This file is used to demonstrate the algrithm to find the two 
// losed numbers in a consecutive array.
#include<iostream>
using namespace std;

int main()
{
  // The array between 0 to 999 loses two numbers
  int a[998];
  int lose1=56;
  int lose2=198;
  for(int i=0; i<lose1-1; i++)
  {
    a[i]=i+1;
  }
  for(int i=lose1-1; i<lose2-2; i++)
  {
    a[i]=i+2;
  }
  for(int i=lose2-2; i<998; i++)
  {
    a[i]=i+3;
  }
  // Two numbers need to be found
  int lose1_find=0;
  int lose2_find=0;
  // find lose1^lose2 first
  int temp=0;
  for(int i=0; i<998; i++)
    temp^=a[i]^(i+1);
  temp^=999^1000;
  // find a "1" bit in temp (the right most bit 1)
  int bit1=temp-(temp&(temp-1));
  for(int i=0; i<998; i++)
  {
    if(bit1&a[i])
      lose1_find^=a[i];
  }
  for(int i=0; i<1000; i++)
  {
    if(bit1&(i+1))
      lose1_find^=(i+i);
  }
  lose2_find=lose1_find^temp;
  cout<<"The two losed numbers are: "<<lose1_find<<" "<<lose2_find<<endl;
  return 0;
}




