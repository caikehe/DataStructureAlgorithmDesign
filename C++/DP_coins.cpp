#include<iostream>
using namespace std;

int main()
{
  int S=21;
  int *Min=new int[S+1];
  for(int i=0;i<S+1;i++)
    Min[i]=9999;
  Min[0]=0;
  int f[]={1,3,5};
  for(int i=1;i<=S;i++)
    for(int j=0;j<int(sizeof(f)/sizeof(f[0]));j++)
      if(f[j]<=i && Min[i-f[j]]+1<Min[i])
       {
          Min[i]=Min[i-f[j]]+1;
       }
   
  cout<<"The minimal step is: "<<Min[S]<<endl;
  
  delete []Min;
  return 0;
}
