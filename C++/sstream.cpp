#include<string>
#include<iostream>
#include<sstream>
using namespace std;

int main()
{
  istringstream iss;
  string strvalue="32 24 2 134";
  iss.str(strvalue);
  for(int n=0; n<4; n++)
  {
    int val;
    iss>>val;
    cout<<val<<" ";
  }
  cout<<endl<<"Finish"<<endl;
  cout<<iss.str()<<endl;
  return 0;
}
