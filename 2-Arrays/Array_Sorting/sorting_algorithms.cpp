#include <bits/stdc++.h>
#include <iostream>
using namespace std;

void bubble_sort_asc() {
  int a[5] = {4, 1, 3, 5, 2};
  int n = sizeof(a) / sizeof(int);
  for (int i = n - 1; i > 0; i--) {
    bool didSwap = false;
    for (int j = 0; j < i; j++) {
      if (a[j] > a[j + 1]) {
        swap(a[j], a[j + 1]);
        didSwap = true;
      }
    }
    if (didSwap == false) {
      break;
    }
    cout << "run" << endl;
  }

  for (auto i : a) {
    cout << i << " ";
  }
}

void bubble_sort_desc() {
  int a[5] = {5, 4, 3, 2, 1};
  int n = sizeof(a) / sizeof(int);
  for (int i = n - 1; i > 0; i--) {
    bool didSwap = false;
    for (int j = 0; j < i; j++) {
      if (a[j] < a[j + 1]) {
        swap(a[j], a[j + 1]);
        didSwap = true;
      }
    }
    if (didSwap == false) {
      break;
    }
    cout << "run" << endl;
  }

  for (auto i : a) {
    cout << i << " ";
  }
}

void insertion_sort() {
  int a[5] = {5, 4, 3, 2, 1};
  int n = sizeof(a) / sizeof(int);
  for (int i = 0; i < n; i++) {
    int j = i;
    cout << "pre : j : " << j << endl;
    ;
    while (j > 0 && a[j] < a[j - 1]) {
      swap(a[j - 1], a[j]);
      j--; // VERYYYY IMPORTANT AS WE ARE COMPARING ALL ELEMENTS TO THE LEFT
    }
    cout << "post : j : " << j << endl;
  }

  for (auto i : a) {
    cout << i << " ";
  }
}

void merge(vector<int> &arr, int l, int m, int h) {
  int left = l;
  int right = m + 1;
  vector<int> temp;
  while (left <= m && right <= h) {
    if (arr[left] <= arr[right]) {
      temp.push_back(arr[left]);
      left++;
    } else {
      temp.push_back(arr[right]);
      right++;
    }
  }
  while (left <= m) {
    temp.push_back(arr[left]);
    left++;
  }
  while (right <= h) {
    temp.push_back(arr[right]);
    right++;
  }

  // insert into main array
  for (int i = l; i <= h; i++) {
    arr[i] = temp[i - l];
  }
}

void merge_sort(vector<int> &arr, int l, int h) {
  if (l == h)
    return;
  int m = (l + h) / 2;
  merge_sort(arr, l, m);
  merge_sort(arr, m + 1, h);
  merge(arr, l, m, h);
}

void quick_sort(vector<int> &nums, int low, int high) {
  if (low >= high) {
    return;
  }
  int s = low;
  int e = high;
  int m = s + (e - s) / 2;
  int pivot = nums[m];

  while (s <= e) {
    // check if the elements to the left are < pivot
    // At the end we get the index which is > pivot as "s"
    while (nums[s] < pivot) {
      s++;
    }
    // check if the elements to the right are > pivot
    // At end we get the index which is < pivot as "e"
    while (nums[e] > pivot) {
      e--;
    }

    // At this point s might be > e, so check it again
    if (s <= e) {
      int temp = nums[s];
      nums[s] = nums[e];
      nums[e] = temp;
      s++;
      e--;
    }
  }

  // Now we have the index of the array less than and array greater than pivot
  //  e will be last index of lesser array [low ... e]
  //  s will be the first index of greater array [s .. high]
  quick_sort(nums, low, e);
  quick_sort(nums, s, high);
}

int main() {
  vector<int> arr = {5, 2, 1, 3, 4};
  quick_sort(arr, 0, 4);
  for (auto i : arr) {
    cout << i << " ";
  }
}