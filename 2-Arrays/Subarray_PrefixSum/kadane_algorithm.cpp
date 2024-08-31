#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
  vector<int> nums = {-2,1,-3,4,-1,2,1,-5,4};
  int sum = 0;
  int maxi = INT_MIN;
  int start = 0, maxStart = -1, maxEnd = -1;
  for(int i =0; i< nums.size(); i++){
    if(sum == 0){
      start = i;
    }
    
    sum += nums[i];
    if(sum > maxi){
      maxi = sum;
      maxStart = start;
      maxEnd = i;
    }
    if(sum < 0){
      sum = 0;
    }
  }
  cout<<"Max sum : "<<maxi<<endl;
  cout<<"MaxStart : "<<maxStart << " MaxEnd : "<<maxEnd;  
}