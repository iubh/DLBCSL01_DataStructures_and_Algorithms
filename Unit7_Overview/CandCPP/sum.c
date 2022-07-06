#include <stdio.h>
int fun(int i, int j, int k);

int main() {
    int a = 2, b = 3, c=1;
    printf("a=%d, b=%d, c=%d\n",a,b,c);
    printf("Result=%d\n",fun(a,b,c));
    return 0;
}

int fun(int i, int j, int k)
{
   return (i+j+k);
}
