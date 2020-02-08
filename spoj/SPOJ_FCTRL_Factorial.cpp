#include <stdio.h>

using namespace std;

long getNumberOfZeros(long factorial);

int main() 
{
	long numOfTests = 0;
	long factorial = 0;
	long zeroNum = 0;
	
	scanf("%d", &numOfTests);
    
    
    for(int i = 0;i<numOfTests; i++)
    {
    	scanf("%d", &factorial);
			
		zeroNum = getNumberOfZeros(factorial);
		
		printf("%d \n",zeroNum);
		
	}
    return 0;
}

long getNumberOfZeros(long factorial)
{
	long zeroNum = 0;
	
	for(long i = 5; i < factorial; i = i * 5)
	{
		zeroNum = zeroNum + factorial / i;
	}
	return zeroNum;
}
