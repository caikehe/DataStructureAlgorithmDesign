#include<iostream>
#include<stack>
#include<string>
using namespace std;

int main()
{
  stack<int> my;
  //my.emplace("First");
  //my.emplace("Second");
  for(int i=0; i<5; ++i)
    my.push(i);
   
  cout<<"My stack is: "<<endl;
  while(!my.empty())
  {
    cout<<my.top()<<endl;
    cout<<"size is: "<<my.size()<<endl;
    my.pop();
  }
  return 0;
}
