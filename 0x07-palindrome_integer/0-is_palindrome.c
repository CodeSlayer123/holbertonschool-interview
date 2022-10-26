#include "palindrome.h"
#include <stdio.h>
int is_palindrome(unsigned long n){
   unsigned long reverse = 0;
   unsigned long num = n;

    while (num != 0) {
        reverse *= 10;
        reverse += num % 10;
        num /= 10;
    }

    if (reverse == n){
        return 1;
    }
    else {
        return 0;
    }
}
