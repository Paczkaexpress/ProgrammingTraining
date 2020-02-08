#include <iostream>
#include <stdio.h>

using namespace std;



int main() 
{
	int number = 0;
	
	while(1)
	{
		scanf("%d",&number);
		if(number == 42)
			break;
		printf("%d \n",number);
	}
    return 0;
}
