#include<iostream>
using namespace std;

class Vehicle
{
public:
    virtual void PrintTyre()=0; //纯虚函数是这样定义的
};

class Camion:public Vehicle
{
public:
    virtual void PrintTyre(){cout<<"Camion tyre four"<<endl;};
};

class Bike:public Vehicle
{
public:
    virtual void PrintTyre(){cout<<"Bike tyre two"<<endl;};
};

int main()
{    
    Vehicle *v;
    Camion c;
    v = &c;
    v->PrintTyre();
    Bike b;
    v = &b;
    b.PrintTyre();
    // char *s = "hello";
    char s[] = "hello";
    *s = 'W';
    cout<<s<<endl;
}
