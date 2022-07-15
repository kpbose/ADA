#include<iostream>
using namespace std;
void spiral(int a[10][10],int lr,int lc,int m,int n)
{  if(lr<m && lc<n)
{
int i,j;
	for(j=lc;j<n;j++)
	{
		cout<<a[lr][j]<<"::";
	}
	j=n-1;
	for(i=lr+1;i<n;i++)
	{
		cout<<a[i][j]<<"::";
	}
	i=n-1;
	for(j=n-2;j>=lc;j--)
	{
		cout<<a[i][j]<<"::";
	}
	j=lc;
	for(i=n-2;i>lr;i--)
	{
		cout<<a[i][j]<<"::";
	}
	spiral(a,lr+1,lc+1,m-1,n-1);

}}
int main()
{
	int m,n,a[10][10];
	cout<<"\n Enter the number of rows::";
	cin>>m;
	cout<<"\n Enter the number of columns::";
	cin>>n;
    cout<<"\n Enter the elements of matrix::";
    for(int i=0;i<m;i++)
    {
    	for(int j=0;j<n;j++)
    	{
    		cin>>a[i][j];
		}
	}
	cout<<"\n elements of the matrix are::"<<endl;
	for(int i=0;i<m;i++)
    {
    	for(int j=0;j<n;j++)
    	{
    		cout<<a[i][j]<<"\t";
		}
		cout<<endl;
	}
   spiral(a,0,0,m,n);
return 0;
}
