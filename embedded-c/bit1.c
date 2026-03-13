#include<stdio.h>
int main ()
{
int a =0x5f;
int b;
b = (a & 0xf0) >> 4;
printf("a= %d b = %d ",a,b);
}

