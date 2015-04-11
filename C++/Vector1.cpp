#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main()
{
  vector<string> ss;
  ss.push_back("Hi, 111");
  ss.push_back("Hi, 222");
  ss.push_back("Hi, 333");
   
  cout<<"Constant Iterator:"<<endl;
  vector<string>::iterator cii;
  for(cii=ss.begin(); cii!=ss.end(); cii++)
    cout<<*cii<<endl;

  cout<<"Reverse Iterator:"<<endl;
  vector<string>::reverse_iterator rii;
  for(rii=ss.rbegin(); rii!=ss.rend(); rii++)
    cout<<*rii<<endl;

  cout<<"Swap output:"<<endl;    
  swap(ss.at(0),ss.at(3));
  cout<<ss.at(0)<<endl;
  
  cout<<"Out of range"<<endl;
  cout<<*ss.end()<<endl;
  return 0;
}
