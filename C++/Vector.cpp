#include<iostream>
#include<vector>
using namespace std;

int main()
{
  //vector<int> v1(5);
  //vector<int> v2(v1);
  //vector<int> v1(7,10);
  //vector<int> v1(7);
  //vector<int> v2(v1.begin(),v1.end());
  vector<int> v1;
  v1.assign(7,10);
  vector<int> v2;
  v2.assign(v1.begin(), v1.end());
  for(vector<int>::iterator it=v1.begin();it!=v1.end();it++)
    cout<<*it<<" ";
  cout<<endl;
  for(int i=0; i<v2.size(); i++)
    cout<<v2.at(i)<<" ";
  cout<<endl;
  cout<<v1.back()<<endl;
  cout<<v1.front()<<endl;
  //v1.clear();
  cout<<v1.size()<<" "<<v1.capacity()<<endl;
  vector<int>::iterator bit=v2.begin();
  v2.erase(bit);
  v2.insert(v2.begin(), 4, 100);
  v2.insert(v2.begin(), v1.begin(), v1.end());
  v2.pop_back();
  v1.swap(v2);
  for(int i=0; i<v2.size(); i++)
    cout<<v2.at(i)<<" ";
  cout<<endl;  
  cout<<v2.max_size()<<endl;
  return 0;
}
