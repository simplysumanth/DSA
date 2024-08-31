#include <iostream>
#include<limits.h>
using namespace std;

void countDigits(int N) {
  int count = 0;
  int num = N;
  while (N > 0) {
    int d = N % 10;
    if (d > 0) {
      if (num % d == 0) {
        count++;
      }
    }
    N = N / 10;
  }
  cout << count;
}

void reverseDigit(int x){
  int rev = 0;
  while(x > 0){
    int d = x%10;
    //check if rev*10 > INT_MAX or rev*10 < INT_MIN
    if(rev > INT_MAX/10 || rev < INT_MIN/10){
      cout<<0;
      break;
    }
    rev = (rev * 10) + d;
    x = x/10;
  }
  cout<<rev;
}

void gcd(long long A, long long B){
  long long gcd = 0;
  for(int i = 1; i<= min(A,B); i++){
      if(A%i == 0 && B%i == 0){
          gcd = i;
      }
  }
  cout<<gcd;
}

long long divisors(int n){
  long long res = 0;
  for(int i = 1; i<= n ;i++){
      if(n%i==0){
          res += i;
      }
  }
  return res;
}

void sumOfDivisors(int N)
{
  // Write Your Code here
  long long res = 0;
  for(int i = 1; i<= N; i++){
      res += divisors(i);
      cout<<"res : "<<res<<endl;
  }
  cout<< res;
}

int main() { sumOfDivisors(4); }