#include <iostream>
#include <stdio.h>

using namespace std;



int main() 
{
	long long numOfTests = 0;
	long long chocolatePiece = 0;
	long long mod_num = 0;
	long long result = 0;
	
	scanf("%d", &numOfTests);
    
    for(int i = 0;i<numOfTests; i++)
    {
    	scanf("%d", &chocolatePiece);
		result = 0;
		mod_num = chocolatePiece;

        for(int j = 0;j<numOfTests;j++)
        {
        	if(chocolatePiece == (1<<(numOfTests-j)))
        		break;
        	else
        	{
        		mod_num = mod_num>>1;
        		result = result + 1;
			}
		}
		
		printf("%i %i",1<<numOfTests, result);

	}
    return 0;
}
