#include <stdio.h>

int main()
{
  int math_jc(n){
    int n = 5;
    if ( n == 1) {
      return 1;
    }
    else {
      return n * math_jc(n - 1)
    }
  }
}
