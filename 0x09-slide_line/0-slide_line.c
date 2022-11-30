
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include "slide_line.h"


int slide_line(int *line, size_t size, int direction){

    if (direction == SLIDE_LEFT){
        slide_left(line,size);
        return 1;
    }

    if (direction == SLIDE_RIGHT){
        slide_right(line,size);
        return 1;
    }
    return 0;
}


void slide_left(int *line, size_t size) {
    size_t i;
    int direction = SLIDE_LEFT;

    slide(line, size, direction);

    for (i = 0; i < size; i++){
        if (i > 0){
            if (line[i] == line[i - 1]){
                line[i - 1] += line[i];
                line[i] = 0;
            }
        }
    }

    slide(line, size, direction);

}


void slide_right(int *line, size_t size) {
    size_t i;
    int direction = SLIDE_RIGHT;

    slide(line, size, direction);

    for (i = size - 1; 1; i--){
        if (i < size - 1){
            if (line[i] == line[i + 1]){
                line[i + 1] += line[i];
                line[i] = 0;
            }
        }
        if (i == 0){
            break;
        }
    }

    slide(line, size, direction);

}

void slide(int *line, size_t size, int direction) {
    size_t i;
    size_t j;
    if (direction == SLIDE_LEFT){
        for (i = 0; i < size; i++){
            if (line[i] == 0 ){
                for (j = i; j < size; j++){
                    if (line[j] != 0){
                        line[i] = line[j];
                        line[j] = 0;
                        break;
                    }
                }
            }
        }
    } else {
        for (i = size - 1; i > 0; i--){

            if (line[i] == 0 ){
                for (j = i; i; j--){
                    if (line[j] != 0){
                        line[i] = line[j];
                        line[j] = 0;
                        break;
                    }
                    if (j == 0){
                        break;
                    }
                }
            }
        }
    }


}
