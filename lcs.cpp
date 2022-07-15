#include<iostream>
using namespace std;
string res;
int k=0;
void findseq(int ele,int l2,int l1,string a, string b,int A[10][10])
{   if(l2==0 ||l1==0)
     {
     	cout<<" ";
	 }
	 else
	 {
	int i=l2;
	int j=l1;
	if(ele==A[i-1][j])
	   {
	   	int el=A[i-1][j];
	    findseq(el,i-1,j,a,b,A);
	   }//upper
	else if(ele==A[i][j-1])
	{
		int el=A[i][j-1];
		findseq(el,i,j-1,a,b,A);
	}//left
	else
	 {  //diagonal
	   int el=A[i-1][j-1];
	findseq(el,i-1,j-1,a,b,A);
	   res[k]=a[l1-1];
	   cout<<a[l1-1]<<" ";
	   k++;
	//   findseq(el,i-1,j-1,a,b,A);
     }
}
}
int main()
{
	string a,b;
	int A[10][10];
	cout<<"\n Enter the string 1 :: ";
	cin>>a;
	cout<<"\n Enter the string 2 :: ";
	cin>>b;
	int l1=a.length();
	int l2=b.length();
	cout<<"\n The two strings are ::"<<endl;
	for(int i=0;i<l1;i++)
    {
    	cout<<a[i]<<" ";
	}
	cout<<endl;
	for(int j=0;j<l2;j++)
	{
		cout<<b[j]<<" ";
	}
	cout<<endl;
	for(int i=0;i<=l2;i++)
	{
		for(int j=0;j<=l1;j++)
		{
			 A[i][j]=0;
			
		}
		cout<<endl;
	}
	for(int i=0;i<=l2;i++)
	{
		for(int j=0;j<=l1;j++)
		{
			cout<<A[i][j]<<"\t";
		}
		cout<<endl;
	}
	for(int i=1;i<=l2;i++)
	{
		for(int j=1;j<=l1;j++)
		{
		if(b[i-1]==a[j-1])
		{
		   A[i][j]=1+A[i-1][j-1];
		   
      	}
		else
		   A[i][j]=max(A[i-1][j],A[i][j-1]);
		}
	}
	cout<<"\n ans is::"<<endl;
	for(int i=0;i<=l2;i++)
	{
		for(int j=0;j<=l1;j++)
		{
			cout<<A[i][j]<<"\t";
		}
		cout<<endl;
	}
	cout<<"\n Sequence is::"<<endl;
	int ele=A[l2][l1];
	findseq(ele,l2,l1,a,b,A);
	

	return 0;
}
