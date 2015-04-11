#include<iostream>
#include<list>
using namespace std;

int main()
{
  list<int> L;
  L.push_back(0);
  L.push_front(2);
  L.insert(++L.begin(), 2);
  L.push_back(9);
  //L.unique();
  L.sort(); 
  L.reverse(); 
  list<int>::iterator i;
  for(i=L.begin(); i!=L.end(); i++)
    cout<<*i<<" ";
  cout<<endl;
  return 0;
}
