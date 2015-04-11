#include<iostream>
using namespace std;

int compareToMax(int array[], int n)
{
  int curMax;
  if(n<=0)
    return -1;
  curMax = array[0];
  for(int i=1; i<n; i++)
    if(array[i]>curMax)
      curMax = array[i];
  return curMax;
}

int compareToAll(int array[], int n)
{
  for(int i=0; i<n; i++)
  {  
    bool isMax = true;
    for(int j=i+1;j<n;j++)
      if(array[i]<array[j])
      {
        isMax = false;  
        break;
      }
    if(isMax)
      return array[i];
  } 
}

int compareToAll1(int array[], int n)
{
  int i, j;
  bool isMax;
  if(n<=0)
    return -1;
  for(i=n-1; i>0; i--)
  {
    isMax = true;
    for(j=0; j<n; j++)
    {
      if(array[j]>array[i])
      {
        isMax = false;
        break;
      }
    }
    if(isMax)
      break;
  }
  return array[i];
}

int main(int argc, char** argv)
{
  int array[] ={11, 3, 4, 1, 5, 9, 7, 5};
  cout<<"Using compareToMax max is: "<<compareToMax(array, sizeof(array)/sizeof(array[0]))<<endl;
  cout<<"Using compareToAll max is: "<<compareToAll(array, sizeof(array)/sizeof(array[0]))<<endl;
  cout<<"Using compareToAll1 max is: "<<compareToAll1(array, sizeof(array)/sizeof(array[0]))<<endl;
  return 0;
}
