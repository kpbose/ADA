#include<iostream>
using namespace std;
void find_triplet(int a[10],int n)
{  int temp,ans;
	for(int i=0;i<n;i++)
	{
	for(int j=0;j<n;j++)
	{
		if(i!=j)
		{
			temp=(a[i]*a[i])+(a[j]*a[j]);
	for(int k=0;k<n;k++)
	{
		if(k!=i && k!=j && i!=j)
		{
			ans=a[k]*a[k];
			if(ans==temp)
			   cout<<"\n numbers of pythagoras triplet::("<<a[i]<<")^2+("<<a[j]<<")^2=("<<a[k]<<")^2"<<endl;
		}
	}
}
	}
	}
}
int main()
{
	int n;
	int a[10];
	cout<<"\n Enter the size of the array::";
	cin>>n;
	cout<<"\n Enter the elements of the array::";
	for(int i=0;i<n;i++)
	{
		cin>>a[i];
	}
	find_triplet(a,n);
return 0;
}
