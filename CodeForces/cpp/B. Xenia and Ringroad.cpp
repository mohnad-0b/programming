
#include<iostream>
#include<vector>
using namespace std;
int main() {
	
	int host = 1;
	int time_unit = 0;
	int n, m;
	cin >> n >> m;
	vector <int>tasks;
	int t;
	for (int i = 0; i < m; i++) {
		cin >> t;
		tasks.push_back(t);
	}
	while (true) {
		
			if (tasks[0] == host) {
				while (true) {
					if (tasks.size() > 1 && tasks[0] == tasks[1]) {
						tasks.erase(tasks.begin());
					}
					tasks.erase(tasks.begin());
					break;
				}
			}
			if (tasks.empty() == true) { break; }
			if (host == n) {
				host = 0;
			}
			time_unit += 1;
			host += 1;
	}

	cout << time_unit;
	
}
