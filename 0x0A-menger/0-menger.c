#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "menger.h"

void menger(int level){
    int size = pow(3, level);
    int i;
    int j;
    int z;
    int y;
    int x;

    for (y = 0; y < size; y++) {

        for (x = 0; x < size; x++) {
            i = x;
            j = y;

            for(z = 0; z < level; z++){
                if (i % 3 == 1 && j % 3 ==1){
                    break;
                }
                i /= 3;
                j /= 3;
            }
            if (z == level){
                printf("#");
            }
            else {
                printf(" ");
            }

        }

        printf("\n");
    }

}