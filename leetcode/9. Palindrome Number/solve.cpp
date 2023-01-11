class Solution {
public:
    bool isPalindrome(int x) {
      if (x < 0) {return false;}
      long long int n = x,reversed_number=0,remainder;
        while(n != 0) {
          remainder = n % 10;
          reversed_number = reversed_number * 10 + remainder;
          n /= 10;
  }

  return (x==reversed_number);

    }
};
