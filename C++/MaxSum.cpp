#include<iostream>
using namespace std;

int main()
{
  int a[]={1,-2,3,10,-4,7,2,-5};
  int sum=0;
  int len=sizeof(a)/sizeof(*a);
  int b=0; // record the sum value until current position 
  for(int i=0;i<len;i++)
  {
    if(b<0)
      b=a[i];
    else 
      b+=a[i];
    if(sum<b) //deal with the last element in the array 
      sum=b;
  }
  cout<<"Maximal Sum is: "<<sum<<endl;
  return 0;
}
