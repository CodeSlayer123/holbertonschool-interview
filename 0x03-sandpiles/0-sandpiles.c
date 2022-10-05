#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include "sandpiles.h"



_Bool is_stable(int grid1[3][3]){
    int i, j;
    bool lower_than_four = true;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            if (grid1[i][j] > 3)
            {
                    lower_than_four = false;
            }
        }

    }
    return lower_than_four;
}
void sandpiles_sum(int grid1[3][3], int grid2[3][3]){
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            grid1[i][j] = grid1[i][j] + grid2[i][j];
        }

    }



    while (1)
    {
        if (is_stable(grid1) == false)
        {
            printf("=\n");
            print_grid(grid1);
        } else{
            break;
        }
        for (i = 0; i < 3; i++)
        {
            for (j = 0; j < 3; j++)
            {

                if (grid1[i][j] > 3){

                    grid1[i][j] = grid1[i][j] - 4;

                    if (i < 2){
                        grid1[i+1][j]++;
                    }
                    if (j < 2){
                        grid1[i][j+1]++;
                    }
                    if (i > 0){
                        grid1[i-1][j]++;
                    }
                    if (j > 0){
                        grid1[i][j-1]++;
                    }


                }


            }

        }
    }


}




static void print_grid(int grid[3][3])
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            if (j)
                printf(" ");
            printf("%d", grid[i][j]);
        }
        printf("\n");
    }
}

