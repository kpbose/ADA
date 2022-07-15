#include<iostream>
using namespace std;
void sorting(int a[10],int n)
{
for(int i=0;i<n;i++)
{
for(int j=i+1;j<n;j++)
{
if(a[i]<a[j])
swap(a[i],a[j]);
}
}
}
void disp(int a[10],int n)
{
for(int i=n-1;i>=0;i--)
{
cout<<a[i]<<"::";
}
cout<<endl;
}
void merge(int a[10],int n)
{
for(int i=n-1;i>0;i--)
{
 a[i-1]=a[i]+a[i-1];
 n--;
 sorting(a,n);
 disp(a,n);
}
}
int main()
{
int a[10],n;
cout<<"\n Enter the no of files::";
cin>>n;
cout<<"\n Enter the files::";
for(int i=0;i<n;i++)
cin>>a[i];
sorting(a,n);
disp(a,n);
merge(a,n);
}