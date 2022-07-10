#include<iostream>
using namespace std;
int main() {
	int np,s1,s2,s3,S=0;
	cin >> np;
	for (int i = 0; i < np; i++) {
		cin >> s1 >> s2 >> s3;
		if (s1 + s2 + s3 >= 2) {
			S += 1;
		}
	}
	cout << S;

}