//华氏温度 - 摄氏温度
#include <stdio.h>

#define LOWER 0
#define UPPER 300
#define STEP 20

// test define 
int f2c_define() {
    int fahr;
    for(fahr=0; fahr<=UPPER; fahr=fahr+STEP)
        printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));

    return 0;
}

// test for 循环 
int print_fahr2celsius() {
    int fahr;
    for(fahr=0; fahr<=300; fahr=fahr+20){
        printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
    }
    return 0;
}

int main()
{   // while 循环方式
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;
    upper = 300;
    step = 20;


    fahr = lower;
    while(fahr <= upper) {
        celsius = (5.0/9.0)*(fahr-32.0);
        printf("%3.0f %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }

    printf("====================");
    //For 循环方式简单解决
    print_fahr2celsius();    
    printf("====================");
    // test define
    f2c_define();
}
