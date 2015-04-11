#include<iostream>
using namespace std;

int main()
{
  int s[]={5,3,4,8,6,7};
  int l=sizeof(s)/sizeof(*s);
  int len=1;
  int *d=new int[l];
  for(int i=0;i<l;i++)
  { 
    d[i]=1;
    for(int j=0;j<i;j++)
      if(s[j]<=s[i] && d[j]+1>d[i])
        d[i]=d[j]+1;
    if(d[i]>len) 
      len=d[i];
  }
  cout<<"the size of the longest increasing subsequence is: "<<len<<endl;
  delete []d;
  return 0;
}
