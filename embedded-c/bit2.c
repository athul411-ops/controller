#include<stdio.h>
int main() {
int a =0x0f;
int d = a;
a |=(0X60);
printf("%d",a);
a &=~(0x07);
printf("\n a %d",a);
int c =((1<<2)-1)<<5;
printf("\n%d",c);

d |= c;
printf("\n%d",d);
d &=~(0x07);

printf("\n%d",d);
} 
