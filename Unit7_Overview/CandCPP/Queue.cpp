#include <iostream>
#include "string.h"

using namespace std;
namespace Queue
{
    void enQueue(int);
    int deQueue();
}
void testQ(int n)
{
    Queue::enQueue(n);
    if(Queue::deQueue() == n) cout << "PASS\n";
    else cout << "FAIL\n";
}
namespace Queue
{
    const int maxSize=100;
    int val[maxSize];
    int num=0, front=0, rear=0;
    bool isFull=0;
    
    void enQueue(int n)
    {
        if(isFull) return;
        val[rear]=n;
        num++;
        rear=(rear+1)% maxSize;
        if(num==maxSize) isFull=1;
    }
    
    int deQueue()
    {
        if(num==0) return-1;
        int temp = val[front];
        front =(front+1)% maxSize;
        num--;
        return temp;
    }
}
int main()
{
    testQ(35);
}
