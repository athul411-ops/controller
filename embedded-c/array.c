#include<stdio.h>
int main () 
{
int arr[5]={10,25,24,4,8};
int *p = arr;
int sum=0;
int max=arr[0];
for (int i=0;i<=4;i++)
{

sum +=*(p+i);

}

printf("%d\n",sum);

for (int i=0;i<=4;i++)
{

if (max < *(p+i))
{
max =*(p+i);
}
}
printf("%d max",max);
}





