#include<iostream>
using namespace std;
void staircase(int n, int sum, int steps[10],int s)
{  int t=s;   
if(sum==n)
    {
    	for(int i=0;i<s;i++)
    	{
    		cout<<steps[i];
		}
		cout<<endl;
    }
	else if(sum<n)
	{
		//with 1:
		  int newsum=sum+1;
		  steps[s]=1;
		  s++;
		  staircase(n,newsum,steps,s);
		//with 2
		   s=t;
		   int newsum1=sum+2;
		   steps[s]=2;
		   s++;
		   staircase(n,newsum1,steps,s);
	}
	else
	cout<<"\n-----"<<endl;
}
void steparray(int N,int sum,int steps[10],int s,int x[10],int n)
{ int t=s;
  int nsum=sum;   
if(sum==N)
       {
       	for(int i=0;i<s;i++)
       	{
       	cout<<steps[i]<<"::";	
		}
		cout<<endl;
	   }
	else
	if(sum<N)
	{
		for(int i=0;i<n;i++)
		{   
			sum=sum+x[i];
			steps[s]=x[i];
			s++;
			steparray(N,sum,steps,s,x,n);
		     s=t;
			 sum=nsum;	
		}
	}
}
int main()
{
	int N;
	int steps[10];
	cout<<"\n Enter the  number of steps in staircase::";
	cin>>N;
	//staircase(N,0,steps,0);
	int n;
	cout<<"\n Enter the number of elements of x::";
	cin>>n;
	int x[10];
	cout<<"\n Enter the elements of x::";
	for(int i=0;i<n;i++)
	{
		cin>>x[i];
	}
	steparray(N,0,steps,0,x,n);
return 0;
}
