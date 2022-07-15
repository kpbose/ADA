#include<iostream>
using namespace std;
int n;
float Profit[10],Weight[10];
char item[10];
void string_swap(char a,char b)
{
	char temp=a;
	a=b;
	b=a;
}
int by_weight(int W)
{
	int i,j;
	for(i=0;i<n-1;i++)
	{
		for(j=0;j<n-i-1;j++)
		{
			if(Weight[j]>Weight[j+1])
			   {
			   swap(Profit[j],Profit[j+1]);
			   swap(Weight[j],Weight[j+1]);
			   string_swap(item[j],item[j+1]);
	        	}
	    }
	    
	}
	int cost=0;
	for(int i=0;i<n;i++)
	{
		if(W>=Weight[i])
		   {W=W-Weight[i];
		     cost=cost+Profit[i];
		   }
		else
		    {
		    	int temp=((W*Profit[i])/Weight[i]);
			    cost=cost+temp;
			    W=0;
			}
	}
	return cost;
}
int by_profit(int W)
{
	for(int i=0;i<n-1;i++)
	{
		for(int j=0;j<n-i-1;j++)
		{
			if(Profit[j]<Profit[j+1])
			{
				swap(Profit[j],Profit[j+1]);
			   swap(Weight[j],Weight[j+1]);
			   string_swap(item[j],item[j+1]);
			}
		}
	}
	int cost=0;
	for(int i=0;i<n;i++)
	{
		if(W>=Weight[i])
		   {W=W-Weight[i];
		     cost=cost+Profit[i];
		   }
		else
		    {
		    	int temp=((W*Profit[i])/Weight[i]);
			    cost=cost+temp;
			    W=0;
			}
	}
	return cost;
}
int by_p_w_ratio(int W)
{
	float PW[10];
	for(int i=0;i<n;i++)
	{
	  PW[i]=Profit[i]/Weight[i];
	}
	for(int i=0;i<n-1;i++)
	{
		for(int j=0;j<n-i-1;j++)
		{
			if(PW[j]<PW[j+1])
			{   swap(PW[j],PW[j+1]);
				swap(Profit[j],Profit[j+1]);
			   swap(Weight[j],Weight[j+1]);
			   string_swap(item[j],item[j+1]);
			}
		}
	}
	int cost=0;
	for(int i=0;i<n;i++)
	{
		if(W>=Weight[i])
		   {W=W-Weight[i];
		     cost=cost+Profit[i];
		   }
		else
		    {
		    	int temp=((W*Profit[i])/Weight[i]);
			    cost=cost+temp;
			    W=0;
			}
	}
	return cost;
}

int main()
{ int W;   
cout<<"\n Enter the capacity of the bag:: ";
     cin>>W;
    cout<<"\n Enter the number of items::";
    cin>>n;
	cout<<"\n Enter the name of the items::";
	cin>>item;
	cout<<"\n Enter the profit and Weight on items resp. "<<endl;
	for(int i=0;i<n;i++)
	{
		cout<<"\n On "<<item[i]<<" ";
		cin>>Profit[i]>>Weight[i];
	}
	for(int i=0;i<n;i++)
	{
		cout<<"\n On "<<item[i]<<" ";
		cout<<Profit[i]<<"::"<<Weight[i];
	}
	cout<<"\n Total cost by Weight :: "<< by_weight(W);
	cout<<"\n Total cost by  Profit :: "<<by_profit(W);
	cout<<"\n Total cost by P/W ratio :: "<<by_p_w_ratio(W);
return 0;
}
