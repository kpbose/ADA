 #include<iostream>
using namespace  std;
int flag=0;
int bsearch(int[],int,int,int);
int main()
{
   int n,a[10],no;
   
   cout<<"Enter the no of elements you want in array";
   cin>>n;
   
   cout<<"Enter the values in array in ascending order";
   for(int i=1; i<=n; i++)
   cin>>a[i];
   
   cout<<"Enter the no. to be searched";
   cin>>no;
   
   int b=bsearch(a,0,n,no);
   if(b==0)
   cout<<"\n search is not succesful";
   else
   cout<<"\n search is succesful";
}

int bsearch(int a[],int low, int high,int no)
{
	if(low<=high)
	{
		int mid=(low+high)/2;
		if(a[mid]==no)
		{
			flag=1;
		}
		else if(a[mid]>no)
		{
			bsearch(a,low,mid-1,no);
		}
		else
		{
			bsearch(a,mid+1,high,no);
		}
	}
	else
	return flag;
}