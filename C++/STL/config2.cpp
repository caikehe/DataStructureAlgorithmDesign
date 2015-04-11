#include<iostream>
using namespace std;

//class or typename
template <class T>
class testClass{
  public:
    static int _data;
};

static int testClass<int>::_data = 1;
static int testClass<char>::_data = 2;

int main()
{
  cout<<testClass<int>::_data<<endl;
  cout<<testClass<char>::_data<<endl;
  testClass<int> obj1, obj2;
  testClass<char> obj3, obj4;
  cout<<obj1._data<<"  "<<obj2._data;
  cout<<obj3._data<<"  "<<obj4._data;
  obj1._data = 3;
  obj3._data = 4;
  cout<<obj1._data<<"  "<<obj2._data;
  cout<<obj3._data<<"  "<<obj4._data;
  return 0;
}
