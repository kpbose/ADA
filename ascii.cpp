#include<iostream>
using namespace std;
void get_ascii(char c)
{
	int i=c;
	cout<<"\n ascii value of "<<c<<" is "<<i<<endl;
}
int main()
{
  get_ascii('a');
  get_ascii('z');
  get_ascii('A');
  get_ascii('Z');
  get_ascii('!');
  get_ascii('@');
return 0;
}
