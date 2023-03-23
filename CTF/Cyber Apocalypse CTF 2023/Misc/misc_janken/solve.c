#include <cstdlib>
#include <iostream>
#include <time.h>
using namespace std;

int main()
{
    long long int time;
    cin >> time;
	srand(time);
    cout << rand()%3;
	return 0;
}
