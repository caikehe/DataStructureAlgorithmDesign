#include<iostream>
using namespace std;

int partition(int *input, int l, int r)
{
    // set the last element as pivot
    int pivot = input[r];
    // put the elements smaller than pivot on the left size
    for(int i=l; i<r; i++)
    {
        if(input[i] < pivot)
        {
            int tmp = input[l];
            input[l] = input[i];
            input[i] = tmp;
            l++;
        }
    }
    // put pivot in the right position
    int tmp = input[l];
    input[l] = input[r];
    input[r] = tmp;
    return l;
}

void quickSort(int *input, int l, int r)
{
    if(l>r)
        return;
    int tmp = partition(input, l, r);
    quickSort(input, l, tmp-1);
    quickSort(input, tmp+1, r);
}

int main()
{
    int input[] = {1, 4, 10, 5, 8, 7, 2};
    int l = sizeof(input)/sizeof(input[0]);
    quickSort(input, 0, l-1);
    for(int i=0; i<l; i++)
        cout<<input[i]<<" ";
    cout<<endl;
}
