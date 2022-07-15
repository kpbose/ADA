#include<iostream>
using namespace std;
int  Add1[4][4],Res[4][4],Subt[4][4],Add[4][4],Ans[4][4],p8[4][4],p9[4][4],p10[4][4],p11[4][4];
void add(int n,int A[4][4],int B[4][4])
{   
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			Add[i][j]=A[i][j]+B[i][j];
		}
	}
}
void subt(int n,int A[4][4],int B[4][4])
{
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			Subt[i][j]=A[i][j]-B[i][j];
		}
	}	
}
void display(int r,int c,int A[4][4])
{
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{ 
			cout<<A[i][j]<<" ";
		}
		cout<<endl;
	}
}
void Assign(int r,int A[4][4],int Ans[4][4])
{
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<r;j++)
		{
			A[i][j]=Ans[i][j];
		}
	}
}
void Strassen(int start,int r,int c,int A[4][4],int B[4][4])
{   int a[4][4],b[4][4],c1[4][4],d[4][4],e[4][4],f[4][4],g[4][4],h[4][4];
	int size;
	if(c>r)
	  size=c-start;
	else
	    size=r-start;
	if(size==1)	   
	{
	    Ans[0][0]=A[0][0]*B[0][0];	
	}
	else
	{//Dividing matrix A and B in 4 equal parts
	int k=0,l;
	for(int i=start;i<r/2;i++)
	{  l=0;
		for(int j=start;j<c/2;j++)
		{  
			a[k][l]=A[i][j];
			e[k][l]=B[i][j];
			l++;
		}
		k++;
	}
	k=0;
	for(int i=r/2;i<r;i++)
	{  l=0;
		for(int j=start;j<c/2;j++)
		{
			c1[k][l]=A[i][j];
			g[k][l]=B[i][j];
		l++;
		}
		k++;
	}
	k=0;
	for(int i=start;i<r/2;i++)
	{  l=0;
		for(int j=c/2;j<c;j++)
		{
			b[k][l]=A[i][j];
			f[k][l]=B[i][j];
		l++;
		}
		k++;
	}
	k=0;
	for(int i=r/2;i<r;i++)
	{  l=0;
		for(int j=r/2;j<c;j++)
		{
			d[k][l]=A[i][j];
			h[k][l]=B[i][j];
		l++;
		}
		k++;
	}
	//1st formula
	subt(r/2,f,h);
	Strassen(0,r/2,c/2,a,Subt);
    int p1[4][4];
     Assign(r/2,p1,Ans);
	//2nd formula
	add(r/2,a,b);
	Strassen(0,r/2,c/2,Add,h);
	int p2[4][4];
	  Assign(r/2,p2,Ans);
	//3rd
	add(r/2,c1,d);
	Strassen(0,r/2,c/2,Add,e);
	int p3[4][4];
	   Assign(r/2,p3,Ans);
	//4th
	subt(r/2,g,e);
	Strassen(0,r/2,c/2,d,Subt);
	int p4[4][4];
	   Assign(r/2,p4,Ans);
	//5th
	add(r/2,a,d);
	Assign(r/2,Add1,Add);
	add(r/2,e,h);
	Strassen(0,r/2,c/2,Add1,Add);
	int p5[4][4];
	   Assign(r/2,p5,Ans);
	//6th
	subt(r/2,b,d);
	add(r/2,g,h);
	Strassen(0,r/2,c/2,Subt,Add);
	int p6[4][4];
	   Assign(r/2,p6,Ans);   
	//7th
	subt(r/2,a,c1);
	add(r/2,e,f);
	Strassen(0,r/2,c/2,Subt,Add);
	int p7[4][4];
	  Assign(r/2,p7,Ans);
	//8th  
	add(r/2,p5,p4);
	add(r/2,p6,Add);
	subt(r/2,Add,p2);
	    Assign(r/2,p8,Subt);
	//9th
	add(r/2,p1,p2);
	  Assign(r/2,p9,Add);
	//10th
	add(r/2,p3,p4);
	   Assign(r/2,p10,Add);
	//11th
	add(r/2,p1,p5);
	 Assign(r/2,Add1,Add);
	add(r/2,p3,p7);
	subt(r/2,Add1,Add);
	   Assign(r/2,p11,Subt);
    for(int i=0;i<r/2;i++)
    {
    	for(int j=0;j<r/2;j++)
    	{
    		Ans[i][j]=p8[i][j];
		}
	}
	k=0;
	for(int i=0;i<r/2;i++)
	{   int l=0;
		for(int j=c/2;j<c;j++)
		{
			Ans[i][j]=p9[k][l];
			l++;
		}
		k++;
	}
	k=0;
	for(int i=r/2;i<r;i++)
	{   int l=0;
		for(int j=0;j<c/2;j++)
		{
			Ans[i][j]=p10[k][l];
			l++;
		}
		k++;
	}
	k=0;
	for(int i=r/2;i<r;i++)
	{   int l=0;
		for(int j=c/2;j<c;j++)
		{
			Ans[i][j]=p11[k][l];
			l++;
		}
		k++;
	}
}
}
int main()
{
int A[4][4],B[4][4];
int n;
cout<<"\n Enter the number of rows and columns:: ";
cin>>n;
cout<<"\n Enter the elements of the matrix 1::";
for(int i=0;i<n;i++)
{
	for(int j=0;j<n;j++)
	{
		cin>>A[i][j];
	}
}
cout<<"\n Enter the elements of the matrix 2::";
for(int i=0;i<n;i++)
{
	for(int j=0;j<n;j++)
	{
		cin>>B[i][j];
	}
}
cout<<"\n Matrix 1 is ::"<<endl;
display(n,n,A);
cout<<"\n Matrix 2 is ::"<<endl;
display(n,n,B);
//Calling function for Strassen Matrix Mulltiplication
Strassen(0,n,n,A,B);
cout<<"\n Strassen Matrix Multiplication for Matrices is ::"<<endl;
display(n,n,Ans);
return 0;
}
