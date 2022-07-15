#include<iostream>
using namespace std;
int a[100];
void Merge(int low,int mid,int high)
{
int n1=mid+1-low;
int n2=high-mid;
int l[n1],r[n2];
    for(int i=0;i<n1;i++)
{
l[i]=a[low+i];
}
for(int j=0;j<n2;j++)
{
r[j]=a[mid+1+j];
}
int i=0,j=0,k=low;
while(i<n1 && j<n2)
{
if(l[i]<r[j])
   {
   a[k]=l[i];
   i++;
   k++;
       }
    else
      {
       a[k]=r[j];
       j++;
       k++;
  }   
}
while(i<n1)
{
a[k]=l[i];
i++;
k++;
}
while(j<n2)
{
a[k]=r[j];
j++;
k++;
}
}
void MergeSort(int low,int high)
{   
int j;
if(low<high)
{
    j=(high+low)/2;
    MergeSort(low,j);
    MergeSort(j+1,high);
    Merge(low,j,high);
}
}
int main()
{
int n;
cout<<"\n Enter the size of the array::";
cin>>n;
cout<<"\n Enter the elements of the array:::";
for(int i=0;i<n;i++)
{
cin>>a[i];
}
MergeSort(0,n-1);
cout<<"\n After Sorting Array be like::";
for(int i=0;i<n;i++)
{
cout<<a[i]<<"::";
}
}