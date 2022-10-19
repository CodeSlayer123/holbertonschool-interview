#include "lists.h"
#include <stdio.h>
int is_palindrome(listint_t **head){
    listint_t **first;
    listint_t *last;
    listint_t *tmp;

    if (*head == NULL){
        return 1;
    }
    first = head;
    last = *first;
    tmp = *first;

    last = last->next;
    while(last->next != NULL){
        last = last->next;
        tmp = tmp->next;

    }
    while ((*first)->next != tmp){
        if (*first == tmp){
            break;
        }
        if ((*first)->n != last->n){
            return 0;
        }

        tmp = *head;
        if (tmp != last){
            while (tmp->next != last){
                tmp = tmp->next;
            }
        }
        *first = (*first)->next;
        last = tmp;

    }
    return 1;

}
