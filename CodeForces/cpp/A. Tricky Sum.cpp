#include <iostream>

int main(){
	long long n,t;
	std::cin>>t;
	long long powers[32];
	powers[0] = 1;
	for (int i=1;i<32;i++){
	    powers[i] = powers[i-1]*2;
	}
	for (int i=0;i<t;i++){
	    std::cin>>n;
	    long long sum = ((1+n)*n)/2;
	    int power=0;
	    for (int i=0;i<32;i++){
	        if (powers[i] == n) {
	            power = power + powers[i];
	            break;
	        } else if (powers[i] > n){break;}
	        else {power = power + powers[i];}
	        

	    }
        long long ans = sum - power*2;
	    std::cout<<ans<<std::endl;
	}
}

