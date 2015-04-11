#include<iostream>
#include<queue>
using namespace std;

int main()
{
  queue<int> my;
  int a;
  cout<<"please enter:"<<endl;
  do{
      cin>>a;
      my.push(a);
    }while(a);
  cout<<"contains:"<<endl;
  while(!my.empty())
  {
    cout<<my.front();
    my.pop();
  }
  cout<<"\n";
  return 0;
}
