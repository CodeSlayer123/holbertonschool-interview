#ifndef PALINDROME_H
#define PALINDROME_H
#include <stddef.h>


/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

int is_palindrome(unsigned long n);

#endif /* LISTS_H */