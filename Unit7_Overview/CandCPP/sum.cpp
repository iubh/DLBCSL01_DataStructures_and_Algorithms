#include <iostream>
#include "string.h"
using namespace std;
template<class T> T fun(T i, T j, T k);
template<class T> T fun(T i, T j, T k)
{
   return (i+j+k);
}

int main() {
    int a = 2, b=3, c=1;
    std::cout << "a=" << a << ", b=" << b << ", c=" << c << "\n";
    std::cout << "Result  = " << fun(a,b,c) << "\n";
    float d=2.3, e=2.5, f=1.1;
    std::cout << "Result  = " << fun(d,e,f) << "\n";
    string r = "Apple", s = "Orange", t = "Peach";
     std::cout << "Result  = " << fun(r,s,t) << "\n";
    return 0;
}
