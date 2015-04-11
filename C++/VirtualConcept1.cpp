#include<iostream>
using namespace std;

class A
{
public:
    int iValue;
};

class B:virtual public A
{
public:
    void bPrintf(){cout<<"This is class B"<<endl;};
};

class C:virtual public A
{
public:
    void cPrintf(){cout<<"This is class C"<<endl;};
};

class D:public B,public C
{
public:
    void dPrintf(){cout<<"This is class D"<<endl;};
};

int main()
{
    D d;
    cout<<d.iValue<<endl; //错误，不明确的访问
    cout<<d.A::iValue<<endl; //正确
    cout<<d.B::iValue<<endl; //正确
    cout<<d.C::iValue<<endl; //correct
    cout<<d.D::iValue<<endl;
}
