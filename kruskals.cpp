#include<iostream>

using namespace std;

int main()

{
    
int A[10][10],n;

string nodes;

cout<<"\n Enter the number of nodes::";

cin>>n;

cout<<"\n Enter the nodes::";

cin>>nodes;

cout<<"\n Enter the distance b/w nodes"<<endl;

for(int i=0;i<n;i++)

{  cout<<"\n From node "<<nodes[i];

for(int j=0;j<n;j++)

{

cout<<" To node "<<nodes[j];

cin>>A[i][j];

}

}

for(int i=0;i<n;i++)
{
	for(int j=0;j<n;j++)
	{
		cout<<A[i][j]<<"\t";
	}
	cout<<endl;
}
int sum=0;

for(int i=0;i<n-1;i++)

{  int min=999,to;

for(int j=0;j<n;j++)

{

if(min>A[i][j])
{
 min=A[i][j];

 to=j;
}
}

cout<<"\n From node "<<nodes[i]<<" to node "<<nodes[to]<<" distance is "<<min<<endl;

A[to][i]=999;

sum=sum+min;

}

cout<<"\n Total Cost is:: "<<sum;

return 0;

}
