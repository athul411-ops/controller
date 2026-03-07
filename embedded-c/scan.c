#include<stdio.h>
int main() {
int a;
scanf(" %d ",&a);

float b;
scanf(" %f",&b);
int  c;

int *d =&c;
scanf(" %d",d);

printf("%d\n%f\n%d",a,b,*d);

}
