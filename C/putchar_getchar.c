#include <stdio.h>

void count() {
    long nc;

    nc = 0;
    while(getchar() != EOF) {
        ++nc;
    }
    printf("%ld\n", nc);
}

int main()
{
    int c;

//    count();

    c = getchar();
    while(c != EOF){
        putchar(c);
        c = getchar();
    }
}
