#include<stdio.h>

typedef struct st{
  int a;
  char ch;
}stru;

int main()
{
  struct st obj;
  stru *stobj=&obj;
  stobj->a=5;
  stobj->ch='a';
  printf("\n [%d] [%c]\n", stobj->a, stobj->ch);
  printf("\n [%d] [%c]\n",obj.a, obj.ch);
  return 0;
}
