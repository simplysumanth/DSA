#include <iostream>
using namespace std;

void pattern_10(int n){
   /*    1 2 3 4 5
    1    *
    2    * *
    3    * * *
    4    * * * *
    5    * * * * *
    6    * * * *
    7    * * *
    8    * *
    9    *
  */
  int stars;
  for(int i = 1; i<= 2*n-1; i++){
    if(i<=n){
      stars = i;
    }else{
      stars = 2*n-i;
    }
    for(int j = 1; j<=stars; j++){
      cout<<"*";
    }
    cout<<endl;
  }
  
}

void pattern_11(int n){
  /*   1 2 3 4 5
  1    1
  2    0 1
  3    1 0 1
  4    0 1 0 1
  5    1 0 1 0 1
*/
  int start = 0;
  for(int i =1; i<= n; i++ ){
    if(i%2 == 0) start = 0;
    else start = 1;
    for(int j = 1; j<= i; j++){
      cout<<start;
      start = 1-start;
    }
    cout<<endl;
  }
}

void pattern_12(int n){
  /*
      1      1
      12    21
      123  321
      12344321
  */

  for(int i =1; i<=n;i++){
    //numbers
    for(int j = 1; j<= i; j++){
      cout<<j;
    }
    //space -> at each row, the no. of space is reduced by 2 (6->4->2->1) : 2*(n-1)
    //2*(n-i) -> n = 4, i=1 : 2(4-1) = 6 : i=2 -> 2(2)=4 ...
    for(int j = 1; j<= 2*(n-i); j++){
      cout<<" ";
    }
    //numbers
    for(int j = i; j>= 1; j--){
      cout<<j;
    }
    cout<<endl;
  }
}

void pattern_13(int n){
  /*  
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
*/
  int count = 1;
  for(int i=0; i<n;i++){
    for(int j =0; j<=i;j++){
      cout<<count;
      count++;
    }
    cout<<endl;
  }
}

void pattern_14(int n){
  /*
      A
      A B
      A B C
      A B C D
*/
  // i = n, j = i , print = A++
  for(int i = 0; i< n; i++){
    char digit = 'A';
    for(int j = 0; j<= i ; j++){
      cout<<digit;
      digit++;
    }
    cout<<endl;
  }
}

void pattern_15(int n){
  /*
    A B C D E
    A B C D
    A B C
    A B
    A
*/
  for(int i = 0;i<n;i++){
    char digit = 'A';
    for(int j = 0; j<n-i;j++){
      cout<<digit;
      digit++;
    }
    cout<<endl;
  }
}

void pattern_16(int n){
  /*
    A
    B B
    C C C
    D D D D
    E E E E E
*/
  char digit = 'A';
  for(int i = 0; i<n; i++){
    for(int j = 0; j<= i; j++){
      cout<<digit;
    }
    digit++;
    cout<<endl;
  }
}

void pattern_17(int n){
  /*
          A
        A B A
      A B C B A
    A B C D C B A
*/
  for(int i = 0; i<n ; i++){
    //space
    for(int j = 0; j<= n-i; j++){
      cout<<" ";
    }
    //digits
    char digit = 'A';
    for(int j =0; j< 2*i + 1; j++){
      cout<<digit;
      if(j >= i){
        digit--;
      }else{
        digit++;
      }
    }
    //space
    for(int j = n-i; j>= 0; j--){
      cout<<" ";
    }
    cout<<endl;
  }
  
}

void pattern_18(int n){
  /*
      E
      D E
      C D E
      B C D E
      A B C D E

      n = 5 , d = d + n - i
*/
  for(int i = 1; i<=n;i++){
    char digit = 'A' + n - i;
    for(int j = 1; j<= i; j++){
      cout<<digit;
      digit++;
    }
    cout<<endl;
  }
}

void pattern_19_1(int n){
  /*
      ******
      **  **
      *    *
      N= 3
*/
  int space = 0;
  for(int i=0;i<n;i++){
    //stars [3,2,1]
    for(int j = 0; j<n-i; j++){
      cout<<"*";
    }

    //space [0,2,4]
    for(int j = 0; j<space; j++){
      cout<<" ";
    }

    //stars [3,2,1]
    for(int j = 0; j<n-i; j++){
      cout<<"*";
    }
    space+=2;
    cout<<endl;
  }
}

void pattern_19_2(int n){
  /*
      *    *
      **  **
      ******
      
      N= 3
*/
  int space = 2*n-2;
  for(int i=0;i<n;i++){
    //stars [3,2,1]
    for(int j = 0; j<=i; j++){
      cout<<"*";
    }

    //space [0,2,4]
    for(int j = 0; j<space; j++){
      cout<<" ";
    }

    //stars [3,2,1]
    for(int j = 0; j<=i; j++){
      cout<<"*";
    }
    space-=2;
    cout<<endl;
  }

}

void pattern_19(int n){

  /*  
      ******
      **  **
      *    *
      *    *
      **  **
      ******
*/
  pattern_19_1(n);
  pattern_19_2(n);
}

void pattern_20(int n){
  /*
    *    *
    **  **
    ******
    **  **
    *    *
    N = 3
*/
  int space = 2*n-2; //4
  for(int i=1;i<=2*n-1;i++){
    int stars = i;
    if(i>n) stars = 2*n-i;
    //stars [1,2,3,2,1]
    for(int j = 0; j< stars; j++){
      cout<<"*";
    }

    //space[4,2,0,2,4]
    
    for(int j =0;j<space;j++){
      cout<<" ";
    }
    if (i<n) space -= 2;
    else space += 2;
    
    //stars[1,2,3,2,1]
    for(int j = 0; j< stars; j++){
      cout<<"*";
    }
    cout<<endl;
  }
}

void pattern_21(int n){
  /*
      ****
      *  *
      *  *
      ****
      N=4
*/
  for(int i=0;i<n;i++){
    for(int j = 0; j< n;j++){
      if(i==0 || i==n-1 || j == 0 || j == n-1){
        cout<<"*";
      }else{
        cout<<" ";
      }
    }
    cout<<endl;
  }
}

void pattern_22(int n){
  /*
      3 3 3 3 3 
      3 2 2 2 3 
      3 2 1 2 3 
      3 2 2 2 3 
      3 3 3 3 3
      
      N = 3
*/
  for(int i=0;i<2*n-1;i++){
    for(int j = 0; j< 2*n-1; j++){
      int top = i;
      int left = j;
      int right = 2*n-j-2;
      int down = 2*n-i-2;

      cout<<(n-min(min(top,down), min(left,right)));
    }
    cout<<endl;
  }
}

int main() {
  int n;
  cout<<"Enter n : ";
  cin>>n;
      pattern_22(n);
  
}