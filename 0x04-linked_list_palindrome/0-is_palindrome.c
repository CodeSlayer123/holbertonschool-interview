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
    while ((*first)->next != NULL && last != *head){
        printf("test");
        if ((*first)->n != last->n){
            return 0;
        }
        *first = (*first)->next;
        last = tmp;
        tmp = *head;
        if (tmp != last){
            while (tmp->next != last){
                tmp = tmp->next;
            }
        }

    }
    return 1;

}