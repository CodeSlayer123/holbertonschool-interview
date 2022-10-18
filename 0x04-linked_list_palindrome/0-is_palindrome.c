#include "lists.h"
#include <stdio.h>
int is_palindrome(listint_t **head){
    if (*head == NULL){
        return 1;
    }
    listint_t **first = head;
    listint_t *last = *first;
    listint_t *tmp = *first;

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
