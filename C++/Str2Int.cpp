#include<iostream>
using namespace std;

int Str2Int(char* string)
{
  if(string==NULL)
    return 111;
  int num = 0;
  while(*string!=0)
  {
    num = num*10+*string-'0';
    string++;
  }
  return num;
}

int main()
{
  char* str = NULL;
  cout<<Str2Int(str)<<endl;
  cout<<NULL<<endl;
  return 0;
}
