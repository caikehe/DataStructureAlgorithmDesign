#include<vector>
#include<iostream>
using namespace std;

int main()
{
  # if defined(__sgi)
    cout<<"__sgi"<<endl;
  # endif
  
  # if defined(__GNUC__)
    cout<<__GNUC__<<" "<<__GNUC_MINOR__<<endl;
    cout<<__GLIBC__<<endl;
  # endif
  return 0;
}
