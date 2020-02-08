#include <iostream>
#include <stdio.h>

using namespace std;

long primeTabSize = 100000; //31622 = sqrt(1000000000)
long testSize = 100000;
long startingPoint = 0;
bool primeTab[100000];
bool solutionTab[100000];

void initSieve();
void segmentedSieve(long,long);
void cleanSegmentetSieveTable();

int main() 
{
	long numOfTests = 0;
	long n;
	long m;
	primeTab[1] = 1;
	
	scanf("%d", &numOfTests);
    
    initSieve();
    
    for(int i = 0;i<numOfTests; i++)
    {
    	scanf("%ld %ld", &n, &m);
			
		if(m>testSize)
		{	
			cleanSegmentetSieveTable();
			segmentedSieve(n,m);
		}
		
		for(int i=0;i<=m-n;i++) 
		{	
			if(i+n<testSize)
			{
				if(primeTab[i+n] == 0)
					printf("%ld \n",i+n);
			}
			else
			{
				if(solutionTab[i] == 0)
					printf("%ld \n",i+n);
			}
		}
		printf("\n");
	}
    return 0;
}

void initSieve()
{
	for(int i = 2;i<primeTabSize;i++)\	
	{
		if(primeTab[i] == 1)
			continue;
			
		for(int j = 2*i;j<primeTabSize;j=j+i)
		{
			primeTab[j] = 1;
		}
	}
}	

void segmentedSieve(long start, long end)
{
	int smallSieveStart = 0;
	
	for(int i = 2;i<primeTabSize;i++)
	{
		if(primeTab[i] == 1) //not a prime
			continue; 
		
		smallSieveStart = 	i * (start / i ) + i - start;
		if(i * (start / i ) == start)
			smallSieveStart = smallSieveStart - i;
			
		for(int j = smallSieveStart;j<=end-start+1;j=j+i)
		{
			solutionTab[j] = 1;
		}
	}
}

void cleanSegmentetSieveTable()
{
	for(int i =0; i<testSize; i++)
		solutionTab[i] = 0;
}
