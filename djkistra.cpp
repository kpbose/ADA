#include <iostream>
using namespace std;
#define INFINITE 32000

class Dijkstra{
	int *Graph;//adjacency matrix for graph
	int *spt;//shortest path tree
	bool *visited;//visited nodes list
	int n;//no. of nodes
	int source_node;
	
	public:
		void setGraph(){
			cout << "Enter number of nodes in graph : ";
			cin >> n;

			Graph = new int[n*n];
			
			cout << "Enter graph in adjacency matrix(if node is not connected enter 0) : \n";
			for (int i=0; i<n; i++)
				for (int j=0; j<n; j++){
					cin >> *(Graph+i*n+j);
				}
			
			cout << "Enter source node[1 to "<<n<<"] : ";
			cin >> source_node;
			source_node -= 1;
			
			spt = new int[n];
			for (int i=0; i<n; i++)
				spt[i] = INFINITE;
			spt[source_node] = 0;
			
			visited = new bool[n];
			for (int i=0; i<n; i++)
				visited[i] = false;
		}
		
		void shortest_path(){
			for (int count=0; count<n-1; count++){
				// Initialize min value
 		   		int min = INFINITE, u;
 				for (int v = 0; v < n; v++)
        			if (visited[v] == false && spt[v] <= min)
            			min = spt[v], u = v;
            
    			// Mark the picked vertex as visited
        		visited[u] = true;
 
        		// Update shortest path value of the adjacent vertices of the picked vertex.
        		for (int v = 0; v < n; v++){
 
            		// Update spt[v] only if is not in visited, there is an edge from
            		// u to v, and total weight of path from src to  v through u is
            		// smaller than current value of spt[v]
	            	if (!visited[v] && *(Graph+u*n+v) && spt[u] + *(Graph+u*n+v) < spt[v])
    	            	spt[v] = spt[u] + *(Graph+u*n+v);
				}
			}
		}
		
		void display(){
			cout << "\nShortest Path from source node...";
			for (int i=0; i<n; i++)	
				cout <<"\n "<<source_node+1<<"->"<< i+1 <<"  "<<spt[i];
		}
};

int main(){
	Dijkstra a;
	a.setGraph();
	a.shortest_path();
	a.display();	
}