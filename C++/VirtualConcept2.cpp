#include<iostream>
using namespace std;

class A
{
public:
    void virtual funPrint(){cout<<"funPrint of class A"<<endl;};
};

class B:public A
{
public:
    void funPrint(){cout<<"funPrint of class B"<<endl;};
};

int main()
{
    A *p; //定义基类的指针
    A a;
    B b;
    p=&a;
    p->funPrint();
    p=&b;
    p->funPrint();
}
