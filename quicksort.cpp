#include<iostream>
using namespace std;
int A[10];
int partition(int , int );
void quicksort(int , int );

int main()
{
  int n ;
  
  cout<<"\n Enter the no of elements u want in array";
  cin>>n;
  
  cout<<"\n Enter the elements in array";
    for(int i=0; i<=n; i++)
  cin>>A[i];  
  
  cout<<"\n\n array before quick sort";
  for(int i=0; i<=n; i++)
  cout<<"\t"<<A[i];
  
  quicksort(0 ,n );
  cout<<"\n\n array after quick sort";
  for(int i=0; i<=n; i++)
  cout<<"\t"<<A[i];
}

int partition(int low, int high){
  int pivot = A[low];
  int i = low;
  int j = high+1;
  
  while(i<j){
    
    do{
      i++;
    }
    while(A[i] < pivot);
    
    do{
      j--;
    }
    while(A[j] >pivot);
      
    
    if(i <= j){
        swap(A[i], A[j]);
  }
}
        swap(A[low], A[j]);      //swapping pivot with A[j]
      return j;                //returning pivot index
}
void quicksort(int low, int high)
{
  if(low <= high){
    int pi = partition(low, high); //pi is partioning index
    quicksort(low, pi-1);
    quicksort(pi+1, high);
  }
}