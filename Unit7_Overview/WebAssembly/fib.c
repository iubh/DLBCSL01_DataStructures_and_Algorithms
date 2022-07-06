int fib(int n)
{
  int curr, next, sum;
  curr = 1;
  next = 1;
  for(int i = 1; i <= n-2; i++) {
     sum = curr + next;
     curr = next;
     next = sum;
  }
  return sum;
}
