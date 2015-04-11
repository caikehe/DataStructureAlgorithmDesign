#include<iostream>
using namespace std;

int split(int input[], int a, int b)
{
  int pivot = input[b];
  while(a < b)
  {
    //select left elements
    while(input[a] < pivot)
      a++;
    while(input[b] > pivot)
      b--;
    if (input[a] == input[b])
      a++;
    else if(a < b)
    {
      int t = input[a];
      input[a] = input[b];
      input[b] = t;
    }
  }
  return b;
}

int quickSort(int input[], int a, int b)
{
  if(a < b)
  {
    int t = split(input, a, b);
    quickSort(input, a, t-1);
    quickSort(input, t+1, b);
  }
}

int main()
{
  int in[] = {2,1,3,9,8};
  quickSort(in, 0, 4);
  for(int i=0; i<5; i++)
    cout<<in[i]<<" ";
  cout<<endl;
}
