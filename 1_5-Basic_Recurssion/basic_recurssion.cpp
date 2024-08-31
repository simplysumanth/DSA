#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int fibo(int n){

  //base condition
  if (n<2){
    return n;
  }
  return fibo(n-1) + fibo(n-2);
}

int factorial(int n){

  //base condition
  if(n==0){
    return 1;
  }
  //recursive call
  return n * factorial(n-1);
}

void reverseArray(int a[], int l, int n){
  if(l>=n/2){
    return;
  }
  swap(a[l], a[n-l-1]);
  reverseArray(a, l+1,n);
}

bool isPalindrome(int i, string &s){
  if(i>=s.length()/2) return true;

  if(s[i] != s[s.length()-i-1]) return false;

  return isPalindrome(i+1,s);
}

int main() {
  //int a[5] = {1,2,3,4,5};
  // reverseArray(a, 0, 5);
  // for(int i = 0; i<5;i++){
  //   cout<<a[i];
  // }

  string str = "A man, a plan, a canal: Panama";
  cout<<isPalindrome(0,str);
}