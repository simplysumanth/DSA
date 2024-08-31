#include <bits/stdc++.h>
#include <iostream>
using namespace std;

// Hashing numbers using array
void hashNums(int a[]) {
  int q;
  int hash[100000] = {};
  cout << "Enter the no. of queries" << endl;
  cin >> q;
  while (q--) {
    int a;
    cout << "Enter the no. you want to hash: " << endl;
    cin >> a;
    hash[a]++;
    cout << "The count for " << a << " is :" << hash[a] << endl;
  }
}

// Hashing string using array
void hashString() {
  string s;
  cout << "Enter the string : ";
  cin >> s;

  // pre-compute
  int hash[265] = {0};
  for (int i = 0; i < s.size(); i++) {
    hash[(unsigned char)s[i]]++;
  }

  // Queries
  int q;
  cout << "Enter the no. of queries: ";
  cin >> q;
  while (q--) {
    char a;
    cout << "Enter the char : ";
    cin >> a;
    cout << "Count : " << hash[(unsigned char)a] << endl;
  }
}

void usingHashMap() {
  // get string
  string s;
  cin >> s;

  // init hashmap
  map<char, int> mpp;

  // precompute
  for (int i = 0; i < s.length(); i++) {
    mpp[s[i]]++;
  }

  // Ouput
  int q;
  cout << "Enter the no. of queries : ";
  cin >> q;
  while (q--) {
    char a;
    cout << "enter the char : " << endl;
    cin >> a;
    cout << "Count of " << a << " is : " << mpp[a] << endl;
  }
}

int main() {}